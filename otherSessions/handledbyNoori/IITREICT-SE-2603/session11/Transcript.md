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

Thank you.

5:00

Thank you

5:30

Thank you

6:00

Thank you

6:02

Thank you

6:04

Thank you

6:06

Thank you

6:08

Thank you

6:10

Thank you

6:12

Thank you

6:14

Thank you

6:16

Thank you

6:18

Thank you.

6:48

Thank you.

7:18

Thank you.

7:48

Thank you.

8:18

Hello, everyone.

8:24

Good morning.

8:25

So let's wait for a few minutes because participant strength is too low.

8:48

Am I audible?

8:52

Okay, thanks.

8:55

Let's wait for few minutes.

9:18

Thank you.

9:48

Thank you.

10:18

Thank you.

10:48

Thank you.

11:18

Thank you.

11:48

Thank you

12:18

Thank you

12:48

Thank you

13:18

Hello. Good morning.

13:21

So in the last class, we stopped while we are discussing operator overloading.

13:27

So in what means we are discussing about the overloading kind of thing.

13:32

As we discussed in the last class, now we are going to see how can we overload an operator with the help of magic name.

13:40

And if you can recall, magic name is nothing but whenever you are applying some operator, Python also provide some name.

13:47

So for example, plus has a different name called underscore, underscore, add, underscore underscore underscore.

13:52

So whenever you are doing plus, internally, it is calling that ad function.

13:57

And how you are calling it?

13:59

So object 1 plus object 2 is nothing but object 1.

14:03

. underscore underscore add underscore object 2.

14:06

So you are passing this object 1 also, object 2 also to the magic function add.

14:11

So let's assume you want to implement your own definition of add.

14:15

So how you are going to do.

14:17

do so let's see you have a class a okay so let's assume you are defining your new class and in new class you want to give different meaning of add or plus operator so how can you do it?

14:30

Simply first you are defining a constructor for that class and you're assigning self dot a equal to a now you want to overwrite that definition of ad so you have this magic function and now you are defining this magic function why it will work the region is when we are saying

14:47

the method resolution order. What is our order? First, you have to check, do we have any specific definition for that function in inside my class or not? So whenever you are calling plus, it will check, do we have some definition of underscore add inside my class? It will say, yes, I have this definition. So it's going to call this underscore ad. So what is the meaning of this ad function? I'm simply doing self dot a into self dot, uh, uh, uh,

15:17

a self dot it means this add function will require two arguments right lhs and

15:22

it means lhs of plus operator arches of plus operator is op one plus op two so op one here will be

15:29

self because you are calling with the help of self operator or the uh object of class a and the second thing

15:36

you are passing okay so now what you are doing you are creating an object of class a with argument one so it will

15:45

in slice self dot a equal to one here self dot a will be two again you are creating a

15:51

third argument sorry third object here you are saying a is nothing but a string self dot a will become

15:59

high in fourth object what you are doing you are creating an object of class a and insolizing with

16:05

three now i am doing so just focus on line number 13 i'm doing ob1 plus ob b2 this is nothing but

16:14

ob1 dot underscore underscore add underscore obf2 so you are calling this function and obv1 is

16:22

nothing but one obv2 is two so somehow i'm doing one into two so the answer in this case will be

16:28

one into two equal to two now you have ov3 and ov4 you are using plus operator so in this case what will

16:37

will be the answer try to guess

16:44

yes so what what here we are doing you have this plus operator and the lhs is kind of a

16:59

string operator right so now this is nothing but high into three so high into three

17:05

once whenever you are multiplying a string with a constant number what will happen it will repeat it

17:10

that number of time so here you can see how you can see how you

17:14

you define a different meaning of plus operator with the help of operator overloading.

17:21

So if you have to do complex, means addition for the complex number, you can simply do

17:26

imaginary plus, imaginary and real plus real. So you can define whatever definition you want to give.

17:33

So this is called operator overloading. If you see the output, the first is two and the second is high

17:44

three times. Okay.

17:58

Okay. We will see this letter. First you will see this one.

18:04

So I think in the last class, someone,

18:09

some extent pinged that they want to see the example of how we can pass value to the

18:14

the constructor, A, B, C, the example, which I mentioned. So I created this, you can see.

18:19

So let's assume you have a class called employee. And yes, there's always use case of operator overloading,

18:31

right? I said, let's, for example, you are defining a complex class. So how can you do addition of two

18:37

complex numbers? Because plus means you simply add two numbers, or you can append a string, or you can add

18:41

list to plus you can see internally. This is also a number.

18:44

loaded right it's depend on what is the data type if this is list then there's a different

18:49

meaning of plus if this is a string then there's a different meaning of plus if this is an integer

18:53

then there's a different meaning of plus so based on the data type you can always define what is the

18:59

new semantics of this and you can apply that semantics and provide the meaning of plus so for us plus

19:05

is kind of a math operator but there's no hard writing right you can say in my language plus

19:09

means something else so if you want to do that you can do it

19:14

So here in this class we have, it means this class in class EMP is not inheriting anything,

19:22

so there is no parameter after that. We have a constructor. Constructor is taking two argument,

19:27

ID and name, and we have self.a equal to ID, self dot B equal to name. So we initialize

19:34

A and B are object variable or instance variable and you need slice those values with the help of ID and name.

19:44

have a class fund which is inheriting property from class EMP, from class employee

19:51

you are inheriting. And in the constructor of fun, you have information, ID, name, email. You have

20:02

three things, right? In the base case, you have ID and name. Here you have ID, name, and email.

20:08

So now you know, I am in, means, I have a constructor, which

20:13

takes three argument and this class inherits from the base class called EMP which requires

20:20

two arguments. So you can understand somehow I have to pass this information because you have to construct

20:26

the parent class also, right? So you have to pass these information to your parent class. How can you pass?

20:32

With the help of super. So with the help of super, you are creating a dummy object or proxy object

20:38

of the base class and then you are calling its constructor and you are passing

20:43

ID and name to the base class. And this will call eventually line number two,

20:48

constructor at line number two, and you'll enslave it. And you installize it and you installes

20:52

self dot SQL to email in the current constructor. So whenever you are creating an object

20:58

of this class fun, it will take three arguments because this constructor need three arguments.

21:03

So first argument is 101. This is AP and this is temp enterate mill.com. You created an object. So what will be

21:11

the flow the flow will be this constructor will be called this constructor will call

21:17

the parent constructor because i called super and then this constructor is called here it will

21:25

in slides a equal to id id id is nothing but one zero one b will be ap and the constructor called

21:33

is completed now you'll come back to line number nine then you will see self dot c equal to

21:39

temperate mail.com so now you can see

21:41

whenever you are creating an object with the help of super you can initialize the value of

21:48

base class also parent class also so and if you have to pass you can pass with the help of super okay any doubt

21:55

in this okay okay so now try to answer this question try to understand this code line number 14 to line number 24

22:11

So what will be the output at line number 24?

22:41

Thank you.

23:11

Can someone guess why we are getting this?

23:18

So whoever written 103, try to write reason also why you'll get 1.3?

23:25

At which line I set the value ID equal to 103.

23:41

so if you see the flow what is the flow you created an object and passing jack and

23:56

one zero three okay you have jack equal name equal to jack id equal to one zero three at this point line

24:03

number 10 but are you in utilizing it you are insizing only name if i put employee dot name

24:10

If I'll do employee dot name, then you will see Jack.

24:24

So Harold, at line number 23 in slicing the value, I'm not in slicing at line number 23.

24:33

You are creating an object and you are just passing the argument.

24:38

This is not the initialization.

24:39

This is done.

24:40

inside the constructor.

24:47

If I copy this line.

25:10

And if yes, what will be the difference?

25:25

Yes.

25:27

So now what we are doing?

25:28

We are calling our parent constructor also.

25:31

And inside the parent constructor, we are inslizing the name and we are insizing the ID.

25:37

So even if I comment this.

25:39

Will it cause an issue?

25:46

Because all those insidization can happen and the parent constructors, right?

25:53

So you will see name ID.

25:57

Yes.

25:59

So now you can see if something is inside the parent, but you are not insolizing it.

26:06

You are not calling it constructor.

26:08

Then there's no.

26:09

no meaning of it. Are you able to see this?

26:13

If you are calling this, then only you are insizing it.

26:18

Otherwise, it will say, I don't know what's the value of this attribute.

26:21

So always you have to call the constructor of the parent.

26:25

If you are not calling the constructor of your parent,

