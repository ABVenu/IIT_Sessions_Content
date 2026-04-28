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

10:25

Hello, am I audible?

10:31

Am I audible?

10:32

Yes, thanks for the confirmation.

10:37

So let's wait for five minutes and we see the significant participate that we can start.

10:48

Thank you.

11:18

Thank you.

11:48

Thank you.

12:18

Thank you

12:48

Thank you

13:18

Thank you

13:48

Hello everyone. Good evening.

13:53

So any doubt from the last class.

13:55

So any doubt from the last class?

14:00

So in the last class we covered class objects,

14:05

variables.

14:07

So there are two types of variables inside an object.

14:10

So one is per object variable and when it is shared among all the objects.

14:16

So that is called class variable.

14:17

So that is called class variable.

14:18

So similarly we have functions also. So our method, we can use that method to get or set the value to do some computation over it.

14:26

So today we are going to start some advanced topics in object related programming.

14:32

So the first topic is inheritance, okay? Inheritance simply says that, okay, so just try to see this.

14:40

Let's assume you already have a class whose name is animal.

14:44

So in class, you might have some attribute, right?

14:47

right?

14:48

Because whenever you are creating a class, you must have some attributes, you must have some

14:52

methods.

14:53

Now try to see cat and dog.

14:56

These are also two classes.

14:58

There must be some similarity between the attributes or the members of animal class and the cat class, right?

15:05

There's a slight difference in those functionality, but you can understand

15:10

there's similarity between cat and animal general class.

15:13

Similarly, there's a similarity.

15:15

Similarly, there's a common functionality shared among animal class and dog class.

15:21

So if this is the scenario that you already have created a class, and now you have to create a new class.

15:28

So let's see this scenario is you have to create a new class called cat, new class called dog,

15:34

and already you have a class called animal.

15:37

There are many features which is shared among us.

15:40

So whenever we are creating a new class cat, should we start from scratch?

15:44

from scratch or can I somehow use the already existing features or attribute of this animal class?

15:52

So the inheritance problem, inheritance tries to solve this problem.

15:56

Inheritance says that,

15:58

Inheritance says that, okay, you can inherit.

16:03

The new class can inherit some property of already existing classes.

16:08

So here already existing class is animal.

16:11

So whenever you are creating a new class cat, you are saying,

16:14

saying, okay, I'm going to inherit the attributes, method, which are already presented in animal.

16:20

And based on my need, I can modify the functionality, okay?

16:25

So you can see here, the arrow says that, okay, cat is a class and it inherits from animal class.

16:36

Similarly, dog is a class and it inherits property from animal class.

16:42

So what is inheritance?

16:44

Whenever you are creating a class, you are using some pre-existing class.

16:49

You are inheriting the property that is called inheritance.

16:52

So you are taking all the attributes which can be taken from the base class.

16:59

So this is used to reuse the code.

17:02

So why we are saying we are using the code?

17:04

So let's assume there is a functionality called animal can walk, right?

17:09

Animal can eat.

17:11

Animal can create a sound.

17:13

The sound.

17:14

For all animals are different, but the common functionality is they can create some sound, right?

17:19

So you can assume sound functionality is already provided in animal.

17:23

Whenever you are providing sound functionality for cat, you can simply say that, okay, I'm going

17:28

to take the sound functionality of the animal and then I'm going to rewrite it.

17:32

So rather than re-using, creating it from scratch, you are using it.

17:36

So whenever you will see the code, then it will give you the clarity.

17:39

But the only importance of the inheritance is if you have already done some code.

17:43

if you have already created a class.

17:45

Can I reuse it class without rewriting it again?

17:50

So one class derives from another.

17:53

The meaning of this line, one class derives from another means this cat class is derived from animal.

18:00

It means cat class is kind of a super set of the annual class.

18:03

All the functionality, the annual class contain, cat will contain those functionalities.

18:09

Cat may contain some extra functionalities also.

18:12

And we will see how to.

18:13

To edit, how to inherit it, what is the syntax, but here this is kind of a overview that what is the meaning of inheritance.

18:19

Inheritance simply says that, let's assume you already have a base class, okay?

18:24

This is called base class from where you're going to inherit.

18:27

So in this case, animal is a base class.

18:29

So if you have already created a base class, can you create a new class with the help of the base class?

18:36

This new class is called derived class.

18:38

Okay, so this cat class is derived from the base class whose name is animal.

18:43

So the first objective of this inheritance or the motivation for providing this feature is avoid duplication.

18:52

So you might, so you can convince yourself that there are many functionality common among animal and cat class, right?

19:00

So why should I rewrite it again?

19:02

If I have some functionality from which I can simply reuse the code which is written inside this animal class, I can use it.

19:10

So that is the one of the main motivation, avoid duplication.

19:13

The second thing is called modern real world relationship.

19:17

So as we said, this object-oriented programming is nothing but we are trying to make it more relevant or more easily relatable without real-world programming.

19:26

So here you can say, okay, theoretically, cat and animal, two different classes.

19:32

But if you think from the real-world point of view, cat is an animal, right?

19:37

So you can see there must be some property which are common in cat and any generic

19:43

animal, right? So that's why you are trying to create a relationship between it.

19:47

You are saying that, okay, cat is an animal. So you can assume cat is a derived class based on the

19:53

base class animal. Class can take attributes and matter from another class. Okay, so this is

20:02

the main line. Class can take attributes and matter from another class. The class which is taking

20:08

the attribute is called child or derived class. So in this case,

20:12

cat and dog are child or derived class, okay?

20:18

The animal, from where it is taking the functionality, attributes, method, they are called parent or base class.

20:26

Okay?

20:26

So we have two naming convention.

20:28

You can say parent or child or you can say base or derived.

20:33

So in this case, animal is a parent or base class and cat and dog are child or derived class.

20:42

Okay. So this is the syntax of the how you are going to inherit.

20:49

Okay.

20:50

So I hope there is no doubt in the first part, class animal.

20:54

So you are creating a class whose name is animal.

20:57

It has two methods.

20:59

The first method, what is the name of first method?

21:01

Can you please write what is the name of the first method?

21:12

Info is not the first function.

21:19

The underscore underscore unit underscore is the first function and that is called constructor of the class.

21:26

So you are defining constructor of the class anymore.

21:29

Then you are defining a new different function called info.

21:34

For any generic function, which is part of a matter, which is part of a class, the first argument is always

21:42

self. Okay. So now you can understand the annual class constructor simply says that,

21:47

okay, I'm going to take name as an input and then I'm going to assign self dot name equal

21:52

to name. So now you can understand self dot name is a instance variable. So each object

21:58

will have different name. So it's not a shared variable. This is an instance variable. And here

22:04

from the info function, what you are doing, you're simply printing animal name is self.

22:09

name. Now this is the interesting one, the next line. Class, dog, here we are providing

22:16

parenthesis and inside a parenthesis I am writing a name called animal. The meaning of this is

22:22

dog is a new class, okay? Dog is a new class, but it is taking attribute or it is inheriting

22:30

or we are deriving from the base class whose name is animal. So dog is the name of the new class.

22:38

annual is the name of the base class of parent class from where I am deriving.

22:43

So the syntax is simply you have to write class, the name of the class, and inside the parenthesis,

22:49

the name of the class from where you want to inherit.

22:52

Okay.

22:53

So now you have, you define a new function called sound.

22:58

Sound, it simply says that, okay, self.

23:01

not name and bark.

23:03

Okay, so inside this you are printing what is self. name?

23:06

So how dog will get self.

23:07

dot name is not able to find inside dog right so how dog will get self dot name yes from

23:22

parent class so as we said sorry dog is taking all the attributes from its

23:30

parent class the parent class is animal animal simply it says that okay it has

23:37

the constructor also and this is the info also it is not going to inherit the constructor

23:44

it is only going to inherit the variables and the name of the for the method inside the animal class okay

23:52

so it will simply say that okay name variable exists so it will have a different constructor

23:59

but it's going to inherit all the attributes and attributes are defined inside the constructor so you can

24:04

assume i'm just copying the constructors name

24:07

and I'm also copying the info or the function which is defined inside the parent class.

24:14

Okay, so we will see the example, then we can get some more clarity.

24:34

So now try to see this.

24:36

the first part is already described through the slide that we are creating a class whose name is animal we have the constructor we are assigning it then we have a info which is the name of the function which is the name of the method which is defined inside the parent class and inside dog you are creating a new function called sound and inside that you are simply saying bark okay as you can see I'm saying you are not copying the constructor but even

25:06

eventually you have to call this constructor right so that the name will be stored inside that so

25:12

the constructor is the base the construction of the base class is defined as it's going to take a parameter and the name of the parameter is name so here you can see i'm creating a object of a dog class and the parent constructors need a name so simply what i am doing inside dog i am giving the name of the dog and it's buddy okay so