26:28

there might be possibility that you will get incorrect answer or you may find some problem

26:33

whenever you are building a large project.

26:36

So whenever you are creating a class object, always

26:39

always think that whenever you are inheriting a class, always define the constructor,

26:45

always call the constructor from the base class and the parent class. Okay.

27:09

I study this in the latest days.

27:11

So, yes.

27:14

So we are studying about the advanced object-oriented programming, right?

27:19

So the first thing which we understood inside this is inheritance.

27:23

Now the second important concept called polymorphism.

27:27

Polymorphism simply says, same interface, different behavior.

27:31

Poly plus morphism.

27:34

So you have same thing, but it is showing different behavior based on.

27:39

the context. So for example, based on the parameters, based on the data types, you are calling the same thing, but it will giving two different output based on what type, with the help of which data type you called it function or you called it operator.

27:54

So we already studied this. Can you let me know what are the things which is provided by Python to support polymorphism?

28:04

The same code is going to behave in two different ways.

28:07

Yes.

28:08

Yes.

28:09

method overloading, matter of a writing.

28:11

So why class object?

28:14

Selim try to answer this.

28:15

Why you have written class and objects?

28:19

So polymorphism can be handled with the help of overloading and overriding.

28:24

So you have the same function name, but it's dependent on whether you have defined inside the parent or you are creating an object of the parent.

28:31

Then which object will be called, which function will be called.

28:34

For example, operator overloading, it will depends on whether you are calling from a string,

28:39

So each object will have different behavior, but one object will always have the same behavior, right?

28:47

You have to understand the same thing should not behave in two different ways.

28:53

An object will always show the same behavior, right?

28:57

Two different objects are two different things, so two different things can behave in two different ways.

29:03

But let's assume A plus B. Plus is an operator.

29:07

Plus has two different things.

29:08

must has two different meaning based on what is a i'm not saying you have two different behavior of a i'm saying you have two different behavior of plus operator and this behavior depends on what is the data type of a so for example a dot foo will have multiple definitions or multiple faces behavior based on in which function it is defined

29:33

a is a object of which class right so the same name

29:38

but it has different meaning based on the context that is called polymorphism different

29:44

action based on the context so method overloading operator overloading method overriding

29:50

these are the examples of polymer fism in last class we also studied about the duct typing

29:57

function to work on different ways based on the data type so if you're not able to recall i'll

30:03

show you the example of duct typing

30:08

so in the last class we studied this code right that typing so you have the same

30:19

function perform task perform task but based on the object that what is the type of this object

30:27

is this a pen or erasure then different function is called so let's assume this part is hidden from the

30:34

user because most of the time the actual logic is hidden from the user right

30:38

user generally call a function from APIs perform task pen perform task erasure so now

30:44

you have same definition of perform task but now it is linking with two different definitions

30:50

based on what is the data type of the object which you are passing inside the function so that is

30:58

called that typing okay so we have seen polyphal miss while studying about the inheritance we have

31:08

have captured or we have covered all the topics which are provided in polymorphism also so you

31:14

have to only understand that all those things are part of polymorphism also so whenever an

31:19

interviewer will ask what do you mean by polymorphism so simply you have to understand if the

31:24

same code is behaving in two different ways based on the context and context can be data type or the

31:31

environment or the object if it is showing that behavior then you have to say this is a polymorphism in

31:37

In Python for achieving the polymorphism, you have three ways, method overloading,

31:41

operator overloading, method overriding, okay?

31:46

Now the third important concept in object-oriented programming is called encapsulation.

31:53

Incapsulation simply says that, okay, forget about three types of programming language.

31:58

Now we want us build a secure, safe programming languages.

32:02

So for making things safe and secure, somehow we have to hide something.

32:07

from the user.

32:08

Because if users knows each and everything,

32:13

then there might be possibility that intruder,

32:16

intruder is also a user only, right?

32:18

Someone wants to hack your system,

32:20

he or see can behave like a user.

32:22

And if user has all the information,

32:24

then hacker can get those information also.

32:27

So that's why by the other object-oriented programming system

32:31

says that we should hide important things.

32:34

We should not expose each and everything to the user.

32:37

So first encapsulation says that, okay,

32:40

just try to see this capsule kind of thing.

32:42

You are seeing this capsule, but you don't have power to see what is inside that.

32:48

Okay?

32:49

If you want to access the data which is inside this, I am going to provide the API.

32:57

Without API, you can't access the data.

33:00

So these kinds of things are hiding detail from the user.

33:03

And you can understand, so currently you might not able to understand how we

33:07

can hide it, we will see it, but at least you should be able to understand why we should hide it.

33:13

And the decision is security perspective. So let's assume your bank balance. If you are able to modify

33:19

your bank balance by simply setting account or bank balance equal to XYG rupees, this is an incorrect behavior,

33:27

right? You can modify your bank balance only by taking some money out or by depositing something.

33:34

So you can see the bank balance will only be more.

33:37

modified with the help of two functions. If I'm withdrawing something, then bank balance

33:42

should be modified. Or if I'm depositing something, then my bank balance would be modified.

33:47

Bank balance is only linked with these two functions. If someone wants to modify without these

33:52

two operations, then there's something fishy, right? So now you can understand how this is related

33:57

to real world also. So in encapsulation, you are simply saying that, okay, I am hiding all those

34:04

things inside some capsule and you can access.

34:07

all those things with the help of some APIs. Without API, you can't do it.

34:13

Object is one kind of encapsulation because you can see inside an object, you have functions also,

34:19

you have data also. But one thing you will notice, till this point, we were not working on hiding the

34:26

data. All the data can be accessed from the class, without the class. You can access it from anywhere.

34:31

But now we will see how can we restrict. How can we say that you can't, you can't.

34:37

access this data if you want to access the data you have to use this function only so we will

34:42

see how we can provide the security features okay so encapsulation says that bind data and

34:48

matter in a single unit so you can clearly understand object is one kind of encapsulation because

34:54

object contains data also object contained method also help in achieving the abstraction how

35:03

this is abstraction because you only have to worry about this outer circle

35:07

kill you don't have to worry about what is inside it so you don't have to understand

35:12

what is happening inside the capsule you only have to think okay there are two APIs i can work

35:17

with that capsule with the help of these two APIs only hide the internal details so for example

35:24

let's assume you are the developer you created the logic for adding to complex number and you give

35:30

this plus operator to the user you you give this a API to the user you give this a API to

35:37

to the users that you can create complex number you can add to complex number with the

35:42

help of plus operator user is only seeing c1 plus c2 but internally what you are doing it should not

35:48

be the interest of user users should get the correct answer and with the help of encapsulation you can

35:54

achieve this now this is the important topic access specifier access is specifier you have three

36:01

different category of access is specifier public private protected

36:07

okay please just see this if otherwise you will get confused and this is very much important

36:13

concept from the security point of view access is westfire says that if there is some data

36:20

or if there is some function who can access this okay now you are guiding that who can access this

36:28

function or data if some function or data is public it can be accessed from anywhere and the meaning of

36:37

anywhere is i can access it inside the class also i can access it outside the class or with

36:43

the help of object also if some variable or function is private it can be only access through the

36:53

class you can't access it outside the class and we'll see the example that we will get the syntax

36:58

error but now only understand public is specified can be accessed from anywhere private

37:05

can be accessed only inside the class so you can't access the private variable with the

37:10

help of object if you want to access you have to access it inside the class only and how can you

37:16

provide this access specifier you have to start the name of the variable or name of the

37:22

method with underscore underscore so if you're starting something with the help of underscore underscore

37:26

it will become private so public from anywhere you can access it private you can only access

37:34

through the class but now let's assume you are doing the inheritance in inheritance you want to

37:40

access the private thing public thing can be access so there is not is not an issue and i said private

37:46

can be accessed only through the class but if you are inheriting you are outside that class right so how can

37:52

i access it so for that it tried it a protected but if something is protected you can access it through

37:59

the class or subclass or the class from which you inherited it you can access those things and

38:04

and the name starts with underscores so let's see the example and then we'll come back

38:08

again go there okay so now see this class you have a class called bank account

38:18

and you initialized the bank account with thousand rupees self-taught balance equal to

38:23

thousand okay so this is a constructor there's no issue now you have

38:30

underscore so balance what is the meaning of underscore underscore

38:37

underscore says that this is the protected one okay so okay even i think this underscourt is not

38:46

required even without that you can continue so okay in in initially let's assume you have