25:36

so it simply says that okay i'm going to create a object of this class dog and i'm going to call this

25:43

constructor with the help of this name called buddy so whenever you create this object you are creating or

25:50

assigning self dot name equal to name and here name is nothing but buddy so d dot name will become

25:57

buddy okay then you are simply coiling d. info info is defined in the parent class and as i said i inherited it so i

26:06

and access okay so it will print annual name is buddy then we are saying d.s sound

26:12

d.s sound is that you have this function or this method is defined inside the class itself so it

26:19

will say okay you are defined inside the class i'm going to print self dot name is buddy and buddy box

26:26

so if you see the output

26:36

animal name buddy and buddy box okay no d is it okay so d is not object of both

26:47

the class d is an object of this class dog so you can assume so i'm just giving you some

26:54

hint you don't you don't have to think like this but for like visualization you can assume whenever

27:00

you are inheriting this the code is nothing but

27:06

now you have something like this and forget you have this annual one okay so the effect

27:15

is kind of this okay this is not the practical things you have to add some extra thing also but you

27:20

can assume if you are not inheriting then you have to write something like this okay but how

27:26

we solve this problem with the help of inherit tests so now you can also visualize the two

27:31

motivation which we solved what are the two motivation?

27:36

avoid duplication this is the first motivation right so if i'm not inheriting if i'll

27:42

do this thing i'll get the same functionality but i am copying this code here right so this is the code

27:48

duplication so that's why we are saying okay code duplication is not required we can inherit

27:53

and we can get the same functionality any doubt

28:06

so now we have one more problem so what problem will say so let's assume so see

28:14

example okay let's assume you want to access some variable which is defined in your parent class

28:21

so how can you access how can you get your parent information so for that we have a special

28:29

word called super okay so for example self self is you

28:36

what is the use of self can please write what is the use of self

28:44

yes current object access so with the help of self you can access the current object okay

28:53

so now you can access the current object let's assume you want to access your parent class you want to

29:00

access your parent class so how can you access for that you have a spatial variable called super so

29:06

with the help of super you can access your parent class used to call parent class method okay

29:13

so this is the use of super so whenever you want to access either a method or a variable you have to use super if

29:20

you want to access the method or variable of your parent class okay so for example in the parent class

29:27

the name of function is fun name then you have to use something like super dot fun name and with the help of this

29:33

you can call your method which is defined inside your parent class okay

29:41

child class uses the parent functionality and then add its own behavior right because now try to

29:46

understand if you are not adding your functionality then there's no need for creating a new

29:52

class right you can use that u.s class itself so if you see what i'm trying to say so let's assume

29:57

i'm not defining this function i'm not defining this okay so is there any use of creating this class

30:03

this class because it's only going to take functionality of the parent class you can always

30:07

get the functionality with the help of creating an object of the parent class so why you should create

30:12

two different classes right so the meaning of that line is simply saying that first you are going to

30:18

define the or we are going to inherit the functionality provided by the parent class and then you can

30:25

add your functionality okay so just like self means whenever you call this super

30:33

so now you can see self is a variable but super is a function method so wherever you have

30:39

a function or a method it returns something so you can assume it's returned a proxy object of your

30:45

parent class so there was a typo so this is class c l n double s okay so it's return a proxy

30:51

object which you can assume that okay with the help of this super i'm creating an temporary object or

30:58

proxy object of my parent class and if you are able to create that object

31:03

with the help of that object you can easily access the functionality of your parent class so this is

31:08

the way we try to access okay mostly it is used during the inheritance phase sorry in the

31:16

constructor phase so whenever you are constructing because whenever you are constructing you have to

31:20

set the variables value of your base class also or the parent class also so during that time

31:27

it is used so we'll see with the help of example so for example um

31:33

okay so let's assume this is the scenario okay in the base class you have two attributes

31:39

a and b and in the derived class you have attributes c and d and the role of constructor is to

31:47

initialize the value of a b c and d so how we are going to slice it for that you have to write

31:53

the constructor as we are writing the constructor in the derived class

31:59

accessing or modifying the value of c and d is not a problematic

32:03

you can easily assign self dot c equal to the value which you want to give self dot d

32:08

equal to the value which you want to give but if you have to set value of a and b in that case

32:14

you have to call the constructor of your parent and how can you call with the help of our

32:19

super function okay so let's see the example it will give you the clear thing

32:33

okay so first try to see this okay let's assume what you are doing you are creating

32:46

a parent class inside a parent class you have this so function okay with the help of

32:53

so function you are simply printing this is the parent class method it is not taking any

32:58

argument and in the child class you are inherent

33:03

the parent class okay in the parent class we have to function so and now you are

33:09

defining a new function called so one inside so one let's assume you want to print or you want to call

33:17

this so how can you call it you can simply call it with the help of super dot so if you are calling

33:25

super dot so then it is understanding okay i have to call my parent miss this so function is defined

33:33

inside my parent class and i have to access it and then i have to call this or print

33:39

this one okay so the output of this will be so you created an object of child class so you are creating

33:45

an object of this class okay and then you are calling so one function so one method from object

33:52

so one simply says that okay you have to first call super dot so

34:03

super dot so means this so is defined in a parent class so i'm printing this this is

34:07

the parent class method okay this functionality of this line is done because the use of this line is to

34:13

only call the parent the only call to this function which is defined inside the parent class

34:20

after that you are printing this is the child class method so with the help of this what will

34:25

be the output first we'll print this one then we'll print the second line

34:33

this is the parent class method and this is the child class method so whenever

34:43

whenever you have to call a method which is defined in your parent class you have to use the

34:51

super function first because with the help of super function you are creating kind of a proxy object

34:59

of your parent class and with the help of that proxy object

35:03

you are simply calling this function so okay so now you are able to understand what is

35:12

inheritance you have some base class whenever you are creating a new class you want to use the functionality

35:18

already provided in the base class and you can inherit it how you can inherit it you have to write the

35:24

name of the base class inside the parenthesis and rest all are exactly same so now there are different

35:30

types of inheritance okay so the different types of inheritance is the first one which

35:38

we are able to understand what is the meaning of this b is a base class sorry b is a derived class and

35:45

it is inheriting from a so a is a parent class and b is a derived class okay so this type of

35:54

inheritance means we already seen the example of this this type of inheritance called single inheritance

36:00

okay now we have a different type of inheritance called multiple inheritance

36:07

you can see why this is called multiple inheritance because here you have a derived class c

36:14

and this is taking attributes from two base classes okay or multiple base classes so here it's

36:21

not we are not saying that you can inherit from only two you can inherit from

36:25

an number of classes okay that's why we are calling it multiple inheritance okay

36:30

So let's see the syntax of this.

36:42

So let's assume you have the first base class called mother name and inside that you are defining

36:48

mother equal to print self dot mother name okay.

36:51

Now you have another class called father class in which you are defining the father name and

36:57

with the help of this father function you are simply printing the name of it.

37:00

the father okay now you have a derived class so please note that at line number

37:07

nine and line number two we are simply defining the class we are not inheriting anything right

37:12

because inside we are not using any parenthesis so these are the normal class definitions

37:18

now you have a new class called son inside the sun class what you are doing you are inheriting from two different classes

37:30

and the name of the first class is mother, the name of the second class is father.

37:34

So in the previous example we are inheriting only from the first class, right?

37:38

It means only from one class, but here you are inheriting from multiple classes.

37:43

So that's why you are giving the name of the class from where you are inheriting.

37:46

So here you are inheriting from two classes.

37:48

So that's why you are writing mother and father.

37:51

Okay.

37:52

And inside this derived class, what you are doing?

37:57

You are printing father name is nothing but.

38:00

self dot father name, mother name is nothing but self dot mother name.

38:04

You are creating an object of this son class.

38:08

Now in the son class you are setting s1 dot father name equal to Ram,

38:13

s1 dot mother name equal to seta.

38:16

So what is the meaning of this? Father name and mother name are the attributes.

38:21

These attributes are taken from the base class or the parent class.

38:25

This father name is defined inside the father's class.

38:28

mother name is defined inside the mother class, okay?

38:32

So we are initializing these variables.

38:36

And then we are simply calling S1.

38:38

Parents.

38:40

Inside this S1.

38:41

What will happen?

38:43

You are calling this one son parent.

38:46

Inside that you are printing name of the father.

38:49

And as you have seen, you initial this with the help of Ram

38:52

and you'll slide this with the help of Sita.

38:54

So it will print father equal to Ram,

38:57

to RAM, but that is equal to SETA.

38:59

So there's no technicality, there's no in depth knowledge.

39:02

So simply it is saying that, just like the previous case, you used only one class inside

39:07

the parenthesis.

39:08

Now you can use multiple class name inside the parenthesis and this is called multiple inheritance

39:15

because you are inheriting from the multiple classes.

39:18

If you see the output here,

39:22

father is RAM, whether is Zeta.

39:26

that is Zeta, okay?

39:44

So this is the third level of inheritance called multi-level inheritance.

39:49

The meaning of this multi-level inheritance is

39:51

now you are inheriting from only one class at a time, but

39:56

But you are creating a chain.

39:58

So you can see, A is a base class.

40:03

I created a new derived class called B,

40:06

which is inheriting property from class A.

40:10

Then again, you are creating a new class derived class C,

40:14

which is inheriting from B.

40:16

So you can convince yourself,

40:19

C is taking attributes from B, but B is already taking attributes from A.

40:26

So here also you are kind of inheriting from two different classes, but not at the same time,

40:31

you are kind of creating a chain.

40:34

So there's a difference between multiple and multi-level.

40:38

So in multiple, you are inheriting at the same level, right?

40:41

So A means there's no relation between A and B.

40:44

A and B are totally different classes, okay?

40:47

There's no similarity, commonality between A and class A and class B.

40:52

You are inheriting from class A and B at the same time.

40:55

this is called multiple inheritance.

40:58

Here, you are not doing multiple inheritors.

41:01

You are inheriting from one class at a time,

41:04

but step by step.

41:06

So first you created class B, which is inheriting from A,

41:10

then you created class C, which is inheriting for class B.

41:15

So it's totally depend on the use case,

41:19

what type of inheritance you have to use.

41:21

So there is no theoretical rule.

41:23

It's totally based on your intuition, your

41:25

implementation, that what type of implementation or what type of inheritors you want to use.

41:30

So the syntax of this will be very simple.

41:37

Okay. So, yeah, the multi-level is pretty easy one.

41:42

So what you are doing, you have a grandfather class. This is called the base class.

41:48

So just like in this picture, A, you can assume this is the grandfather class.

41:53

So Cuxi, please write what you have doubted multiple inheritance.

41:59

It's not like, please, so the example, this already we have shown, right?

42:02

You can see the video also because we are going very slow.

42:07

So in the grandfather class, what you are doing, we are simply defining a constructor.

42:13

The constructor is underscore underscore in it.

42:16

Here you are taking one argument only because self is by default passed.

42:21

So you are passing only.

42:23

one argument to this constructor and with the help of that constructor, what you are doing?

42:27

You are utilizing the value of grandfather with the parameter which is coming inside this.

42:34

Okay. Then what is our task? You want to create a new class B, which is deriving from A.

42:43

So here what you are creating, kind of an individual class. You are creating class father,

42:48

which is inheriting grandfather. Okay. When you are you are inheriting this

42:53

grandfather what you are doing self dot father name equal to father because now

43:00

it's take two argument one argument is father name other argument is grandfather name so what you are

43:07

doing self dot father name equal to father name unislize it now you have to pass this grandfather

43:13

name to the parent class or the derived class so what you can say so there are two way one with the

43:20

help of super you can do because it is inheriting from there

43:23

but there's one tricky thing left in the super that's why i'm not using super here in the next

43:27

slide or once we read about all the types of inheritance we will see a problem then we will understand

43:33

what is the main use of super then we will see how can we use super to do this also but here you can

43:38

assume grant because you know what is the name of the parent class so you are what you are doing

43:43

simply with the help of grandfather you are calling this underscore underscore in it underscore underscore

43:49

so you are calling this constructor manually for this parent class okay and then what you are passing

43:56

self-hand grandfather name and this will in slides the line number four okay then in the sun class so

44:06

we are able to do we are able to create this relationship right a and b we are able to we are able to

44:14

create a class b which is deriving from class a okay

44:19

now we are creating a next class c which is going to derive from b so now we are

44:27

creating a class son which is going to inherit from father so now if you see the relation son

44:35

is inheriting from father father is inheriting from grandfather so you have chain-like relationship

44:41

okay here in the constructor you are defining you are taking three arguments first argument is

44:48

son name second argument is father name third argument is grandfather name why i'm

44:53

taking three arguments because i know that i'm inheriting from the father

44:59

father takes two arguments so at least i need two arguments because if i am i don't have two arguments

45:05

what i'm going to pass to my parent constructor okay the third is the name or the initialization which

45:11

is done inside this class so you are you are doing self dot sun name equal to sun name and you are passing

45:17

rest these two arguments to your parent constructor so how it will work it will

45:24

simply assign self dot name self dot name equal to sunname line verse 16 simply says that

45:31

self dot sun name equal to son name okay here we are doing father dot in it so what i am

45:43

trying to do i'm trying to call the constructor of father

45:47

so in both cases we are using constructor so that in both cases we are using a

45:54

constructor line number 11 also we are using constructor line number 18 also we are using the parent

45:59

constructor so here we are calling or initializing our father constructor right so it this

46:05

constructor requires two arguments father name and grandfather name that's why i'm passing

46:10

self father name grand father name so it will come here it will initialize self dot father name equal to

46:17

father and then it will call grandfather dot in it so you are going to call your

46:24

grandfather constructor so if you see line by 26 i'm not creating object for father and grandfather

46:31

with the help of son only i am initializing the content of father name and grandfather

46:40

name so how's going to work you are passing three argument a b c son name will be a father name

46:47

will be b and grandfather name will be c so here self dot sun name will become

46:53

a now you are passing b and c to the parent constructor what is parent here father so now you have father

47:01

name equal to b grandfather name equal to c self dot father name will become b and grandfather

47:08

dot constructor means we are simply calling the constructor of its parent and we are passing c as a

47:15

parameter over there and then we are in

47:17

it so if you see the output of this

47:21

it so if you see the output of this

47:47

so siddhar if you notice here mother name and father name are class variable they are

48:01

not instance variable right they are not defined inside the constructor so that's why you

48:06

can access it directly also if it is inside the constructor if you're insizing it then you can use

48:12

the same thing if i'm achieving some goal with method this or i'm the

48:17

achieving goal with the method this it i'm not saying you can't achieve the same goal

48:21

with some other method also we can't enumerate each and every method right so you can achieve this with

48:27

the help of other method also but first you have to see this is the class variable and you

48:32

can easily access it so that's why you did it okay okay okay now this is

48:47

Again, just for the naming convention, if someone asked, this is called hierarchical inheritance.

48:53

No specialty, it is simply saying that, okay, B is inheriting from A, C is inheriting from A, D is inheriting from A.

49:02

So kind of B, C, D are at the same hierarchy, right? There's no relation between B, C and D, but all are

49:09

inheriting from A. So somehow you can say this is the hierarchical means whenever you have to create some hierarchy kind of thing, then you can use this.

49:17

kind of construct there okay so you can see you have a base class called parent and you have two child classes

49:35

child one and child two both are inheriting from parent this is inheriting from parent this is also

49:41

inheriting from parent here you are defining function two here you are defining function three

49:47

so everyone please write what will be the output in this case because this is just a naming

49:51

convention at hierarchical already you have all the ingredients you know which which is the parent

49:57

which is the child which how we are creating the object which function we are calling so what will

50:02

be the output in this case please take some time and write

50:17

Thank you.

50:47

child one parent class yes so what we are doing we are we are creating two objects the first

50:53

object is belonging to child one class the second object belonging to child two class okay then you are

51:00

calling object one object one is nothing but an object of child one class and then you are calling

51:05

function one so in child one function one corresponds to the this function is in parent class then

51:13

we are printing object one function two this function is a

51:17

child one then again you are calling object to function one it will call the parent class and then

51:24

function three this is child one so it will print parent child one parent child two

51:36

parent child one parent child two

51:47

Okay. Now we have an interesting case. Let's assume you want to change the definition of the function which you inherited. So just try to see what we are doing. You have an annual base class. Okay. In this base class, we have two functions. First function is move. Second function is eat. In the derived class dog, again we have two functions.

52:17

move and bark.

52:21

Let's assume you want to change the definition of move because you are inheriting it, right?

52:29

So if you see in the dog class, you will see, let's assume this move is not there.

52:36

First of all, let's assume this move is not there.

52:39

Then in dog class, you will see technically three functions.

52:43

First function will be this move, second function will be eight.

52:46

will be eight third will be bark right if this move was not there but now i want to modify the definition of move because already i received move from a parent class but i'm not happy with the definition provided in the parent class are you able to understand what is the scenario you are inheriting a function from a parent class the name is already there the move name is already there but now you want to change the

53:16

of that method okay you have you inherited a function but now you want to change the definition of the function which you inherited

53:28

this technique called method over riding so I have a method which I inherited from my parent but now I'm overriding it I'm simply saying that okay I want to remove those definitions or I want to add upend some extra definition inside

53:46