38:52

this normal function so balance okay so why so you are asking why this is protected

39:00

let's show your designer means you are a designer right i am not designing a project i'm just

39:04

showing you how you can create a protect okay so you should not ask why this is protected why

39:09

this is public why this is private once you get the project then you have to think why this is

39:13

protected why this is private i'm showing the example that's why i'm creating something

39:18

which is either protected or so my task is to show you how to create this okay so don't ask reason

39:25

that why this is private why this is protected so i'm not creating a project right

39:30

now let's assume this is a normal function so balance and the task of this

39:36

so balance is simply balance and what is the amount you have in your whatever amount you have in your

39:44

account so technically it will show balance equal to thousand okay now you have this update balance

39:53

the update balance is starting with underscore underscore so i'm saying if you want to

40:00

a private if you want to create a private function you have to start the name of that

40:06

function with underscore underscore okay and then inside that you are giving amount as an argument and whenever

40:15

you are getting this amount what is your task you have to do self-dot balance minus equal to

40:20

amount so you are deducting your bank balance with that amount okay and then you have a normal function

40:27

called withdraw

40:30

Withdraw function simply says that, okay, I want to withdraw some amount.

40:35

The amount you have already mentioned.

40:38

Now you are saying, if balance is greater than amount, self underscore, self dot underscore

40:44

update balance amount and then so balance else invalid withdraw amount.

40:49

So you are simply checking whether this amount is greater than the amount which I am holding.

40:56

If it is greater than that means if my balance is greater than the amount,

41:00

i'm trying to withdraw then withdraw otherwise print invalid amount and whenever i'm withdrawing

41:06

i have to update the bank balance also so i have to withdraw i have to deduct that as you

41:11

now amount from my balance and then i'm printing so balance so now you are creating an object

41:18

of the class bank account so by default constructor will be called and the value will be

41:24

thousand you are calling so i converted this into normal

41:30

function so now i'm calling so balance okay so balance will simply show

41:38

you the balance after that i'm doing account dot withdraw withdraw is just like a normal

41:44

function it will call this you'll subtract 500 from because balance is thousand and you are

41:50

subtracting only 500 from here so the remaining balance will be 500 and you will get this as an answer

42:00

oh so balance is 1,000, is 1,000, then it will become 500.

42:23

So, Krunal has asked, is balance is private, public or protected?

42:30

question is balances private protected public sort of why you are thinking

42:45

that this is private? Whenever you have to create something private what you have to use

43:00

So for private, you have to use underscore underscore.

43:09

Am I using underscore underscore underscore before balance?

43:16

If I'm not using underscore underscore underscore underscore, then this is by default a public, right?

43:24

But if I will do this, if I'm uncommenting this line, line number

43:30

20 account dot underscore underscore update balance 500 okay what should be the behavior

43:45

so i'm calling a private function from outside a class you are inside the class you are inside the class you can call the private function okay but here you are

44:00

inside the class, you are calling a private function outside the class.

44:06

And if you are doing so, Python will simply say, I don't know about this attribute.

44:15

This attribute doesn't exist, okay? So you are getting a error.

44:22

So now you can understand this is for the security point of view also. So the security point of view is that

44:30

Even if you have access to this function, even if somehow you know that I want to update the balance, you want to call it, but you can't call that function, right?

44:39

It will give you the error.

44:41

And this business logic from line number one to line number 16, that is written by the trusted person.

44:48

So you are trusting the whole code written inside this is correct, true.

44:52

And this is the line number nine is the only thing which is updating or changing your balance.

44:58

you can't call this function from outside the class then you are safe and secure that the balance is not going to be modified by some intruder or malicious person so now you have to understand that whenever you are designing a software you have to understand what are the critical or important things make all critical and important things as a private variable so generally it's recommended that all the data

45:28

should be private. All the data should be private. And whenever you want to access those data, you must have to provide some APIs just like this.

45:40

So function, so balance, here you can simply say that balance is a private and so balance can show you. You can't see the balance also from the user point of view. Okay. So this is the normal general suggestion.

45:54

And that's why

45:58

Only from the naming point of view, there is no change in the syntax.

46:01

This is only naming point of view that whenever you want to set data, whenever you want to get data, you have to write two special functions called getter and setter.

46:13

So there's only speciality in the name except for that there is no speciality.

46:17

So why it is calling getter or setter?

46:20

Just try to see this.

46:23

You have an employee class and then you created a salary and the variable salary is public.

46:28

private.

46:37

You see why this is public?

46:39

Now it's starting from underscore underscore.

46:46

So now what I'm saying is as our design principle says that every data should be private and you always, if you want to set it or get the value of it, you have

46:58

to use the special function, getter and setter.

47:02

So now what I am doing?

47:05

Get salary is nothing but return.

47:07

What is the salary of that employee?

47:10

I'm inside the class so I can access the private variable.

47:14

There is no issue.

47:16

Set the salary means I'm getting some value from the parameter.

47:21

And if amount is greater than zero, salary is amount.

47:25

Otherwise you're saying invalid salary.

47:27

You can't set negative.

47:28

So this is just a sanity check or regular check.

47:30

So now what you are doing, you created a object of the class employee.

47:36

And first you are printing what is the salary of the employee.

47:41

And then you are setting the salary of an employee and then you are again printing it.

47:48

So if you see the output, just a second.

47:58

50,000, 60,000. If I'll print this, what will the output?

48:28

As this is a private variable, you can't access outside the class.

48:45

That's why you will see the error at line number 16.

48:50

It will say it has no such attribute viewed.

48:55

So again, this is just a design principle.

48:57

There is no change.

48:58

in the syntax or semantics only you have to understand if some variable is

49:04

a function or variable is private start with underscore underscore if this is public just

49:10

start normally without using an underscore and if this is private and you can protected

49:14

then you can start from underscore so getter and setter and setter we already have

49:20

studied what is getter and setter. Getter and setter are the name of a spatial function

49:26

whose use is to getter.

49:28

the value or set the value of the private methods, okay?

49:36

Helper function to get and set the private variables.

49:40

Okay. So if you recall, in last week, I mentioned you, do we have get?

49:47

No, means with the help of normal function also, you can do this. You don't have to specifically

49:51

mention ad rate, getter, at the rate, setter, even without that. So here you can see, right?

49:56

Even without the ad rate getter, without ad rate get the setter, you can achieve the property or achieve the goal which you want.

50:05

So in last week, I requested you people to recall me whenever we complete this topic.

50:12

And the reason was, we have to understand custom exception handling.

50:18

What is the meaning of exception handling? Are you able to recall?

50:24

What is exception handling?

50:26

So how the exception handling is different from if else?

50:56

with the help of if else only.

51:14

So in the last week, whether we are studying about the exception handling, we studied that how can we, if something bad happen, in

51:26

future? How can we predict it, detect it, and we can handle such types of cases?

51:32

So the such type of cases like whenever you are doing division, you might get divided by zero kind of

51:38

error at runtime. So whenever you are accepting something may cause problematic thing in future,

51:43

you always write it inside tri-block. Okay? Inside a tri-block, if you are able to complete that

51:51

thing, that is fine. Otherwise, it will cause the exception.

51:56

And you can handle the exception.

51:57

You can print what is the type of exception and you can raise the exception also.

52:02

But the main problem, it means we studied till that point was there are only well-defined exception handler.

52:10

You can't write your own custom exception handler.

52:13

But now we have sufficient expertise that we can write our custom exception handler also.

52:18

So the custom exception handler means if you want to add some more exception based on your project,

52:26

Okay, this scenario might occur. So for example, if your account balance is X rupees and you are withdrawing money, which is more than X. You should throw an exception, right? But these types of well-defined exceptions are not part of Python. So you want to write your custom exception handler. So how can you write all those such type of exception handler? We will see. Okay.

52:56

So now why we postpone this topic after this class and object, the region is you try to think internally how Python works.

53:05

So Python has created a class of exception, okay?

53:10

And if you want to create a custom exception handler, by default, you have to inherit that class.

53:16

So base exception handler class is kind of a parent class or base class.

53:21

And whenever you are writing a custom exception handler, you have to create a,

53:26

inherited version of the base class because maybe functionality wise it is different, but you have to support the common thing, right?

53:34

So tri-block will remain, concept of tri-block will remain same, the concept of exception block will remain same.

53:39

Somehow you have to print something else. You have to handle something else.

53:42

So what you can internally assume, I'm overloading, I am just inheriting the base exception class, and then I'm overriding the base exception class, and then I'm overriding the base definition all of those overloaded class.

53:56

you have to overload the functionality which is provided by the base exception class so for that you have to understand what is inheritance then you have to understand what is overriding that's why we delayed this topic but we now we have covered all those topics so now we can cover this one also okay

54:15

so create a class that it had it from built-in exception class or its subclass so the syntax should be something like this what is the meaning of this can

54:26

someone say what is the meaning of this line?

54:56

already a class which is either defined by me or by Python in this case it is defined

55:01

by the Python built-in library itself okay so you don't have to worry exception class is

55:06

already defined by the Python you are creating a new subclass based on that base class

55:14

and the name of this subclass is my custom error define the functionality of custom

55:21

handling so how can you define you have to provide your

55:26

constructor that if some exception happen what you are going to behave and as i said this is

55:32

inheriting so somehow you have to pass this message to the base exception class also so this is a

55:40

general trend every error has some code right which generally for enumerating it this is a normal

55:47

convention that every error should have code so that's why this is your custom if you are also

55:54

defining a new error code so that is

55:56

in future you can understand with the help of this error code also so whenever you are

56:00

defining a custom exception handling you have to send two important things one is what message you want

56:08

to show what message you want to throw and what is the error code the message which you want to

56:14

throw you have to pass to your parent class and error code you are storing here now you are

56:22

able to set up the basic thing for your exception

56:26

handler now you have to call your exception also right because if you defined it but you are not

56:31

calling or you are not raising then there's no use of that exception right you have to raise the

56:36

exception how can you raise simply by using raise keyword and the name of the exception handler the

56:43

name of the exception handler is my custom error so now we will see the example then we'll come back to

56:52

this slides once again

56:56

okay so now try to see this program what we are doing we are creating

57:09

a invalid age error or exception the name of the class is invalid is error and

57:17

we are inheriting from the exception class so exception is the base class now what i said what is the

57:25

normal is suggested way so here in this case i'm not passing the error code if you see this

57:31

slide also this error code is for my bookkeeping this error code is not required for the base class

57:40

so here the base class required what is the message you want to show once you are able to reach that

57:46

exception so i'm saying the message which is provided by the constructor or whenever i created this class

57:52

this message and the age so what message you are passing to your parent class

57:57

message plus but your age is so what is the meaning of this line line number three

58:05

what is written inside this parenthesis can someone interpret this what is written inside

58:10

this parenthesis and what is the use of this f

58:22

yes so this is a formatted string so what it says that message is a type of string

58:44

i'm appending this string with the string which i have written here what i have written here so f is

58:51

nothing but just a syntax of the formatted string it is saying but your age and here i have

58:57

written something inside the curly braces the whatever written inside a curly braces is treated as a

59:02

variable and this variable will be replaced by the actual value and what will be the actual value

59:08

actual value is right from the parameter itself so it will simply say whatever the message i'm

59:12

passing plus but your age is and whatever the age you have passed so this string is going to pass to

59:19

so the constructor of the base class of this inherited class and the base class is

59:25

exception class okay now you have the actual definition so you are defining a function called

59:32

check age okay inside check age you will get is as an input so this is the logic so now you are not

59:41

doing exception handling you are simply writing a definition normal definition what you are writing

59:47

you have to check the age whether that is less than 18 or greater than 18

59:53

if age is less than 18 then i know something bad happens if age is less than 18 i know something bad happens

1:0:01

so i want to raise a custom exception handler which i created right now and how can i raise it i

1:0:10

can simply raise it raise and name of the class what is the name of class what is the name of class invalid age

1:0:17

error and as this constructor requires two things i have to pass the two parameters also

1:0:24

the first parameter is age must be 18 and above this is a normal string which is nothing but this

1:0:29

message and the age is whatever the age provided by the user and if this is not the case then

1:0:36

you are simply accessing the grant this grant access granted okay so now you have learned that what is a minimum thing

1:0:46

i'm not saying this is the only but what is the minimum thing for writing a custom

1:0:50

exception handler you need a message and this message should be passed to the parent constructor

1:0:58

okay and whenever you think now something bad happen so there are two things please note that

1:1:06

there are two things one is a code base where a error can occur those code base should be written inside try

1:1:14

when you are going to say raise when you understood that now the error has happened

1:1:21

now the error has happened then you are raising the custom exception handler now from where you are

1:1:30

calling this function means you define this function right check age in the code you must call this

1:1:36

function otherwise this is never triggered so this is the part where you are calling this function

1:1:43

so if you're calling this function then you might notice that you can get this exception

1:1:49

so this code should be written inside the tri block okay you tried it and let's assume you entered

1:1:59

age equal to five then you raise this exception right because five is less than 18 this

1:2:06

exception is raised you are getting this message and in the try block you will get the exception has

1:2:13

occurred so invalid and what type of exception occurred the name of the exception is invalid

1:2:19

error so accept invalid as error e and then you'll print custom exception got and e e e is nothing but

1:2:27

the message you printed there so if you see the output you will see like this

1:2:43

enter is to custom exception caught why you are getting this because now you see

1:2:51

are trying so the actual logic is starting from line number 10 you are entering the age

1:2:58

you are checking the age when you are checking the age you notice that something bad happened

1:3:05

you raise the exception you raise the exception so try will understand that okay after

1:3:13

this I have to raise the exception and the exception is raised and what type of

1:3:19

exception is raised this type invalid age error so it's printing custom exception

1:3:24

you see custom exception caught right and then I'm printing this E also is nothing but

1:3:32

it is storing the metadata or the information regarding the exception we pass this information

1:3:38

so you can mess over approximate that this is the information stored inside the E it is

1:3:43

stored more than that also but you can assume this is storing e only so what is

1:3:48

written age must be 18 or above but your age is this then you are printing age must be 18 or

1:3:54

above and but your age is two and after that execution completed because that is the use of finally

1:4:04

just see this code once again i'll ask a question see this code

1:4:13

If I enter age equal to DGFG this line, what will be the output?

1:4:25

So just see I entered age equal to DGFG what will be the output?

1:4:43

Thank you.

1:5:13

so it will say a value error the region is this line is age equal to int whenever you are

1:5:26

converting a non integer to an integer it will say this is a value error and when there's

1:5:32

a value error you are catching this exception it will say invalid input please well

1:5:37

invalid input please enter a number is completed okay

1:5:42

now some one student asks that if i want to so what this question is if we want to raise

1:5:48

error for age above 100 do we need to create a new class or we can edit in the same class as the

1:5:54

custom error so this is just a printing message so when you are calling this exception it depends on

1:6:01

if else so for example if it means the objective which you want to achieve we can achieve with the help of this

1:6:06

also right if age is less than 18 invalid age error age must win 18 or above

1:6:12

if age is greater than 100 then i'll say invalid age error i change the message but i'm

1:6:18

printing the same thing i change the message age must be 100 or above sorry 100 or below and your

1:6:24

age is 100 okay okay so again custom exception court age must be

1:6:42

or below. So any question in exception handling?

1:7:12

question so waiting for that

1:7:42

so you don't have to create a new class for that you can handle with the help of that

1:7:49

that only but okay so you have to understand this exception represents a class of events right

1:7:58

if you can mix or bunch them inside a same class then it's fine so invalid agent so for achieving

1:8:06

this you can create a new class also right it's not an issue but

1:8:11

no you can't do it with a custom message error custom message this is the

1:8:18

recommended way that you have to write a custom exception handler and inside a custom

1:8:22

exception handler you are messing this so that in the small project it will not create an issue in the

1:8:27

small project i hope you never use the tricass block also because you will see okay this is the common

1:8:32

case i can understand but if you're working on a generic and a big project which is shared between

1:8:38

multiple teammates then this exception handling will let you know

1:8:41

and help you to understand what is the exact error you are seeing now again this is a design

1:8:46

principle if you are handling all those exceptions inside the same class only because the help

1:8:54

with the help of this class you are simply distinguishing that this exception is totally different

1:8:58

from the other exception which is called if you are clubbing all those exceptions in the single class

1:9:04

then in future it will create a mess while you are doing debugging if you are writing custom

1:9:09

some exception for each and every different scenario then the code size will be huge

1:9:13

you will not able to understand also so based on the design and based on the objective you have to

1:9:19

understand which thing you have to mix and match okay so some exception you can club some

1:9:25

exception you can't club but this is not restricted by the python this is restricted by the design

1:9:30