this technique called method over riding okay provide a specific implementation of a method that is already provided by one of its parent class this is called method over riding what it says that provide a specific implementation so here in case of dog I want a different implementation of move I'm not happy with the definition provided by an annual class of move function okay so

54:16

So this thing called method over writing.

54:19

How can we do that?

54:26

Okay.

54:30

Now try to see this.

54:32

So we are only writing the code which is important to show the concept, okay?

54:36

You have a parent class.

54:39

Inside the parent class, you have a constructor.

54:41

You are simply writing self dot value equal to inside parent,

54:45

inside parent, okay? So this is the constructor of the parent class. Inside the parent class, you have a function called so inside that you are simply printing what is the value. So whatever you in slides from the constructor, you are simply printing it. Okay? Now let's assume you want to do something else. What you want to do? You have the, you created a class called child, okay? Childs say,

55:15

that okay i'm going to inherit the functionality of parent so it inherited this so function now what i'm doing i'm creating my

55:25

new constructor for this child class the constructor whenever you are creating this constructor you are calling the

55:32

constructor of the parent also okay so here because maybe i have to install some thing for my parent right because i want to inside self-flot value so i

55:45

and is called the parent constructor how can i call the parent

55:48

constructor with the help of super okay super will give you proxy object of your parent and with the

55:54

help of that you are calling the constructor okay and inside it again you are

55:58

initializing self-flot value so i'm not saying you can do or you can't do there are

56:03

totally different thing it simply says that i called my constructor parent constructor and then i'm

56:09

doing something else okay you can write value you can write value and anything you can

56:15

right okay so it's not like that now you are giving a new definition of so so now you can

56:23

say okay so what you are saying the previous definition of so was only print self dot value the

56:37

self dot value was nothing what inside parent so it is printing it but now here i'm showing so

56:45

print high plus self dot value okay so what we are doing object one i'm creating an

56:53

object of my parent class then i created object of my child class then i'm saying object one dot so

57:04

do we need to call parent constructor it's not mandatory but it's generally recommended you should

57:10

call your parent constructor okay because there might be something which you need to

57:15

initialized so always it's good to initial to call your parent constructor but it is not

57:21

mandatory even if you are not calling it that is fine but if your parent constructor need some

57:27

argument then it is kind of must otherwise those variable are not initialized okay so totally

57:33

depends on the huge cases so here object 1.so object 1 is a object of class parent so it is going

57:42

to print this one right self dot value

57:45

Now I'm just calling object 2.so.

57:48

So what will be the output of this object 2.so?

57:53

It is not going to call its parent right because in my child I modified the definition of

57:59

so function. So now you can see this show is even if inside my parent, it will going to call the

58:08

child one okay the function which I define inside my current class. It's going to access

58:15

this one okay and neha your answer isn't correct so here we are going to call

58:25

this so function and the self dot value will be self dot value inside child so the output will

58:45

So first we are printing inside parent because I am calling the sole function of a parent object.

58:59

Then we are calling the sole function of the child class, then it is printing high inside child.

59:06

Okay?

59:08

So what we learned from this, even if you are inheriting a function or a method,

59:15

from your parent, you have full freedom to change the definition of that function.

59:21

You are only going to call the definition which is frauded inside the child class.

59:26

But if you have, so let's assume, I'm not writing this definition.

59:33

Then what will be output?

59:38

Will it compile? What will be the output?

59:45

Inside parent, inside child. So even if you are not providing, then the Python will say, okay, you haven't defined this function. So I have to check inside my parent. And inside parent, you have this definition. So this object. So is going to bind with this definition, which is provided it.

1:0:15

number 8 and it will simply print self dot value.

1:0:19

So if you want to change the definition, you can change the definition.

1:0:25

If you don't want to change the definition, by default, it will use the definition of your parent.

1:0:31

Okay?

1:0:33

This is called method over riding.

1:0:38

So now there's a thing called method over riding.

1:0:41

So now there's a thing called method

1:0:45

solution order. So now try to visualize this diagram. What is the meaning of this?

1:0:51

A is a base class. B is a derived class and it is inheriting attributes from A. Okay?

1:1:02

C is also a derived class which is taking attribute from A. So kind of B is inheriting from A, C is inheriting from A.

1:1:15

is inheriting from both B and C because error is going in that direction.

1:1:20

Now take a scenario. Let's assume Fu function is defined in A also, it is defined in B also.

1:1:28

It is defined in C also. The thing which I'm trying to say, let's assume Fu function is defined in A, B, and C.

1:1:36

And this is totally possible, right? Because A function may contain the first definition of Fu. B class will say, okay, I want to over

1:1:45

the definition of Fu, so it is again defining Fu.

1:1:48

C class again thinking that okay, the definition of Fu is not good, I'm going to override it.

1:1:54

Now I'm inheriting, now I'm creating a Class D, which is inheriting from Class B and Class C.

1:2:03

Now, if you are calling Fu Function from the object created from D, which Fu should be called?

1:2:11

Is the question clear?

1:2:12

If I am calling a foo function from this D object of class D, now you have three different version of foe, right?

1:2:24

One foe is in A, one foe is inside B and one foe is inside C. Which foe should be called?

1:2:31

For solving this problem, the topic called method resolution order.

1:2:39

Matter resolution order simply saying that whenever the problem, the topic called method resolution order,

1:2:42

you have multiple definitions of a method.

1:2:47

Which methods should I choose? In which order I'm going to search?

1:2:52

So simply you can say, okay, for solving this problem, we have to find answer of a question.

1:2:57

And the question is, whenever I am searching this full function,

1:3:04

whenever you're calling a function, means you have to search the definition of that

1:3:08

full function, because if you are able to get the definition of full function,

1:3:12

you can simply call it, you will get the answer.

1:3:16

Whenever you are inside D, you created an object of D, now you have to find where this full function is defined.

1:3:25

The first rule says that, so, okay, so this topic called order in which Python searches for a method in a class and its parent class, this topic called method resolution, order, okay?

1:3:38

When this occurs, when the same method exists in most,

1:3:42

so then one class in an inheritance change so now you can clearly see this is the scenario

1:3:48

who is defined in b also who is defined in c also who is defined in a also so we are able to hit

1:3:54

the second case also now what is the method result order followed by python it will simply say

1:4:02

first check whether the definition of the function is provided in that class or not so you

1:4:08

created an object of d right so first python will check

1:4:12

Where does this full function?

1:4:26

So Rabi, please ask these types of questions to your industry partner, okay?

1:4:32

Because they designed the slavers, you can ask this question to them.

1:4:37

So here it will simply say,

1:4:39

is fu function is defined inside d or not if fu function is defined inside d then i'm going to

1:4:50

choose that one okay that is the first rule first check the class for which you created the object

1:4:59

if there's a so if i create a definition of foe here i'm not going to choose that definition

1:5:05

troided in b i'm not going to choose definition troided in c i'm not going to choose definition

1:5:08

in a i'm only going to choose definition troided in d okay this is the first rule

1:5:17

now you have the diamond problem it simply says that okay let's assume this the scenario

1:5:25

d is inheriting from b and c this is the case right so if you want to see the syntax this is kind of

1:5:31

thing d is inheriting from b and c b is inheriting from a c is inheriting from a c is inheriting from a

1:5:38

this is the actual thing in which order python is going to search this is the defined

1:5:45

order why this is the order let's try to visualize it what is first rule first check in the class

1:5:52

corresponding to object okay you are trying to search foe from object of class d okay so that's why

1:6:00

i'm going to first check in d okay then it will simply say what is my inheritance order here i have written

1:6:08

b comma c okay inheritance order simply says that i'm inheriting from b then i'm inheriting from

1:6:15

c that's why it is searching from b first then it is searching in c then there might be

1:6:22

possibility that who function is not defined in b also it is not defined in c also okay then i'll

1:6:28

check who are the parent of b or c i will see okay a is parent of b then i'm going to say okay even if you're

1:6:37

not able to find definition of foe in b and c then you should check the definition of foe

1:6:42

inside a okay and even if you are not able to find there's some syntax error in your program

1:6:48

because this is the inheritance chain you should find the definition of who inside it otherwise there's

1:6:54

a syntax error so in sort what is the order in which python is going to search first it is going

1:7:00

to search inside the actual class for which you are creating the object

1:7:07

okay so first you are searching from d you are searching inside d okay then you are

1:7:13

saying inheritance order what is the inheritance order first first you are searching inside b

1:7:20

then you are searching inside c even if you're not so if you are able to find inside b

1:7:26

then you are not going to search further because your task is to not enumerate all the foes

1:7:31

your task is to get what is the definition of foo so simply what you are saying if i'm able to find

1:7:36

i'm able to find definition in b printed call that function if i'm not able to find

1:7:42

inside b then i have to check inside c if i'm able to find inside c good otherwise then i have to see

1:7:50