principle okay so let's take a break means we'll meet at 12 05 and then we'll start the fundamental of

1:9:39

and budget control.

1:10:09

I don't know

1:10:39

You know.

1:11:09

You know

1:11:39

You know

1:12:09

I'm

1:12:39

I'm

1:13:09

I'm

1:13:39

I'm

1:14:09

I'm

1:14:11

you

1:14:39

Thank you.

1:15:09

Thank you.

1:15:39

Oh, sorry, I was on mute. Okay. So, what is the answer of this fight?

1:16:09

So whoever is writing destroyed, that answer is incorrect.

1:16:39

What is the answer of this?

1:16:45

So please don't write answer of other questions.

1:16:49

Please write answer only which is highlighted.

1:16:51

Otherwise, this gives me confusion.

1:16:59

Okay.

1:17:01

So what is the answer of this?

1:17:09

What about this?

1:17:20

This one?

1:17:36

Good.

1:17:37

Good.

1:17:38

Okay.

1:17:39

Okay. So let's get started with a new topic called version control.

1:17:49

And I hope many people already using this thing or face the problem related to this or aware about the solutions of this, but they might not be using it.

1:18:00

But all of you must be aware, used, or heard about this problem.

1:18:05

So let's see what is this.

1:18:09

So version control simply says that, okay?

1:18:12

So let's assume you are working on some project.

1:18:15

So forget about how many people are there.

1:18:17

You are alone working on that project.

1:18:20

And this project is used that it requires 30, 40 files and each files contain more than

1:18:25

thousand lines of code.

1:18:28

You build that software and it's working fine.

1:18:34

And then you want to add some more feature and while you are adding some more, you are adding some

1:18:39

more feature, you created a mess and now it is not working.

1:18:43

So how will you go back to the previous correct version?

1:18:48

Can someone give a solution for this?

1:18:51

If you created a project that is working perfectly fine,

1:18:56

but after doing some modification, now it is not working.

1:19:00

So how can you solve this issue?

1:19:02

How can you go back to the last correct version?

1:19:09

So all are we saying by rectifying the error? Yes, that is a nice answer, but let's assume you don't have that much time. You have to submit your project by today's 5pm.

1:19:38

and you don't have that much time to submit the project and currently your project is in very bad state.

1:19:44

At least you will say, okay, I'm not able to fulfill this goal, but previous all things are working, right?

1:19:49

So you want to submit that project.

1:19:51

Let's say you don't have time to rectify.

1:19:56

By eliminating new added feature, how will you...

1:19:59

So let's assume the added feature spans in all the files and you have written some part in this file, some part in some other file, inside some function.

1:20:07

How can you do this?

1:20:09

Save a copy of a previous version.

1:20:16

That is the initial solution. Save a copy.

1:20:20

But there's a problem with that solution.

1:20:22

So one of the strength is suggesting that whenever you are at the correct stage,

1:20:27

simply save that copy.

1:20:29

And then you can start working after that.

1:20:32

Again, if you're facing some issue, at least you can go back to the saved correct version.

1:20:36

correct version.

1:20:37

How many copy you will save?

1:20:40

So actually, please don't write using version control, version control.

1:20:46

If you are good in version control, please skip the class.

1:20:49

I'm setting the platform for each of the students you are spamming by writing using version control.

1:20:55

Maybe all the students don't know, right?

1:20:57

So for that, I have to give the motivation and the background.

1:21:03

So let's assume the initial solution, some of the strengths,

1:21:06

we will save the last working copy.

1:21:09

So how many copy you will save?

1:21:11

And how you are sure that that copy is also correct?

1:21:15

Maybe you are understanding that, okay,

1:21:17

at that time it's fulfilling the goal,

1:21:19

but after some time you realize that there's some issue

1:21:22

in that solution, in that copy also.

1:21:25

You want to go back even before that.

1:21:27

So eventually what you will think,

1:21:29

I'm going to save copy after each day, right?

1:21:34

That's a solution might work.

1:21:35

might work that every day you are saving the copy.

1:21:39

But the problem with this solution is like

1:21:42

you are creating a multiple copies.

1:21:45

So first problem is disk space.

1:21:48

So that is not a nice way to save a copy.

1:21:52

But frankly speaking, that is the first solution which is used.

1:21:55

So always we created a backup

1:21:57

and we are saying something bad happened,

1:21:59

we are going to that stays with the help of copying.

1:22:02

Okay?

1:22:03

So now you can understand why version can understand why version

1:22:05

control is important.

1:22:06

Currently, you don't know what is the solution,

1:22:08

but you can understand why version control is important

1:22:12

because maybe you want to go back at some particular point.

1:22:15

So for example, let's see.

1:22:18

If you are using, if you have used Linux operating system,

1:22:22

you must heard that after two years there is a stable version,

1:22:27

like 1 to 22, 124, 1 to 26, 18, and that is valid for 5 years.

1:22:33

So after 2 years, there is least a stable version.

1:22:34

After two years, they are releasing a new version, but they are maintaining the previous version also.

1:22:38

So at the same time, they are maintaining the previous version also, the current version also.

1:22:44

So in their system, they have multiple versions of it.

1:22:48

How can we handle that thing also?

1:22:50

So let's assume you are releasing some software or whatever your favorite software,

1:22:54

you can assume that every year or in some frequency, they release some stable version of it, right?

1:23:01

And they are working on the previous version also by saying that,

1:23:04

bug fixing, like for example, Android also.

1:23:06

Latest version of Android is released.

1:23:08

But for the last few versions, they said that we are providing the support.

1:23:12

Maybe for the first version or the second version they are saying,

1:23:15

now that is outdated, we are not providing the support.

1:23:18

But at least for the last few versions, every tech company says that we are providing the support.

1:23:23

So you can understand, they are not starting from the scratch

1:23:27

because the latest version is somehow the modification of the previous version.

1:23:31

Then they should not start from the scratch also.

1:23:33

also so in their system they have multiple copies theoretically you can understand there are multiple copies one corresponding to each version but it will create an issue regarding which version is correct how I'm going to pinpoint that this is the latest version or the older version how many copies should I create so for solving those kinds of issues we created a different solution that's called version control now even after it so currently you are working only on

1:24:03

that project, no one working with you.

1:24:05

But now, let's assume, you are in industry.

1:24:07

Many people are working together.

1:24:09

First thing, you want to check who added this code, right?

1:24:14

Because let's assume you are saving a copy, you created a stable version, you saved it.

1:24:20

You are not maintaining that who created that file, who modified that file.

1:24:25

So that in future, let's assume something bad happened in that part,

1:24:29

you can ask that person that you created this code, can you create this code, can you

1:24:33

please fix this because you are aware of that code base right so that's why you can ask that please fix this issue so for that you have to maintain all those information that who modified the code what was the last correct build these are the important thing one more important thing is like if you are modifying something on a file and some other other teammates is also modifying the same file how can you fix all those issues because there might be possible

1:25:03

that you are working on the same code base you are modifying the same code at a time how can you fix or how can you identify which version is correct and which version i should use so for solving all these problems there's a system called version control system was defined so any doubt in the motivation why we need version control how can we do don't worry about it but any doubt why we need version control

1:25:32

why just creating a backup copy is not good first it will use lots of space the second thing is like even if you are backing up you are not worrying about this space there's still some issues that who modified the code that is the first problem if there are multiple people are working in a team you want to modify a file which backup files should i use which is stored in my system or which is stored in his system so for all those

1:26:02

things we have to create a centralized mechanism which can solve all those issues so version control systems is system that track changes made to file over time so here we always say files but you can assume anything okay the directory the whole code base because that is just a combination of files okay so you want to create a system that is going to track all the changes I'm not saying

1:26:32

you can change major change minus change it's going to track all those changes which is made

1:26:38

about the file from where the file is created so that you have the snapshot you have the

1:26:43

image of each and everything regarding that file that who modified this file when he modifies the

1:26:52

file what is the last correct version of this file you have all this information if you have all this

1:26:58

information then you are always in good shape but when you are always in good shape but when

1:27:02

you are designing such systems you have to think that i should not take so much space also

1:27:07

otherwise most of the company resource are going to be used in version control only save and track changes

1:27:14

revert to previous version collaborate branch okay so these are the important things these are the

1:27:21

important features which we have to provide in our version control system the version control system

1:27:28

should be able to save and track the changes if i'm not able to save something

1:27:34

and i'm not able to track what change at what time span there's no use of such version control

1:27:41

let's assume you are saving but you don't have power to revert to the previous version again

1:27:46

that version control is not nice the solution which you are going to use it should be used among

1:27:52

multiple employees also because maybe it's working for single employee but it is not working

1:27:58

for the multiple employees that again that VCS you should not use so why we are studying

1:28:04

these things the region is maybe you are aware of Git there are many other version control systems

1:28:09

like SVN you can use if you know what is the best rooted for your company each and every subversion

1:28:18

control system is good or bad you have to decide for your requirement which is better no one

1:28:25

can say that this is always superior in all of the cases it's always

1:28:29

depend on the use case so you have to understand what is your use case and what type of version

1:28:34

system you have to use branching and merging we will see it later first we'll understand

1:28:40

why these topics are important then we'll see but this is one of the important feature of

1:28:43

version control okay so this is kind of an architecture of a version control system okay

1:28:55

is the user so now you can see there are multiple users okay so what is of one of the

1:29:04

requirement we can collaborate right so that is now there are multiple users so you can assume

1:29:10

there they can collaborate these are the lowest label entity users each user has its own

1:29:18

copy of repository so let's assume the code base which is provided by your industry each user has its

1:29:25

own copy user one has its copy repo user two has its own copy repo user three has its own copy

1:29:32

repo these three repos might be slightly different from each other these all are originated from the main

1:29:41

central repo so this is the actual code base so you see the actual android code base is you can assume

1:29:48

this is the first employee who is working on the android code base it will create it will simply copy the

1:29:55

repo into its own system and we'll try to modify something okay so this this second table

1:30:01

is called local repository each user may have a different view different image of the repository

1:30:11

the top level is the centralized repository this is consistent everyone will see the exact code

1:30:19

base over there now you will see why and how we are going to interact why we have to create multiple

1:30:25

repository okay now see the region let's assume you join the company already there must

1:30:32

be some code base right because it's not like you are starting from scratch you have to start with the

1:30:36

first main file itself already there's some code base you are here this is the complete code base you will

1:30:45

pull that code base into your machine if you are copying from main repo to your local repo that is

1:30:54

called pull i'm pulling the codebase from main wrapper to my local rapport

1:30:59

and no so the repo of this one user one can never become the main repo you have to do

1:31:10

something else but this is the central repository first you are taking changes from

1:31:16

taking the whole code base from the main repository let's assume you join you have nothing

1:31:21

you are the user one only and you have the central

1:31:24

both you pulled the changes and now you have the consistent copy of the code base what is the

1:31:32

being of consistent copy whatever written inside this repository you have the exact such change okay now your

1:31:39

task is not to only copy or pull the repository you have to do some changes also right now you are

1:31:47

modifying the code base now you are modifying you are modifying the code base now you are modifying you are

1:31:52

changing the codebase you are updating deleting you are adding some feature you are doing

1:31:57

locally right whatever the feature you have implemented till now is neither here nor here nor here

1:32:05

it's it is not presenting any of this repository it is only in this repository already okay once you are

1:32:14

sure that this feature is correct i have done all those things then you are committing

1:32:22

that okay now i'm saying that this is the one of the final version of the feature which i

1:32:29

provided you committed it currently you can assume committed is kind of saving you saved all those

1:32:36

changes okay forget so this is a technical word that's why i use commit but you can use whatever

1:32:42

the changes you made you saved in this repository once you saved it you have to share that

1:32:49

information to each and everyone also right

1:32:52

so how can you say this information do you have any link between repository of user 1 and

1:32:58

repository of user 2 there's no direct link right so what you will do you will push all those changes

1:33:05

to the central repository right you have to push all the changes which you made to the central

1:33:13

repository right so now these two are consistent but the changes you pushed here is not with

1:33:21

user 2 and user 3 right so that's why it generally says that whenever you are starting

1:33:28

a work or whenever you are starting a day you should pull the changes so that whatever the information

1:33:34

it's shared among all those information all those users i should get that image so what we

1:33:40

learn from here with the help of pull you are getting the central image or central snapshot of the

1:33:48

whole repository you are doing something

1:33:51

you are saving slash committing and after committing you are changing you are pushing

1:33:57

that change to the central repository now you saved it you pushed the changes to the central

1:34:03

repository the other user whenever they are going to do pull they will get that information is

1:34:09

there any doubt in architecture please let me know please take two minutes understand if you have

1:34:14

any doubt let me know because you will see there is no use of this but when you go to the industry

1:34:20

you will realize this is one of the most important thing you will get

1:34:22

if you're not able to handle these things properly

1:34:50

okay so one of the question asked by culpays is what if changes are not correct will

1:34:56

previous base repo is stored so okay there are few things which we missed here

1:35:03

whenever you've made some change okay before pushing it there's a step called

1:35:11

code review okay and that is a totally different thing that's not related to

1:35:16

architecture but for making that there might be possibility that you have returned in

1:35:20

correct code of incorrect thing and you're posting the central repository

1:35:24

for stopping these kinds of thing there's an intermediate step which is

1:35:29

provided by the testing team or the intra team they said that whenever you are pushing a

1:35:34

code you have to get approval from your teammates or the code reviewer or from the manager

1:35:40

so first you have to pass all the test case so how can you say the code is not correct if you are

1:35:46

not able to pass all the test cases right so if you are able to pass all the test cases right so if you are able to pass all

1:35:50

those test cases and your managers slash team leads slash your teammates approve that this code

1:35:57

is correct then only it will be pushed so that is the internal infrastructure of industry but from

1:36:05

the version control point of view you can push an incorrect change also here because version control

1:36:11

system doesn't differentiate between what is correct what is incorrect but version control system should

1:36:16

provide you the functionality that in future even if you are able to understand that

1:36:20

that this code is incorrect, somehow I have power to remove it or go back to the previous correct version.

1:36:27

I hope this answers will be right.

1:36:50

So now we will see some terminology.

1:36:55

So this is the basic terminology or basic things which we will understand so that we can work on any of the version control system.

1:37:05

So eventually we are going to focus on Git only.

1:37:08

But you should have fundamentally that much knowledge so that you can work on any version control system.

1:37:14

Okay.

1:37:15

Now let's assume this. Okay. So currently we are discussing

1:37:20

about this repo okay so trunk means what is the main what is the main code base okay

1:37:31

main code base that is theoretically you can assume that is the correct code base that is well

1:37:37

tested well reviewed there's very slight chance that there's a bug in that code base okay that chain

1:37:44

is called because whenever you are modifying so you can assume you are creating kind of a chain right what you did

1:37:50

you create so you have this trunk that main chain is called trunk i am representing

1:37:56

with the help of green color and number one now i said that you copied it right here one of the main

1:38:06

thing is you can see there's a branching you can see right from one i created two branches one is going to

1:38:13

four others is going to two why whenever you are modifying a code this is

1:38:20

a normal suggestion that you should create a branch branch means we will see the command

1:38:27

also for creating the branch but you can technically you can think you are creating a copy

1:38:34

this is the correct code i'm not touching that correct code i am creating a local copy and we

1:38:41

will say it a branch and i'm doing this modification here only so whatever modification you are doing here

1:38:48

here whatever modification you are doing you are not affecting the code base of the main trunk

1:38:55

and it out so inside your local repo so i'm not saying you are changing here i'm talking about this

1:39:01

rep only the repo which you just have you have the main branch or trunk you are not doing anything over

1:39:09

there you created a new branch and you are doing code over here whenever you create a new branch you can

1:39:18

assume simply internally you can assume it's creating a copy so it's creating the code

1:39:23

is copied one in this direction one is in this direction so you are not changing anything which is in

1:39:28

the correct direction you are modifying your changes in your own branch you are modifying some

1:39:35

branches and then you realized that yes trunk is main brand main or master yes once you are able to

1:39:45

convince yourself that my branch is correct

1:39:48

i achieved the goal which i want to do eventually you have to merge that branch into the main branch right

1:39:58

or the trunk branch master branch whenever you are coming from this branch the branch you created

1:40:05

you are merging into the main trunk that is called merge okay so you are mud so now kind of you are

1:40:12

deleting this branch and adding all the changes you made

1:40:18

in this branch into the main trunk branch okay so eventually you should have only one branch

1:40:24

only but whenever you are doing the code base so why i'm okay so can someone let me know

1:40:31

why we should create two branches as i'm working on my local repo why should i create a different

1:40:38

branch i can change the main thing also because i'm not affecting this central repo i can do whatever i want

1:40:45