the instruction or uh inheritance order of this b and c also so b is inheriting from a then i'm

1:7:57

going to search inside a so that is the order so let's see the example which will help us to understand

1:8:06

okay okay you are printing you are printing printing

1:8:36

simply saying i'm printing in class a okay in class b again you are inheriting from

1:8:44

a so you're inheriting from a means you have a definition of fun but now you over

1:8:51

write it right so you have deaf fun means you override the previous definition of fun now you are

1:8:57

creating an object of b right if you want to create an object of class b and then i'm going to call

1:9:05

a dot fun what will be the output based on the order which we studied what will do the

1:9:10

output of line number 10 in class b why because the first rule says that first you have to check

1:9:25

inside the class if you have a definition simply use that definition so you created this object

1:9:32

from class b contains this function called fun that's why i'm printing this one okay

1:9:39

now try to see the second example you have class a which defined fun you have a class b which is

1:9:47

inheriting from a which also defines fun okay again you have a class c which is inheriting from

1:9:53

a which is defining fun again we are defining fun in class d you have a other function called no

1:10:02

in no fun you are simply printing something so inheritance order is clear

1:10:09

base class is a b and c are inheriting from a d is inheriting from b and c okay

1:10:18

okay if you are creating an object of class d a equal to d now you are calling a dot fun

1:10:32

which fun should we get what will be the print value so first it is going to check inside

1:10:42

d right inside d do we have definition of fun we don't have definition of fun right so okay

1:10:51

it will say okay i'm not able to find it now you have to search it in the next class what is the

1:10:58

next class next class is b in b in b

1:11:02

it is going to check okay do we have definition of fun it will say yes we have

1:11:06

definition of fun so i'm going to print in class b so let me first comment line about 30

1:11:11

we will see the output then we'll see what is line about 30

1:11:18

in class b in class b okay if i am writing like this then what will be what will be

1:11:32

what will be the output in this case so here still you will not able to find inside d so you will

1:11:43

search inside c okay in c you have the definition of one that's why you are you will print

1:11:51

in class c okay in class c if we don't have the definition then what will be the output

1:12:02

what will the output in this case so now first we will check in c the order is exactly

1:12:15

same i will check inside c but inside c i am not able to find the definition of fun so i have to

1:12:22

check inside b b is simply saying okay fun is there so print in class b if fun is not

1:12:31

is not in b also then what will be output in class a because i'm not able to find this

1:12:41

definition so i'm going to check in the parent function of or parent class of class c

1:12:48

parent of class c is class a and it has function if there's no definition in fun in class a also

1:12:56

then what will be the output

1:13:01

yes it will d has no attribute fun did you mean fun one so because now you don't have

1:13:15

the definition of fun so it will simply say okay there's some syntax error so you know

1:13:23

what means theoretically you can understand what is the method resolution order right now you have

1:13:29

full confidence over there but

1:13:31

let's assume you have a very big inheritance chain you are not able to check what is

1:13:38

inheritance order means you are not able to understand you are not able to draw so this function d.m.

1:13:45

this is means d is just in class mRO is called matter resolution order this is a special function

1:13:53

which is going to let you know what is the resolution order so if you see this is this will try the

1:13:58

a list of the resolution order

1:14:01

it is simply saying first check inside d then check inside b then check inside c then check

1:14:08

inside a and this is the last one this is not important we will see it later but now you can see

1:14:14

this is the execution order sorry search order first i'm going to check inside d then inside

1:14:20

b then inside c then inside a so this this is the mRO order okay if you want to see the mero order

1:14:28

you have to use this comma this function called m r row i think you have this

1:14:34

facility also underscore underscore m row this will also give you the same output but okay so now

1:14:43

again a small question what is difference between this line which i highlighted

1:14:49

and in this line what is difference between these two line

1:14:58

yes list and tappel so you have to take care about these things because this is list and

1:15:13

this is tappel okay so let's take a break of five minutes then we can start restart okay

1:15:28

I don't know

1:15:58

you know

1:16:28

Thank you.

1:16:58

Thank you.

1:17:28

Thank you.

1:17:58

Thank you.

1:18:28

Thank you.

1:18:58

Thank you.

1:19:28

Thank you.

1:19:58

Okay, welcome back.

1:20:05

So now let's try to find one more interesting case.

1:20:12

Let's assume A and B are base class and C is inheriting from both A and B.

1:20:21

Now the question is,

1:20:27

is, with the help of super, you can access your parent class, right? Super will give you a proxy object of your parent class.

1:20:36

Now, if you are going to say super, super will access A or super will access B?

1:20:44

Is the question clear?

1:20:57

So, till this point, we don't have clarity.

1:21:07

So again, it depends on the method resolution order.

1:21:11

So in which order it is resolute, resoluting the method.

1:21:15

And now we have clear picture of what is the method resolution order.

1:21:18

So we can understand, right?

1:21:20

So it's going to, depends on how I am writing the inheritance sentence, whether I'm inheriting

1:21:25

first from A or inheriting first from.

1:21:27

B. So it will use super to access the first inherited class. And but if you want to access the second one, how can you access it? So these types of question we have to answer. Is the problem statement clear? The first question which we are able to solve with the help of MRO. The first question is inside C, if I am calling super, will it access A or will it access B? We are 100% sure.

1:21:57

it will not access both, right?

1:21:59

It's not a random behavior that sometimes it is giving A or sometimes it is giving B.

1:22:03

It's a deterministic, correct answer that either it's going to access A or it is going to access B.

1:22:09

First question is which class it is going to access.

1:22:13

The second question is, even if I'm going to access the one of the class, how can I access the second class?

1:22:19

If you want to in a slice the constructor of the second class, how can you access?

1:22:26

So let's try to find.

1:22:27

answer of these questions. Okay?

1:22:57

have a class. So now you have multiple constructors. So now you have the first class called A. You are not inheriting anything. So this is the base class, right? Inside the base class, you are defining a constructor. And again, it's not taking any argument. So you are printing, insizing A. Okay? Then you have another base class B because we are not inheriting anything. So we are saying this is a base class B. Inside that, you are defining a or calling.

1:23:27

a defining a constructor, which is simply printing and slicing B.

1:23:33

Now you have a class C, which is deriving from both A and B.

1:23:39

So now this is a multi-label or multiple. Which type of inheritance is this?

1:23:50

Multiple or multi-level? Multiple. Because at the same time,

1:23:57

we are inheriting from two different classes okay so this is the multiple inheritance now the question is

1:24:07

inside this unit function of the derived class i am free to write this code which is written

1:24:13

at line about 13 what this code says that super dot called the constructor so now we have to answer

1:24:20

it is going to call which class class a or class b so what will be the answer in this

1:24:27

this case. So we created a constructor C. So we created an object of class C and whenever we are creating by default

1:24:36

constructor will be called. So you don't have to do anything else. So what will be the output in this case?

1:24:57

first constructor A is called then constructor of C is called.

1:25:15

Why? Because first you are calling super dot in it. So you are sure somehow it is going to call the constructor of the parent. Then we are printing and slicing C.

1:25:27

Now simply understand the matter resolution order.

1:25:31

Super dot init, you are sure you are going to not find inside the current class, right, because I'm calling the parent class.

1:25:39

First, I should search inside A. Inside A, we have definition of init, so we are using it.

1:25:49

If I would have written something like this, then what will be the answer?

1:25:56

in slicing B and C because just like the MRO, it will call the B first and then it's going to access it.

1:26:07

Okay. Now the question is, if you want to call the constructor of both of the classes, then how you are going to do?

1:26:16

Okay? The question is, if you want to call the constructor of both the classes, how you are going to do?

1:26:24

Simple.

1:26:25

just use super and the MRO thing.

1:26:28

The best answer is in each constructor, just call super dot innate.

1:26:35

Okay?

1:26:36

What is the meaning of this?

1:26:39

The meaning of this is whenever I'm creating a constructor,

1:26:42

whenever I'm creating an object of C,

1:26:45

I'm calling the constructor.

1:26:47

Inside the constructor, I'm going to call super dot innate.

1:26:52

As we know,

1:26:55

the order is first we are checking inside B.

1:26:58

So it will execute this constructor.

1:27:01

I don't think there should be any doubt in this.

1:27:04

It should call this constructor.

1:27:06

Inside this constructor, we have, we called super once again.

1:27:11

Now we know the MRO order.

1:27:13

What is the MRO order?

1:27:15

First, it will check in C, then it is B, then inside A.

1:27:18

So this is the total MRO order.

1:27:20

So now if you are calling this super,

1:27:23

then after B, after B, I will check in C,

1:27:25

I'm going to search inside A.

1:27:27

So it will call the constructor of class A.

1:27:31

Here we have super dot in it.

1:27:34

You can ignore that at the end, you have nothing to search,

1:27:37