here why should i create a new branch can someone give me suggestion or

1:40:52

intuition for this so that is not that is not that important you can do with the

1:41:10

so that is not that important you can do with the help of main branch also the main important

1:41:15

thing yes the main important region is let's assume there's a file a dot's python okay

1:41:21

which is inside the main branch there might be possibility that some other user is also working on

1:41:29

a dot python and that person boost his changes in the central repo and what we suggest

1:41:37

that whenever you are working in a team it's generally

1:41:40

recommended that you should frequently pull otherwise there might a possibility that the

1:41:45

feature on which you are working or the code in which you're working already it is modified by

1:41:49

someone else so you should frequently pull those changes so what you are doing you are pulling

1:41:55

those changes and if you both are working on the same branch means you are not creating a different

1:42:02

branch then it will create a conflict that let's assume you added some line at particular point

1:42:08

the other users has added some different line

1:42:10

at the particular point it will create a confusion and we'll say conflict we will see it later

1:42:14

but it will create a confusion which line i should keep which line i should remove so that's why

1:42:19

whenever you are working everything you have to create a branch and whatever you are pulling the actual

1:42:25

trunk is moving forward whenever you are pulling the correct code is already there in the trunk so whenever

1:42:32

whenever you are merging you have the correct code also means the latest code also and you can merge it here otherwise

1:42:40

if you see the practically there's practically there's no use of two and three you can write it inside

1:42:47

here also but whenever you will do this full kind of thing whenever you are taking the central image

1:42:53

it will create lots of conflict and you'll become very much frustrated you will not able to resolve

1:42:58

and you will see that okay most of the time are going to resolve the issue only so that's why

1:43:03

the solution for this is you should create a new branch work on that branch and then you should

1:43:10

merge it once you are able to do it okay so we are able to understand what is trunk

1:43:16

what is branch what is merge now there's an important thing called tag tag is nothing but

1:43:23

a pointer or some renaming or local name for this so let's assume just think about android right

1:43:32

android i hope they push patches every day because there are lots of employee actively evolving

1:43:40

regular changes so daily they are doing some commit can report to access by

1:43:45

report no rapport two can't be accessed by report three and i hope you are talking about

1:43:50

repo two is this one and repo three is this one there's no direct link between them and why you want

1:43:56

to see the code of others so you you you can only access the code of central repo or your repo you can't

1:44:03

access until unless that person shared your code with you you can't see

1:44:10

okay so let's do you think from the android codebase point of view daily they are changing

1:44:18

there are lots of patches they are pushing but there are few important checkpoints so for example

1:44:24

android version 16 Android version 70 or whatever the number so there are some important points right

1:44:30

that this is the latest stable release this is the first stable this is the second stable release so we

1:44:36

gave some important name to those last

1:44:40

commits so here you will say okay this is called my first stable version so that

1:44:45

in future you can easily understand you don't have to dig it out that which is the last stable version

1:44:51

so kind of four has two name one is four and other is t1 so with the help of t1 you can say

1:44:58

okay this is the last stable release i can go here directly so it's just a nickname

1:45:04

nickname fancy name common name for accessing this four

1:45:10

now again we are simply replicating it what we are doing we have a branch we are merging

1:45:18

we have a tag once we are able to successfully do it okay you will see this branch line number 10

1:45:26

it is still not merge because you are currently working on it and eventually you will merge because

1:45:33

that isn't a development branch so whenever you are working on it you should not merge once you think that

1:45:40

i am done i've completed my task then you have to merge okay so any doubt in this diagram

1:45:48

or any doubt in trunk branch merge tag so tag is nothing okay tag is just a name so in future you

1:46:03

want to see what is my last stable version so tag is nothing but it's storing uh giving a name last stable

1:46:10

version equal to four so you want to go at some particular point you are simply going to say

1:46:14

because four is not a nice name to remember right but a fancy name last stable version that is a

1:46:21

fancy name so you are just giving a tag trunk primary line of development main road where stable

1:46:29

code lives branches separate line of development work in progress kind of parallel role without disturbing

1:46:37

main road merge

1:46:40

working for combining work in progress to trunk tag named snapshot of a code point so you are

1:46:47

simply giving a nice fancy name okay get is one of the version control system so till this point

1:46:59

we understood what is version control what is one control system what is the need of version control

1:47:04

right you are able to understand now we will see one of the important version control system

1:47:10

system which is used in most of the industry git

1:47:20

get is a distributed version control system user work on local copy post changes to the main

1:47:26

branch what is distributed version control system what is distributed what is the meaning of distributed

1:47:40

this is distributed you can assume this architecture is actually matching with the architecture of git

1:47:51

each user has its own copy distributors and you have a centralized repo you're communicating

1:47:57

with centralized repo with the help of push and pull

1:48:02

created by Linux Torvalds in 2005 and this person also created a Linux operating

1:48:12

system and for creating this linear operating system he thought we need something nice so he created

1:48:17

get what are the capabilities of Git track changes in file so that is our one of the

1:48:23

requirement right in our version control system this is one of our requirement track changes in file

1:48:30

track history and

1:48:32

commits who modified it what is the modification when he or she has modified

1:48:39

so this is called history collaboration means many people can work on the same project

1:48:47

get provided and do mistakes so let's assume you are able to understand that some bad

1:48:54

code is checked in in your code base how can you fix this get provide functionality for

1:49:02

that also okay branches you understood what is the use of branch why branching is

1:49:08

important so now you need that support also so git provide that support also okay

1:49:18

so we will see commands tomorrow i'm going to show you important things what are that means we

1:49:24

will run it in the whole say in the next session otherwise i will complete something today and

1:49:29

then you will keep loss or means you will not able to

1:49:32

like it and the next class again we have to start so i'll give you the brief overview i will

1:49:36

show you and we will do it by yourself in the next class so there are common git commands and you can

1:49:45

understand why they are common why we have to use this how we are going to do this we will see in the

1:49:51

next class so first i'm always saying repo repo repos repository repository so somehow you have to

1:49:59

to create a difference between directory and repository right so how can you convert a directory

1:50:05

into repository so now there are two things one thing is if repository is already there you have to bring that

1:50:13

copy into your system that is the first scenario right are you able to see what is the first

1:50:18

scenario the directory the repository is already there you are the new person you want to get the copy from

1:50:26

the main server to your machine that is the first use

1:50:29

case the second use case is the first time the code is going to be started because it

1:50:34

them this is true for the first time right the central directory doesn't exist you are creating the copy

1:50:41

and then you have to send it to the main server so the second part called in sly jason that currently

1:50:47

there is no central repository you are creating and then you are pushing so once you create a directory

1:50:54

you will do git in it which you are doing the in slide jason now a normal directory will become

1:50:59

repository and then you have to send it to the server.

1:51:18

So we will do on the base or freshly new directory in the next class but I will show you if some diet is already existing

1:51:28

existing,

1:51:29

how it will show and what is the meaning of this get status is kind of showing you what

1:51:34

are the files which is modified by you and still not checked in inside the main repo it's

1:51:44

simply letting you know what are the files which are modified by you and not post into the

1:51:51

the code base so this is already a git repo if i am doing get status it is saying

1:51:58

then you have these files which are modified okay so let's assume

1:52:07

um-hmm okay so you see what i did i opened this file code of conduct dot md and i

1:52:23

added this file uh modified this file i added this file i added this line

1:52:28

a right after that i did git status it simply says that modified code of conduct

1:52:38

d okay it is showing this thing also untracked file so there are two types of file in

1:52:45

git system tracked file and untracked file means git already knows that these files are

1:52:52

these files are part of this repo and tracked file means i created these files

1:52:59

and the central repo of git is not aware of these files so no one has any copy of this file

1:53:08

so try to understand the difference between this and this because i did git status it divided into

1:53:13

two part right the first part says that this file is modified by you and you and

1:53:22

everyone else has this file but they are only missing your changes the untrant file says

1:53:29

that these files are only with you and if this is only with you then obviously it's modified by you all

1:53:36

right no one knows about this file so this is the meaning of git status so git status is kind of

1:53:43

letting you know what are the changes made by you and how it is different from the other person

1:53:52

now let's assume status is done you want to add something what is the meaning of

1:53:58

add add simply says that okay i modified this code and i want to send it to the central

1:54:06

repository so how can i send it how can i how can i push this data to the central repository

1:54:13

the first step is at least let me know what you want to send so for that you have to simply do add

1:54:22

add code of conduct so it is simply saying that okay i modified this file and i want to

1:54:30

edit so this is a useless and bogus commit so i'm not adding it but you can understand if you

1:54:36

want to send this change to repo how can you do it first you have to add what change you want to do

1:54:44

okay so how can i do get add and name of the files which you modified and want to send

1:54:52

if you are using so there are two types of add generally the second one is not recommended the first one says that

1:54:58

git add file name so you will add file name one by one so you want to add this line you want to add this file

1:55:05

if you are using this dot it means that it will add all the files which you modified there might be thing

1:55:15

that you are doing some testing you don't want to post something but you modified it if you are using this dot it will

1:55:22

add that file also so dot is a shortcut it will save your time but it may push some incorrect

1:55:29

changes also because you don't want to push something but with the help of dot you pushed everything

1:55:35

whatever change you have made so that's why the git add file name is a generally recommended so now

1:55:42

you added the file as i said it maintained history also right in the central server it maintained history also so for that

1:55:52

after adding i have to do commit so if you remember this is the commit part right so i said

1:56:01

you can say this is the storage or storing something commit simply says that okay i made this change i'm

1:56:08

very much happy with the code i want to send this code to the user but to the central repo but before

1:56:15

sending this message to central repo i want to put my stamp over there that i am the

1:56:22

author of dispatch i submitted this patch at this time and why i submitted this patch okay

1:56:30

this is very much important why i submitted because let's zoom in future you want to recall oh

1:56:35

what changes i made in this so the comments or the information you want to add you can add so if you see

1:56:41

let me get log okay so this is the standard format so i saw how can you add a comment

1:56:52

this is git commit minus an initial commit so the meaning of this will be the file you added

1:56:59

you added with the help of add command now you're adding a message that i want to commit and

1:57:06

the message will be just initial commit or whatever you want to say if you see the general thing

1:57:11

these are the general commit status you see right everywhere there's a

1:57:16

commit again there's a commit so this is the whole snapshot of the central repository so each

1:57:25

commit will have some id you don't have to worry about this ID this ID is automatically

1:57:30

provided by the Git repo system okay so you don't have to worry about this ID

1:57:35

by default with the help of Git commit it will add your name as an author your

1:57:41

email id inside this it will add a time stamp also that you post this message you post this

1:57:49

change at this time okay and i said it hyphen m initial commit these are the things with for

1:57:58

example dispatch response to remove support for really old one to release after this remove support so

1:58:03

blah blah blah whatever the message you want to write inside this after this hyphen m all those

1:58:10

things will come here

1:58:11

so in the log you can see i have hold the information that who said this what is the

1:58:19

why who sent this patch at what time that person has sent this patch and why that patch was there okay

1:58:27

if you want to see the patch that okay here you have this brief overview currently you are not

1:58:33

able to see the code if you want to see the code how can you see this commit has some ID right you can

1:58:41

copy this id and then you can do get so and the id which i copied it will show you the

1:58:51

changes made by the user so these are the changes made by the user so they modified

1:58:59

this destro dot touch file and destro dot cp file and inside this they modified so in the next

1:59:07

class we will also understand what is this patch format why there's a plus why there's a minus

1:59:11

but now you can get some clarity so with the help of git log you are able to see all those

1:59:17

so i said right wins with the help of vcs you should able to keep track of all the changes

1:59:22

with the help of this command git log you are able to simply keep track of all those changes

1:59:29

right so this contains all the history if you are particularly interested in some history you can

1:59:34

simply copy it get so paste it it it will show it will show you will show you will show you

1:59:41

what are the changes inside this okay get log it will show you the what is the history of the

1:59:52

current branch if you want to see how many branches are there then there's a command called

2:0:03

git branch so this is the main branch trunk branch master branch and this is the branch created by me okay so i'm

2:0:11

on that branch so to help of this you can see how many branches are there and once your

2:0:16

work is done you can merge this branch into the main branch so you can see any doubt in this

2:0:23

so we will do the demo of each and everything we'll create a fresh repo we will send it we will

2:0:28

pull it we'll push it don't worry we will do all those things any doubt

2:0:41

one after merging branch three into trunk four so what is trunk force so

2:0:46

please please explain all those things because trunk four i never mentioned where is trunk four

2:0:51

so please write it again okay okay so if there's no question then we can end the class and in the

2:1:03

next class we will work on this git commands in detail we will create a repo we will post it pollid

2:1:09

will achieve all those functions

2:1:11

in the next class so kushi you mentioned sir please give the overview of all

2:1:23

these terms in the beginning of next session for calling them better i'll suggest please see

2:1:28

the video also okay i'll try to give it but please see the video also if you have any doubt and

2:1:34

if you have doubt then you can ask this question okay okay thank you

2:1:41

take care bye bye

2:1:46

guys i'm audible

2:1:48

just wait a second so hurry you asked sir where may i practice these types of questions so

2:1:54

what type of question can you please explain so that i can give you the pointer that's why i'm asking

2:1:59

like git come on okay so git is a helper tool you can do so obviously you are working on some

2:2:06

project right or you are developing maybe you're interested in python java or whatever the

2:2:11

programming language website development do one thing create a git repo and push all those

2:2:16

changes on git create a branch by default so there's no exam kind of thing for this you will

2:2:22

do practice for yourself then you'll become comfortable okay so do one thing just push all those changes

2:2:28

whatever you have made into the get repo you'll get clarity familiarity regarding this

2:2:36

okay thank you bye bye

2:2:41

Hello, am I audible? Yes, so I am raising a feedback form first. Okay, so please fill the feedback form.

2:2:51

Are you able to see the feedback form?

2:2:56

Please fill it fast.

2:3:11

Thank you.

2:3:41

Thank you.

2:4:11

Thank you.

2:4:41

We haven't reached the topics yet. We haven't touched all those topics about the Git. That's why I am not launching the quiz. That is the thing.

2:4:51

As per the thing, so I will quit the class in here. You can, you can quit the class.

2:5:11

Hi, about YouTube channels, recommendation for the which topics, Harry? Are you talking about Git or the first topics about oops and all?

2:5:32

Just wait two minutes. I will let you know about those.

2:5:41

links here.

2:5:44

Actually, I will share all those channels from where I learned about oops and get and all.

2:6:01

So wait for two, three minutes and the class, those who want YouTube channels, yeah, sure, sure.

2:6:11

Thank you.

2:6:41

You can take the help of Chai and Code channel. I am sharing a link.

2:7:11

this you can use the revision for the tubes and python okay any any other any other thing that you want to ask

2:7:41

What you said the link?

2:8:11

is the link now are you not able to see that?

2:8:15

Yeah, this is an YouTube link.

2:8:23

Are you able to see it now?

2:8:27

Okay.

2:8:31

Any other question?

2:8:41

Okay, anybody have any doubt?

2:8:43

Yeah, thank you.

2:8:44

Welcome, welcome.

2:8:45

Anybody have any doubt?

2:8:48

Uh, one more thing. Those who have any doubt or anything, you can book in one-on-one session with me.

2:8:58

We will try to resolve your doubt there or we have a TA session as well.

2:9:02

Because I got so many curates in the Q&A.

2:9:05

Yeah, welcome, hello, welcome.

2:9:09

So there will be two things.

2:9:10

be two things. One is in TA session. If you are not able to understand in a TA session or you feel shy or anything, I would say ask openly anything, any question in any session.

2:9:20

Or if you want, you can book in one-on-one call with me as well. We can try to resolve your doubts here.

2:9:26

Thank you. So those who not have any doubt, they can leave the class, not in problem.

2:9:30

Okay.

2:9:31

Wait, those who not have, those who don't know about the one-on-one session, I am sharing with a link here.

2:9:39

sharing with a link here one on one on one on one session as well so you can book it if you want

2:10:09

yeah yeah this is a link in a chat okay so i'm ending in a class okay okay so i'm ending in a class now

2:10:39

Okay.

2:10:40

Anybody have any doubts?

2:10:45

Any doubt?

2:10:47

Any doubt?

2:10:48

This is a one-on-one call schedule. You can use this link to book in one-on-one one-on-one call.

2:10:54

Or we have a DA session as well on this Tuesday.

2:10:57

I have resolved the problem of connector and screen sharing and all.

2:11:01

So we can, we don't have any interruption during the session for now.

2:11:06

Also one more thing, Deepak says.

2:11:08

Deepak sir will be joining from the next class.

2:11:11

So those who have concern about the Deepak sir, he will be joining from the next class.