so it is not going to print anything.

1:27:39

So you can assume it has a special privilege

1:27:42

that even that function is not defined,

1:27:44

it will not throw the error.

1:27:45

Because in the previous case, we are seeing,

1:27:47

right, if a attribute is not defined,

1:27:48

it is showing the error.

1:27:50

So you can assume any t is a special function,

1:27:53

that even if it is not defined, it will not

1:27:55

through the error. So you will not print anything here because there's nothing after class A, right?

1:28:03

The MRO order is nothing but our MRO order was C, B, A, right?

1:28:12

First you called this function, this is going to call this function B.

1:28:18

Again, we have super then it is going to call it A.

1:28:21

Then after calling this, we are printing inslising A, then it will print in a.

1:28:25

Slicing B, then to print, in Slicing C.

1:28:34

In Sizing A, in Slicing B, in Slicing C.

1:28:41

Any doubt in this?

1:28:43

Because this is an important case, because sometimes you are inheriting from multiple classes,

1:28:49

and you have to call the constructor of all the base class.

1:28:52

So how you are going to do?

1:28:54

So thirdly, you can do easily by writing super dot init in each and every class.

1:28:59

But you should also know why you are doing this.

1:29:02

So now you can understand why you are doing this?

1:29:09

Will it call C's init by super?

1:29:12

No.

1:29:13

After A, there's nothing, right?

1:29:14

So why it is called, with the help of super, you are trying to find the base class.

1:29:21

So here, C is not base class of A.

1:29:24

So it will not so you can assume, if you're not able to find something, it will simply return empty.

1:29:30

It will not throw error.

1:29:32

It will simply return.

1:29:33

Okay.

1:29:34

So now we are able to solve that problem also because this is one of the important problem because

1:29:40

multiple inheritance is very common.

1:29:44

And whenever you are doing multiple inheritance, you may want to call constructor of each and every class.

1:29:51

So now you know how to achieve that.

1:29:54

functionality, okay?

1:29:57

Now there's one more important topic called method overloading.

1:30:02

Method overloading simply says that, okay?

1:30:05

So first you have to understand what's the difference between function, method overloading and method overriding.

1:30:12

In method overriding, we are changing the definition of a method.

1:30:19

But the signature of method was exactly same.

1:30:23

What is the meaning of signature?

1:30:24

the meaning of signature is first, the name of the function, second, parameters.

1:30:32

What are the parameters?

1:30:33

The number of parameters should be same.

1:30:35

Type of parameters should be same.

1:30:38

If this is the case that the function signature is exactly same and you are changing the definition,

1:30:44

that is called method over riding.

1:30:47

Because in the previous example, if you remember, the shown function, the name is exactly same.

1:30:53

Both were not taking.

1:30:54

any argument what it means that we are using function overriding in function

1:31:01

or method overloading multiple methods with the same name but different

1:31:07

parameter list so this is a difference between overloading and overriding if

1:31:13

parameter list is different then it is overloading if parameter list is same

1:31:19

then it is overriding okay so for example see this one

1:31:24

foe a comma b foe a comma b comma c now these two definitions are inside the same class even i'm not saying that you have to inherit inside the same class you can define this one

1:31:40

how these two foo foes are different first foo says that if you called it with the help of two arguments if you called it with the help of two arguments then this function should be called if you are called

1:31:54

calling a function with three arguments then this function should be called okay so

1:32:00

thirdly is there any doubt between function overloading and overriding if parameters exactly same

1:32:06

then it is called function overriding if parameters are different then it's called function overloading

1:32:18

one weird thing is python doesn't allow by default function overloading means like

1:32:24

like for example under programming language java python they provide the nice neat and clean way for

1:32:31

method over loading or function overloading but here here inside python you can achieve the same goal

1:32:45

but with some other hacky solution so we will see how to do method over loading inside python okay

1:32:54

Okay.

1:33:23

Okay.

1:33:24

try to see this program okay so i think this is covered in the next slide also

1:33:33

okay so for achieving this python provide two different solution one solution is called default arguments

1:33:41

so if you see what is the default arguments that if you can call this full function with the help of

1:33:49

two parameters also three parameter also if i in a slice see

1:33:54

to some default value right so with the same function you can call it with two different

1:33:59

signature either by providing two parameters or by providing three parameters so that is the

1:34:04

default argument thing which we already discussed here we will understand kw arcs or keyword waste

1:34:11

arguments this is just a super set of arcs here we don't provide keywords even without that it is fine so we'll

1:34:17

see the example of how with the help of kw arcs we are able to

1:34:24

achieve function over loading okay just try to see this one you have a class in this class

1:34:35

you have a constructor underscore underscore in it and you have a self you have a variable a and you have a

1:34:43

spatial kw arcs kw arc simply says that okay i'm let's assume you are calling this

1:34:50

init function with n number of argument okay okay if you are you are

1:34:54

you are calling the unit constructor with n number of argument it will simply say the first

1:34:59

argument is matching with a and remaining n minus one arguments will be stored inside kw r okay so now

1:35:07

what you are trying to say the first argument is stored inside a and all remaining argument will

1:35:13

be stored inside kwr similarly here the first argument will be stored inside b and all remaining argument

1:35:21

will be stored inside kw us so now what how can you use it you know inside a function

1:35:28

that it takes two arguments three arguments so you can define those arguments here and you can

1:35:34

store remaining one in the kw rs and feel free to reject it because i don't want to use it one

1:35:42

okay so we will see how we are achieving that goal okay what we are doing we have a class c

1:35:49

c is inheriting from a and b we have a class c which is inheriting from a and b

1:36:02

it simply says that i'm inheriting from this one also inheriting from this one also you are

1:36:10

creating an object of class c which is taking three arguments 10 20 30 okay now

1:36:19

what you are doing you are simply saying okay call this constructor a b c you have three

1:36:28

arguments then a will contain 10 b will contain 20 c will contain 30 okay now you are calling

1:36:35

the constructor or this super you are calling the parent constructor with the help of this super and underscore

1:36:46

underscore in it this is called keyword based parameter so

1:36:49

so here what you are trying to say just write a inside a and b inside b so here

1:36:56

you know these are a and b are parameters so i'm passing a equal to a and b equal to b this will

1:37:03

call to a or b which constructor will be called with the help of line number 17 it will search inside a so

1:37:16

this constructor will be called okay now just see you call this constructor with two arguments

1:37:23

a and b right but here this constructor take two arguments the first argument is easy to understand

1:37:31

a second argument is kind of weird right because we don't know so what i said kw arg

1:37:39

simply you can assume kw arg is a garbage collector kind of thing so whatever you want to dump dump

1:37:45

dump inside this here you send two arguments a and b it will say okay i'm able to

1:37:52

understand you send a for me but i don't know what you send b because i don't know what is the use of

1:37:59

it so i'm just capturing all those things which you passed here okay that thing is stored inside kw

1:38:06

args okay but you are the programmer you know what is its future use you send it so that

1:38:15

future i am going to send this parameter to the other constructor also okay so here you are calling

1:38:22

this super so at line number three the call whenever you are using this call super it will going to call

1:38:30

call class b's constructor because the m r was c a b so from here you are going to call this one okay

1:38:40

inside that constructor you are sending kw rs why you are sending kw rs why you are sending k

1:38:45

because you know that okay i know how to use a i have used of this a but i don't know

1:38:54

what to do with the remaining ones maybe my parent knows it that's why i'm sending all those

1:39:00

things to the parent or the remaining one okay so kwarks still hold all the information

1:39:07

so what are the information inside kwarks it will simply stored that you have passed a variable

1:39:13

a value b which is going to bind with variable b okay whenever you called it then

1:39:20

say oh okay self comma b now i got it that b is there so it will bind this b with this v and now

1:39:30

you have nothing left in kw args so now again you are going to call this super this super will call

1:39:38

but it will return empty because there's nothing after b inside the mRO right you have

1:39:43

have c you have a you have b so this is kind of a just a dummy call so that you can execute

1:39:50

it and the k w arcs contains nothing because you consumed all those arguments so you can see how you

1:39:57

have a vc three arguments here and you are able to pass partial information to the parent with the

1:40:04

help of kw args so k w x you are simply kind of

1:40:13

storing whatever the things you haven't used till this point okay you passed a comma b

1:40:21

here you consumed a remaining partage is stored inside kw arg so here it is equivalent to i'm

1:40:27

super underscore underscore in it it will say b equal to b equal to b b equal to b

1:40:32

equal to b because k warks stores this information that information passed here so i know okay

1:40:40

b contains the value b and i'm able to do it

1:40:43

So if you run this program and print it, then you will get object.a value, object dot b, object dot B value, object dot C value is nothing but

1:40:54

so a third from last five net I think I'm just telling what is kW arcs and still you're writing what is

1:41:00

KWRs. So I am saying kwR is nothing but you are using all the things which is still unused. So you call this

1:41:08

function right in it. So Arthur please answer which function you are going to

1:41:13

to call from line number 17.

1:41:17

Arthur, please, please write it.

1:41:27

Line number 17, which function will be called?

1:41:43

valid argument right a but here you are passing two arguments a and b now you are able to

1:41:50

consume a but the remaining part the leftover part all the leftover you can pass anything

1:41:57

over here n numbers of argument all those arguments will be stored inside kw rs so kw rs is

1:42:03

keyword waste arguments so this is kind of a way to store all those things inside the

1:42:09

the because you don't know how to use it but

1:42:13

there are some other function where you have to pass this argument they might know how

1:42:18

to use door argument okay so that's why you are storing all those things and sending to the

1:42:24

super dot in it so you are calling now you are calling this b so this kwarks right now contains b

1:42:30

equal to b because you consumed a so the only are keyword uh keyword b is left over so now you are

1:42:37

passing b once you come at line number nine you'll understand okay now i know how to use b

1:42:43

also okay so now it will understand i'm able to use b so now there's nothing left inside kw r so that's why

1:42:50

we are generally using keyword based otherwise if you have written only a comma b then it will become

1:42:55

confusing that okay which is going to bind with this one so that's why we generally use keyword

1:42:59

base argument that whenever you see this name a then bind it with the actual a whenever you see b

1:43:06

bind it with the actual b so with the help of this you are able to pass any numbers of argument to the

1:43:13

function and you can try so for achieving this goal we have one other solution also

1:43:20

that typing what we said let's assume you have a function perform task okay so now try to understand

1:43:31

this code you have a class called pen this pen this pen has a function called use it is taking no argument

1:43:42

so in the previous case we are using with the help of arguments here we don't have any argument okay

1:43:48

now i'm simply returning return writing because the use of pen is writing so i'm simply returning

1:43:55

writing you have a class called eraser eraser says that use of erasure is erasing so you define

1:44:03

the function use and it is erasing okay you are now defining a function

1:44:10

what is function perform task and it's take tool as an argument

1:44:17

means it's just the argument you are capturing with the help of name called tool and now you are

1:44:23

calling print tool dot use so you are not calling erase dot use you are not calling pen dot use you are

1:44:28

simply saying that whatever comes to me i am going to call tool dot use now you are calling

1:44:35

this perform task okay you are calling same function right you are calling same function right you are calling

1:44:40

same function but based on what type you are calling based on which object you are passing

1:44:46

you are calling different function right so you have written only tool dot use but once you are passing pen

1:44:53

as an argument then tool will become pen and pen dot use will become writing okay if you are passing

1:45:01

eraser then tool dot use will become eraser dot use and it will print erasing so you have the same function

1:45:10

same body but you are able to call multiple or different function so this is

1:45:18

called duct typing and this is very common in python if you are managing a large project okay

1:45:28

writing erasing okay so what what we are trying to do you are calling the same function right

1:45:34

perform task but based on the object you are deciding

1:45:40

which use i am going to call okay okay

1:46:10

you know.

1:46:40

Thank you.

1:47:10

Thank you.

1:47:40

answer is incorrect please focus on constructor also

1:48:10

Thank you

1:48:40

Thank you.

1:49:10

Okay.

1:49:40

first you will create the object right at line number 23 you are creating an

1:49:46

object of class c3 whenever you are creating an object of class c3 whenever you are creating an object you will first check whether there's a constructor or not if there's a constructor or not if there's a constructor then you are going to execute that constructor and you are going to print whatever you are going to execute whatever written inside the constructor okay so here

1:50:04

constructor we have the constructor in c3 what it is saying hey my class i am initialized class

1:50:13

three okay then you are calling super dot in it this super dot in it is going to call the parent

1:50:21

constructor what is the who is the parent of c3 it is only one level of what you say this

1:50:30

inheritance c2 is you are inheriting c2 so now you are

1:50:34

going to call constructor of c2 then it is going to say hey my class i am in a sliced class 2 and then you are

1:50:42

going to call the constructor of the parent of c2 who is the parent of c2 c1 is the parent then you are

1:50:51

simply writing hey my class i am in sliced class 1 and now you are not calling anything so this is the

1:50:57

chain of constructor first you are printing 3 then you are printing 2 then you are printing 1 and it

1:51:04

out in this then you are calling this function called my class dot sub my class 10

1:51:18

what you are simply doing okay you are my class is an object of class c3 you are calling

1:51:25

sub my class so first you are going to check where is the definition of this function so you'll see okay

1:51:32

definition of this function is at line number 19 so i'm going to execute how i'm going to

1:51:38

execute first i have to pass this argument what is argument 10 here you don't have worry about self

1:51:44

because self is always a parameter in case of a class method so you are going to in slice b

1:51:51

equal to 10 then you will simply print printing from class c3 output and b will be equal to 10 then you are

1:52:00

calling parent class sub my class and you are passing b plus 1 here you will see okay

1:52:09

i have the definition then you'll print c2 and here you will print 11 then you'll call its parent

1:52:16

its parent is c1 here you'll print 12 so what you are what you are doing first you are printing the constructor

1:52:24

3 to 1 then you are printing printing the value from class 3

1:52:30

10 class 2 11 class 1 12 let's see the output

1:53:00

to check what is the definition of the constructor then you are going to execute that one so you

1:53:07

don't have to think that someone is going to call this in it because many strands were able to write it

1:53:13

the output of this but they are not able to write the output of line number 23 so whenever you are creating

1:53:20

an object constructor is by default called so constructor of this is this one so that's how you

1:53:25

printed three then you called constructor of the parent you printed this one then you called

1:53:30

it's parent then if you printed this one okay okay so now there's one more

1:53:45

interesting concept called operator overloading it simply says that okay we have a function

1:53:53

we can overload it operator is also just kind of an important thing right why should not you overload it

1:54:00

why should not you give a different meaning to an operator also so python says that yes you can do you can do operator overloading

1:54:09

the meaning of operator overloading is giving a totally different meaning of that operator so for example plus you'll simply say okay no no

1:54:18

no in my domain plus means subtraction plus mean multiplication okay so whatever definition you want to give you can give

1:54:25

with the help of this operator overloading okay

1:54:30

same operator to work in different way depending on data type so this is the use case so for

1:54:36

example plus operator in case of integer it's going to add in case of string it is going to append

1:54:44

technically both has the same meaning but you see the implementation wise it's totally different

1:54:49

you can add to integer in case of string adding with appending again multiplication if you have

1:54:56

integer then it will multiply will give you the answer of the

1:55:00

multiplication if it is a string then it is going to say i'm going to so for example high

1:55:05

into three means i'm going to repeat high three times so the same operator has totally different

1:55:11

meaning based on the what type of operator you are passing okay plus can add two number join strings

1:55:21

merge list so for operator overloading we need to understand magic function

1:55:30

so this is a link once i say are slides with you you can click on this you will get

1:55:35

the complete list of magic function here i am not enumerating every function but i'll give one or two

1:55:41

examples so that you can understand what is magic function and then you can do whatever you want

1:55:47

to do so magic function is nothing but a special method name for operators what you simply say

1:55:54

okay plus is an operator right plus is an operator but magic function says that okay i

1:56:05

can give an other name of plus also and what is the name the name is underscore underscore add

1:56:12

underscore underscore so there is it means there are two underscores it is not only one there are two

1:56:18

underscore just like in it right we have two underscore in it then again two underscore so here's

1:56:24

this plus and underscore underscore and underscore underscore underscore are exactly same exactly

1:56:29

equivalent similarly let's assume you have less than operator the name of the magic

1:56:36

function corresponding to this less than operator is underscore underscore underscore underscore underscore undertaker

1:56:40

okay so now you have to understand this one let's assume you are doing a plus b

1:56:49

i'm simply replacing a with object b with object too so let's assume you are doing

1:56:53

assume you are doing object one plus object two object one can be an integer object one can be a list

1:56:59

object one can be a string it can be anything so whenever we so for example you have a complex number right

1:57:06

so remember in the first class i gave it means whenever i did the introduction of object

1:57:10

of programming i ask you how can you add two complex number okay so now you can understand

1:57:17

you can create a class inside a class you will have two member variables real

1:57:23

and imaginary and then you can define a plus operator and the use of plus operator will be real

1:57:29

will be added with real imaginary will be added with imaginary okay so but before that you have to

1:57:35

understand how internally it works object one plus object two this is the normal syntax of right

1:57:41

plus because plus take two arguments so object one plus object two is nothing but this is the exact

1:57:48

meaning what it says i am going to call this underscore underscore

1:57:53

add function and this function is written inside the definition of this function must be

1:58:00

inside the class from which you created this object so it is nothing but as i said operator is

1:58:07

converted into the function name for calling a function you need an object right because that

1:58:13

must be defined inside a class and for accessing that function you need object so what you are

1:58:18

doing object one dot add this magic function and the

1:58:23

second argument you are passing like a argument to that function is this clear or any doubt

1:58:29

in the last line please let me know if you have any doubt in the last line

1:58:53

so object one plus object two is internally converted into object one is going to call

1:59:00

the magic for equivalent magic function and the in you will pass the second argument as an

1:59:06

argument so now what is the meaning you want to add object to so of add is a function

1:59:13

first argument is passed with the help of the object so first you are calling this ad function

1:59:19

with the help of this object one right so with the help of self you can get

1:59:23

all those content of ovj1 right if you want to access what are the content you can access

1:59:28

with the help of sell and you passed obj2 as an argument so you can access the content of obj2 also

1:59:35

so that is the thing that is the functionality so let's see how we can overload

1:59:45

very easy okay this is the basic is the basic examples with the

1:59:53

second one we will cover tomorrow this is the basic one example let's assume you have a add

2:0:01

function okay in add function you are taking two arguments

2:0:08

means in the add function you are taking three arguments first argument is the data type

2:0:14

second argument is second and third argument simply says that you want to add these two numbers okay the

2:0:22

the first argument is the data type and the remaining arguments are the thing which

2:0:27

you want to add okay so as i said just like k k w arcs kw asks kws

2:0:34

was keyword base arguments here you you are not sending keyword these are the normal

2:0:40

arguments you have arcs both are exactly same you don't have to get confused kwarks and

2:0:47

arts are exactly same except for this keyword feature okay so what you are saying okay so what you are saying

2:0:52

okay I'm defining this that means I'm providing definition of this ad function

2:0:57

how how can we add first I have to know the data type and just all are not that important

2:1:04

right now but first let me know what is the data type so it will capture only the first

2:1:11

argument and all the remaining arguments will be stored inside arcs right and this will

2:1:16

stored just like a list so what you are saying you are capturing what is the

2:1:22

data type here you'll say if data type is integer then the result is initialized with

2:1:29

zero if data type is string then result in slides as a empty string you can also extend it you can

2:1:37

say if data type is equal to list you can insize result equal to empty list okay so what you are

2:1:44

trying to say if this is the data type what output i'm going to expect so for that you are going to

2:1:49

in slice as i said these arguments are stored as a list and how you can iterate it you

2:1:57

can i means if you remember iteration is nothing but for item in arcs okay and then you are

2:2:05

adding that's plus equal to item so here you don't have to worry about what is what are the items all

2:2:12

items are stored inside args if this is 15 and 61 because you call it two type right so the first time it is

2:2:19

15 and 61 then it will become z is zero because the argument is integer so in that

2:2:25

case red is in slice z zero zero plus 15 result will become 15 okay then again the second

2:2:35

argument will be 61 then it will do 15 plus 61 it will become 76 so output will be 76 in

2:2:43

the first case so how you are doing it with the help of first argument you are checking

2:2:49

what is the resultant type or resultant value so if this is an integer i'm

2:2:55

utilizing with zero if the string i'm in slicing with empty string okay in the second case you have

2:3:02

a string so you are going to slice result with empty string okay and then inside the arcs you have

2:3:09

d r and students so what will happen in the first iteration of this loop you are going to append

2:3:16

d r inside an empty string and you will say result equal to dear in the second

2:3:21

i trace and you will add a student inside dear and it will become dear

2:3:26

students okay if you see the output

2:3:37

76 and dear student so you have the same function but based on this type you can play

2:3:44

okay so this is that so in two

2:3:46

tomorrow's class we will start with the actual class way of doing the operator overloading okay

2:3:53

so any question if there's no question then we can end the class thank you

2:4:16

i will take it over thank you thank you thank you sir

2:4:22

hey guys i'm audible innocent yes or no okay okay okay okay okay uh first i will share one

2:4:30

feedback form then we will be having a one 90 meter quiz uh okay so i'm sharing a feedback form please

2:4:37

feel it fast so that we will move with the mantimeter quiz

2:4:46

guys poll is launched are you able to see that poll are you able to fill your response

2:4:54

there uh can you give an acknowledgement that you are able to see the poll or kill the things

2:5:06

okay okay got it please fill it fast

2:5:16

you know.

2:5:46

You know,

2:6:16

You know

2:6:46

Guys, fill it fast so that we will move with the 90 meter quiz.

2:6:52

There is 53 students here just 14.

2:6:54

Just 41 have filled it.

2:7:16

You know,

2:7:46

You know,

2:8:16

Hey, may you feel it fast so that we

2:8:46

You know

2:9:16

Hey, may you, may you fill it fast, so that we'll move with the

2:9:34

I just just eight people will move with the minute away. I just, just eight people have left.

2:9:36

If you feel it fast, we will move with the mandator voice.

2:9:46

You know,

2:10:16

I will share

2:10:46

I am not feeling the feedback. Please feel the feedback form. I will share in next two minutes if they are not able, if they will not feel the feedback.

2:10:54

The feedback.

2:10:56

These five people are left to fill the feedback form.

2:10:58

I am urging everyone to fill the feedback form first.

2:11:16

You know,

2:11:46

Okay,

2:11:53

It's my screen is visible.

2:12:16

Okay, so

2:12:20

this is, may you please

2:12:26

scan this your code?

2:12:30

Can this QR first?

2:12:32

Okay.

2:12:36

Do you fast?

2:12:39

Do you fast guys?

2:12:46

Thank you.

2:13:16

Please join fast.

2:13:46

You know,

2:14:16

Thank you

2:14:46

I give the length of the length of the of the of the space as well in the chat. You can join with that as well as well.

2:15:16

Thank you

2:15:46

Guys, if you join this past so that we can end this place fast.

2:15:53

Just 39 people have joined.

2:15:55

There are 407 people in the club.

2:15:57

Why are not joining?

2:16:16

Okay, so I am starting now.

2:16:45

Okay, this is your first question.

2:16:46

What is inheritance in Python?

2:16:51

Using multiple object,

2:16:53

using cooperative and existing class, hiding two tasks,

2:16:56

or writing multiple answers.

2:16:57

What is a narrative?

2:16:59

What is the narrative?

2:17:03

What is an article?

2:17:05

I'm going to draw.

2:17:20

Which syntax is correct?

2:17:35

Which syntax is correct for inheritance?

2:17:40

Okay, it's class child.

2:17:45

Okay, it's class, child, parent is cutting a narrative.

2:18:00

No child.

2:18:02

Okay.

2:18:03

This is, this is the third question.

2:18:13

What is polymorphism?

2:18:15

One function, many form, one class, one class, one object, one variable, one form.

2:18:23

Many classes, no function.

2:18:25

Okay.

2:18:27

Okay, everyone is voted.

2:18:36

It is one function, many times.

2:18:40

That is called polymarkism.

2:18:44

That is the fourth question.

2:18:50

Which concepts hide internal data?

2:18:54

What concept is used to hide internal data?

2:18:56

Is it inheritance, polymorphism, encapsulation, or looping?

2:19:03

Is it polymorphism, inheritance, encapsulation, or looping?

2:19:17

It is actually encapsulation, that is that high internal data.

2:19:25

This is the fifth question.

2:19:30

What is in it? What is innate use in all?

2:19:34

Is it that it's the destructor, constructor, loop or variable?

2:19:55

It is an excellent constructor.

2:20:02

Oh, sorry, actually, who?

2:20:09

I will, I will tell the results who has won this in the tutorial.

2:20:15

Okay.

2:20:17

Okay.

2:20:18

Okay.

2:20:19

Oh, the poll, please.

2:20:23

I will show it later, wait and a minute.

2:20:24

written a minute.

2:20:25

Okay, I'm ending the wall.

2:20:34

Yeah, I will show it.

2:20:35

Just written a minute.

2:20:54

Is it shared?

2:21:06

Actually, Joseph M.

2:21:09

The winner of this quiz.

2:21:11

Thank you.

2:21:12

Thank you, Jol Tema.

2:21:13

Thank you everyone for being there.

2:21:15

Thank you.

2:21:17

Thank you for all your support during this class.

2:21:21

Okay.

2:21:22

Let's stop presenting now.

2:21:26

Those who have not any query can leave the class or those who have any query can be there, we will resolve their query.

2:21:32

If there is three questions in a Q&A, I will answer it.

2:21:38

Okay, those who have nothing to say, they can leave the class now.

2:21:43

Oh, yeah, bye for now.

2:21:49

Bye right.

2:21:50

Bye right.

2:21:52

Yeah, you can reach the class now, those will not have any doubt.

2:22:21

any doubt.

2:22:22

Thank you.

2:22:23

I'm ending the class now.