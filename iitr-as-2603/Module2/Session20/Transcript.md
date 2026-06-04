0:00

Yeah.

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

Thank you.

9:50

Thank you.

10:20

Thank you

10:50

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

Thank you

11:38

Thank you.

12:08

Thank you.

12:38

Thank you.

13:08

Thank you.

13:38

Thank you.

14:08

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

Thank you

17:08

Hi,

17:12

Hi, everybody.

17:15

Hi, everybody.

17:16

Gooding all of you.

17:35

We will start on here.

17:38

Hello, everybody.

18:08

Thank you.

18:38

Thank you

19:08

So, today we'll start on with a completely new

19:23

with a completely new topic called unsupervised learning.

19:30

So all of you settle down.

19:33

I will just be initiating my conversation.

19:38

Thank you.

20:08

Thank you.

20:38

Thank you

21:08

Thank you

21:38

Thank you

22:08

All right.

22:12

So let's

22:18

All right,

22:21

So let's start on.

22:23

So let's start on.

22:27

There was actually a couple of files that I wanted to upload for all of you.

22:31

I hope everyone is able to see my screen.

22:34

This is the third June folder which I have shared with you.

22:37

with you.

22:38

A lot of interesting stuff we will talk about in this session.

22:41

And first things first, what I will do is I'll quickly set the context in terms of where we are right now

22:47

and what we are trying to achieve in this particular session and just going to quickly take you through

22:56

the mind map.

22:57

So we are very much in the machine learning module at this point in time.

23:01

So we are pretty much in the machine learning module.

23:03

The last session we were in, we discussed about the ideas.

23:06

the ideas. Just one second, guys. So the last session we talked about the concept

23:13

of supervised learning. Until the previous module, we talked about supervised learning,

23:20

regression, classification. I think now we have a very good sense in terms of how we can effectively

23:25

build models where the output is known. Okay, if the outputs or labels are known, we can pretty

23:31

much build a model. We have seen that piece. And now today's session is getting in the

23:36

to unsupervised learning. What is unsupervised learning? Unsupervised learning is that kind of machine learning where the outputs or labels are not known. So what do you do in a scenario where the outputs or labels are not known? So that is the thing we will see. And broadly speaking, you know, there are two broad topics we will discuss. Most of the sessions we will discuss about clustering. We will discuss a very interesting, you know, concept called clustering. And very briefly towards the end, I will cover something called PCA, principal component analysis. So we will discuss these two

24:06

broad topics in the session. And obviously, you know, we'll look at some real world use cases, how clustering is useful.

24:13

So unlike in supervised learning where we are trying to make some predictions, in unsupervised learning,

24:19

we are basically trying to form groups and clusters of data. Okay. So we have, so we will see that overall.

24:24

And obviously from here onwards, the next module. So all of these will eventually lead us to the next

24:28

module, another two to three more sessions we are left out with and we are moving on to the absolutely

24:34

the exciting phase of gen AI agents and agentic systems. So this is where we are we currently

24:39

are in our overall journey. Now, to talk a little bit about to very quickly just to recap what is

24:48

supervised learning and what is unsupervised learning. I think everybody, I'm sure at this point in time

24:53

you recall from our very introductory sessions. So supervised learning is that kind of machine learning

25:01

where the output or labels are known to us. Okay. So what is supervised learning?

25:07

Supervised learning stands for that kind of machine learning where the outputs or labels are known.

25:13

Okay. So we know what the outputs are. We know what the labels are and that is what we refer to as supervised learning.

25:18

The outputs or labels are, you know, kind of known to us. That's the way how we understand the meaning of supervised learning.

25:25

So because otherwise, if you don't know the outputs, you cannot build a model. So only way you can build a model is if you know the

25:31

outputs. If you do not know the outputs, if you do not know the labels, then how do you even

25:35

learn the patterns? And that is the context with which we have done all our exercises until now.

25:42

Starting right from linear regression to lasso and rigid regression, we discussed about logistic

25:47

regression and just a Monday session, we talked about random forest and decision trees. In all these

25:52

exercises, if you look at the kind of problems we have taken, in all these exercises, we had some X and

25:57

we had some Y. So we had some inputs and we had some outputs. Input, output, output, output,

26:01

combinations were given to us. Okay. And all that we were trying to do is we were trying to learn

26:07

the patterns. We were broadly trying to learn the patterns on the basis of these input

26:14

output combinations. Inputs were given, outputs were given and we were broadly trying to learn the patterns.

26:19

What are the patterns that is what we were trying to figure out? Okay. And that is effectively what

26:25

supervised learning is. So our labels there, yes, labels are present. The goal is to predict the known

26:30

output and these were some of the examples that we have seen what is unsupervised learning

26:34

unsupervised learning is that kind of machine learning where the outputs are not present and maybe

26:41

another thing I can do is I can take you back to one of our very initial sessions we have done

26:46

before long back this was I think let me quickly look it up this was back in the month of

26:51

May we did this class on 11th of May I'm going to just take a moment and take you back all the way back

26:59

back to that session. And if you remember, I had discussed about this, you know,

27:04

discussed about this particular diagram with all of you. That time I introduced to you,

27:10

what is supervised, what is unsupervised? And I told you unsupervised we'll talk more about later.

27:13

And today is that class when I talk about it. So unsupervised learning is that kind of machine learning

27:18

where the outputs or labels are not defined. So if you remember, this was that beautiful analogy

27:23

that we took, right, where you have a, you know, a kid in a kindergarten.

27:29

and you are trying to teach a kid about different types of fruits, right? So how do you,

27:36

how do you go back and teach a kid about different types of fruits? How do you teach a kid about

27:41

different types of fruits? You show the kid an apple, you show the kid a banana, you show the kid an orange.

27:47

So you end up showing the kid different, different types of fruits. And you tell them that, hey,

27:51

you know, fruits like these are apples, fruits like these are bananas, fruits like these are oranges.

27:56

And the kid somehow learns or understands the patterns, basically.

27:59

on this. That's the way how we relate to it. So I repeat again, you show the kid, you show the kid

28:08

different, different types of fruits. You show the kid different, different types of fruits and

28:12

and you tell them that, okay, this is apple, this is guava, this is banana, and so and so forth.

28:19

And based on that, you learn the patterns. You learn the patterns, basically. That's the way to

28:26

look at it overall. That's the concept.

28:29

What is unsupervised learning? Unsupervised learning means all of a sudden I will hide the output.

28:35

Look at this bottom part. All of a sudden, I've hidden the output. I'm no longer telling you what the fruits are called.

28:42

I will still show you the fruits. I will still show you this, this, this is this, this is this. I'll show you, you know, three, four different things.

28:51

But I'm not telling you what they're called. I'm not telling you, hey, this is called an apple, this is called a banana. This is called, no.

28:57

But I'm showing you the different fruits.

28:59

And your objective is to go back and I understand what are the similar fruits and what

29:05

are the dissimilar fruits? So we are primarily trying to understand similarities and

29:10

dissimilarities from the data. That's the big picture idea that we are trying to that we are

29:16

trying to solve. So we are trying to understand what are the similarities and what are

29:20

the dissimilarities, you know, of fruits, which are the similar fruits and which are the dissimilar

29:26

fruits based on the features that you're able to see.

29:28

Inputs and features.

29:29

Outputs of the part in here.

29:31

We're outputs bathe not here.

29:32

So that is why we often say that in unsupervised learning, we are often trying to find patterns

29:38

or clusters of data.

29:40

So supervised may, our regression classification that story is over.

29:44

We have seen that.

29:45

Now in unsupervised, we are, because we don't know the output, we don't know what to predict, but

29:50

we don't know what to predict.

29:52

But what we are trying to do is looking at the features of our data.

29:56

We are trying to understand the patterns.

29:58

What are the patterns?

29:59

Are they similar fruits?

30:00

Are they dissimilar fruits?

30:02

These fruits are similar.

30:03

These are different like that.

30:04

So this is the big picture idea of what unsupervised learning basically stands for.

30:09

I hope everybody is aligned.

30:10

We have seen this.

30:11

We have kind of gone over it before.

30:13

I will take you to another very nice demonstration.

30:16

And this I have also shared in my notes.

30:19

Let's take a real use case.

30:21

Because, you know, the best way to understand the concept is to take on real use cases.

30:26

Imagine if, imagine, because fruits for example was a general use case.

30:33

I want to take up a real retail use case so that you can really relate to it,

30:36

that what are what do I mean by saying clustering?

30:41

What are what are we trying to do?

30:43

Let's talk about it.

30:45

So we are all buying something in Amazon, right?

30:47

I'm Amazon app.

30:48

Amazon. app, Amazon.comme, Amazon.com, by the way.

30:51

you go to the website, you log in, you search for different products,

31:00

and sometimes you buy something also.

31:03

Now, every time you do these kinds of things in Amazon, remember, Amazon has a track about you.

31:08

Amazon's everything tracker.

31:09

Amazon is tracking who you are?

31:11

How much time you're spending?

31:14

Because he track can't, that this account's logged in and this account is active, this many number of hours.

31:20

Amazon is able to track that.

31:21

that who you are, what time you logged in, how much of money you will spend,

31:27

overall you spent in the platform.

31:30

So Amazon is able to keep a track of that entire data, entire detail.

31:34

How much of time you're able to spend on the, this thing.

31:37

So the whole thing we are able to keep a track off.

31:42

That's the intuition.

31:47

Now, whatever you are seeing on the screen, this is how the,

31:51

the data will be collected, right? You will collect the time and money. How much time did

31:57

customer spend? How much money did customers spend? Every row will be like a customer.

32:02

These all features are. X, here there's no output. So first I wanted to understand the data

32:07

collection part. When you're data collecting, there is no concept of output you have. It is not like

32:14

the kind of problems we were doing in Monday session. Monday we were looking at the features of a person to

32:20

to predict that his disease has or not? We were looking at the,

32:25

one problem we were looking at the features of the transaction to predict that

32:30

fraud is or not? He defaulted or not? But here, there's no output. We only have the features of the

32:38

customer. Customer Amazon's login. It's our details we know. He's how much time spent

32:42

and how much money spent. Now here is the interesting part. On the right hand side, you can you. On the right

32:47

inside, you can plot as a scatter plot. Everybody knows a scatter plot. Every dot on that

32:55

scatter plot corresponds to one customer. If you see every dot on that scatter plot, every dot on that scatter plot

33:03

corresponds to one customer and you're able to see the different, different features of the customer.

33:07

You can't see all the details here per digger. So every dot on the scatter plot corresponds to one

33:12

customer and we are able to see the different features of the customer.

33:15

You can you can see this is a customer who is spending this much time, this much money.

33:26

This is the customer who is spending this much time, this is the customer who is.

33:29

So we've only customer to call customer to data go plot

33:33

here. There is no concept of outputs here. And it is through this that we are trying to visualize groups

33:40

groups or clusters of data.

33:42

As we have data ploted, you know, these are customers who are very similar.

33:48

These are groups of customers who are very similar.

33:50

These are groups of customers who are very similar.

33:54

And these are groups of customers who are very similar.

33:57

But these are groups of customers who are very different.

34:00

So we are able to clearly see customers who are similar, customers who are similar and customers

34:06

who are different.

34:07

We are able to very clearly see that pattern.

34:11

And these are customers who are similar.

34:12

These are customers were similar and these are customers were different.

34:16

And this is your clustering concept.

34:19

I think in many ways, if you remember, we had a module in Python.

34:26

I think we have discussed it briefly.

34:29

Exploratively data analysis.

34:31

We were something that was doing in that time.

34:33

What were we doing in ADA?

34:35

We were giving some data and you were trying to explore the data in different, different ways.

34:40

So, we often say clustering is a form of advanced RIDI.

34:45

Now, clustering may be a kind of way to do you are trying to take the data

34:49

and you are trying to explore the different patterns of your data.

34:54

And this is what we refer to as unsupervised learning, clustering kind of problem.

35:00

And the specific type of clustering that we did here is what is referred to us.

35:04

But the domain is the actual problem that we solved here is what is referred to as customer segmentation.

35:10

So actually what problem solved here right now?

35:13

We actually did something called customer segmentation.

35:16

So we looked at the customer data.

35:19

We, excuse me, we looked at the customer data.

35:25

We understood the patterns.

35:29

What are the different, different features of the customer?

35:32

And based on that, we are able to figure out.

35:34

And based on that, we are able to, you know, in a way, intuitively figure out,

35:40

based from the customer data, that these are features which are very similar.

35:43

These are features which are very similar and these are features which are very different.

35:46

Customers which are very different.

35:48

So that's the way how we can understand the idea behind this.

35:51

So clustering is one type of problem that is related to unsupervised learning.

35:56

We will heavily focus on this topic for today.

35:58

That is the main agenda.

36:00

We'll look in detail in how we'll do it.

36:02

So we will see that.

36:04

Another related topic, which is not the in the scope of the course,

36:07

this coverage is not.

36:08

But I just wanted to talk about it.

36:10

You know, everybody is encountering it every day, right?

36:13

So everybody's using Netflix.

36:15

A Spotify in a song are singing, Amazon music you're trying to turn on, turning on.

36:19

Every time we are full of recommendation systems.

36:22

So recommendation systems are also another very classic application area of unsupervised learning.

36:28

Sometimes people might be wondering, that you're recommendation in what do you're doing?

36:31

Now we've got this machine learning but it is not supervised learning.

36:35

You're not trying to predict anything.

36:37

You're Netflix on movie.

36:39

Netflix predict are that,

36:40

you might like to watch this movie.

36:43

Customers who watch this movie also like to watch this movie.

36:47

Customers who watch Transformers part two,

36:48

he will transformers part three be there.

36:50

The Spider-Man one day,

36:51

that Spider-Man 2 be.

36:53

And you're you,

36:54

you're going to similar movies recommend

36:56

to.

36:56

Look at Amazon.

36:57

You should, you buy something.

36:58

You buy a phone.

36:59

He'll be phone with phone with you might like to buy discharger also.

37:02

What is it?

37:03

Is it predicting something?

37:04

No, it is grouping.

37:05

It is clustering similar items together.

37:07

So recommendation is a.

37:09

grouping problem.

37:09

Recommendation is all.

37:11

Movies in, music,

37:12

there's social network,

37:14

Facebook be recommend

37:15

friends,

37:16

LinkedIn recommend

37:16

connections,

37:18

LinkedIn job

37:19

be recommended.

37:19

Recommendation

37:20

are everywhere.

37:22

Here they're over in Uber

37:23

is recommending

37:25

Uber is recommending

37:25

Uber, what

37:26

is what is

37:26

the algorithm,

37:28

internal algorithm

37:29

but if you

37:30

think about Uber

37:30

broadly,

37:31

you're when when

37:31

you're right

37:32

booking

37:32

then you're

37:33

there

37:34

there's 10 customers

37:34

here here

37:35

there are 10

37:35

drivers

37:36

that basically

37:37

matchmaking

37:37

are not?

37:38

So it is basically

37:39

matchmaking

37:39

ideally.

37:41

And a lot of

37:41

matrimony

37:42

sites and all

37:42

these are also doing

37:43

the same

37:43

recommendation.

37:45

So right

37:45

sharing food.

37:46

So idea is the same

37:47

isn't it?

37:48

So recommendation

37:49

is also a very good

37:51

application of unsupervised learning.

37:53

And if I'm to

37:54

talk about

37:55

one more level of detail

37:56

that

37:57

how it's going to

37:57

behind the scenes.

37:59

So

37:59

we'll take a Netflix

38:01

example for a minute

38:02

your features

38:04

here here.

38:05

Here we've talked

38:06

about.

38:06

Let's example

38:07

me we talked about it, time and money, your customer level features, right?

38:12

What about Netflix?

38:13

So here, we will have information about, we will have information about the features of the customer

38:21

and we will have information about features of the item.

38:25

Item, I mean, the movie that you're watching.

38:27

So what are the features of the customer and what are the features of the movie?

38:33

So we will, so we will know that, hey, you know, customers like this are watching these kinds of movies.

38:37

Excuse me, customers like this are watching these kinds of movies.

38:41

Customers like this are match up, you know,

38:44

watching these kinds of movies.

38:48

And you'll be able to find a pattern.

38:51

You're here here here

38:52

be cluster or pattern

38:53

do not predict

38:55

not. You are trying to predict that

38:58

which type of customers are watching which type of movies.

39:02

So next time a similar kind of customer joins Netflix

39:05

or then you know, Netflix to log in to home page

39:06

go.

39:07

time a similar customer comes, I will recommend that customer also to that similar

39:12

kind of movie.

39:15

That is basically what, how, you know, recommended systems are also a very good application area

39:21

of unsupervised learning.

39:23

Outputs not.

39:24

So theoretically, one line of that theory is not there.

39:28

But I just wanted to take some examples to help you understand.

39:30

Because, see, I believe that in the world of AI, framing the problem is very important.

39:37

Nowadays, code is available.

39:39

Your code generation, chat, GPT,

39:41

Gemini, you know, you know, your code will be.

39:44

All right.

39:46

But you know, what really sets you apart from

39:49

the average people is your ability to look at a business problem.

39:54

If any interviews in whatever interviews you go for,

39:57

whatever enterprises you work for,

40:00

how can you look at a particular problem and frame it correctly?

40:03

Is it a supervised problem?

40:05

Is it a un-supervised problem?

40:07

that is the very, very important skill, right?

40:11

Because once you know that, it becomes a very deadly combination.

40:15

And finally, one last aspect I wanted to cover, which is anomaly detection,

40:18

one type of this is also kind of related to unsupervised.

40:22

But if we are trying to find which transactions are anomalous.

40:25

Oftentimes, there's labor data, you will not know.

40:28

Before frauds happen, before transaction frauds happen, you will not know in advance, right?

40:34

So this is also like a very, very interesting kind of unsupervised learning problem.

40:37

problem. Now let's talk about how these things are done. So all this while,

40:42

you know, I was just trying to introduce what is unsupervised. Now we will specifically look at an

40:45

algorithm called K means. Now we will specifically understand the K means algorithm. And

40:52

using the K means algorithm, we will go back and try to learn exactly how these clusters are created.

41:01

Right. Now, before I get any deeper, all of you just give it a glance once. Like, I know this is

41:06

So, there's a lot going on here. But just before I discuss anything further, 0.1, 0.2,

41:13

0.3, 0.4.5, just give it a quick read all of you. Just give it a quick read all of you.

41:20

So this is a specific algorithm of K means that we are covering right now.

41:25

So all of you just give it a glance, whatever I'm showing on the screen right now.

41:36

Thank you.

42:06

Thank you.

42:36

Thank you.

43:06

Thank you.

43:36

Thank you.

44:06

Thank you

44:36

Thank you

45:06

So as you can see, guys, what is going on here.

45:11

exactly, I will talk about it.

45:13

I will talk about it.

45:14

Step five, I know, I know, I know, repeat steps three and three. I'll explain. I'll explain. I'll explain to you. Don't worry. Don't worry. And I'll take a beautiful animation to, you know, you know, help you understand this in a better way.

45:26

So don't worry. So what is going on here? Let us talk about it. Okay. Let us talk about it.

45:31

So first, a couple of technologies I want to clarify. What is a centroid? Centroid is basically basically not

45:36

but the average value. So I think this diagram very beautifully explains what is going on.

45:44

So we can talk about the same story that we were discussing sometime back. This is the amount of time spent

45:50

in the x-axis and in the y-axis, we have the amount of money spent. Okay? So x-axis, we have the amount of

45:59

time spent and in the y-axis we have the amount of money spent. That is what we have here right now. X-axis,

46:05

is time spent, y-axis money spent. And every dot corresponds to a particular customer.

46:15

Same use case I was discussing a while back. So all these are customers who are part of one

46:21

one group or cluster. All these are customers who are part of one group of cluster. All these are customers who are

46:26

part of one group of cluster. This individual dots are one-a-kestimated. This is your customer one

46:31

customer to a customer three right what is the centroid centroid is like the average of all these

46:38

customers so these are all part of cluster one these are all part of cluster two these are all part of

46:46

cluster three these are the centroid of cluster one that means this data point this particular thing

46:53

is somehow telling you on an average whatever we are seeing in cluster one on an average

46:59

what is the amount of time the customers have spent and what is the amount of money customers

47:07

have spent in cluster 1 that is what this refers to so what is the amount of time customers have spent

47:17

and what is the amount of money that customers have spent in that centroid

47:23

uh sorry in that particular cluster it is somehow telling you the average behavior of

47:29

the group. Similarly, we can look at another one. These are all the customers who are part of

47:36

cluster 2. And here also we can see that the centroid tells you, on an average, what is going

47:43

on in that cluster? What is going on in that cluster on an average? So, on an average,

47:50

the amount of time spent is so and so, and amount of money spent is so and so. And finally,

47:56

say cluster 3, you are trying to find out what is going on on an average in cluster 3.

48:03

So we can say the amount of time spent is so and so, again, the amount of money spent

48:07

is so how much time you're spending, how much money you're spending in cluster 3.

48:12

So that's the intuition that we are getting right now overall. So on an average, what is

48:16

going on in each of the three clusters is what you're able to understand. That's the basic idea

48:21

behind what centroids are. Now let's get a little deeper and understand.

48:26

this thing and I will take up a beautiful animation to explain this in a better way.

48:36

So let us say, friends, you have this thing. T.K. You have this. So I think you will

48:44

remember. You'll not remember this, right? Yeah, then I can try to show you this side by side.

48:50

Okay, you can see this briefly. This will be better. You can see this briefly. On the right. On the right.

48:56

the site. And we're with you

48:58

see what is going on here behind the scenes.

49:04

Now,

49:04

here

49:06

here

49:06

your data. First step

49:09

what is? Choose K clusters.

49:11

Now, I think

49:12

this is a very easy problem. You're looking at the problem

49:14

and wondering that sir, we already know this is three

49:16

clusters. But again, I'm just starting

49:18

out with an easy example.

49:21

We are trying to understand the algorithm.

49:23

Algorithm what?

49:24

So here here three clusters.

49:25

Choose a lot.

49:26

value of K. So you will choose the three

49:29

clusters. And I will randomly place the three clusters. So initially I will not know, right?

49:33

So I'm a cluster here. I will take one more cluster here. I will take one more cluster here.

49:39

There is no particular reason I've done it this way. I've just randomly taken three

49:43

clusters. So decide the number of clusters and randomly place three initial cluster centers.

49:52

So these are the three initial cluster centers I'm placing. Remember, these are the three initial cluster centers I'm placing.

49:54

Remember, these are not the correct cluster centers.

49:58

Cluster centers, what are cluster averages.

50:00

Ultimately, when we will be able to see the exact average value of the clusters.

50:06

Right now, it is not complete. Right now, it is just the approximate

50:09

approximate thing that you're able to see on the screen.

50:14

So we have done until here. We have initialized the centroid.

50:19

Next step, assign every data point to its nearest centroid to firm clusters.

50:24

This is sort of tricky. Let's understand that. How do we do it?

50:30

So we find out what is the distance of every single point from the respective centroid?

50:35

Now, this point consider kind of.

50:37

Here there are three centroid. Right? Red centroid, green centroid, and blue centroid.

50:41

So basically we have to find out which point is closest to the centroid.

50:46

If you talk about this point, we'll find out the distance from the red centroid.

50:49

We'll find out distance from the green centroid.

50:51

This green's a great distance is.

50:53

Or this is how distance? Or this is.

50:54

this point. And you can clearly see this point is closest to the red. So we will assign

51:00

this point to the red centroid. So assign every data point to its nearest centroid. Assign every data point

51:09

to its nearest centroid to form clusters. So we will assign this point to red. We'll assign this point

51:15

to red. You're able to see that color. That means all these points will be assigned to red. Let me do that

51:20

for you. I'll click on Go for a minute. When I do that, all this will be assigned to red.

51:24

All these are closest to blue and all these are closest to green.

51:28

When I hit go, you will see the assignment part is completed.

51:30

Step three completed.

51:32

Step three completed.

51:34

Now we go to step four.

51:36

Step four, we recalculate the mean.

51:39

Mean, means centroid.

51:42

And why are we doing that, guys?

51:44

Because remember, initially, we took the initial value of centroids.

51:49

Centroids were initialized randomly.

51:52

We randomly sentroids to randomly.

51:54

But centroids can be anywhere.

51:57

So actual centroid is this not.

51:59

So now we will recalculate the centroid.

52:01

So what is the new updated green centroid?

52:05

It will be somewhere here.

52:07

So if you recalculate the mean, the mean of the green will be somewhere here.

52:11

The mean of the red will be somewhere here.

52:13

And the mean of the blue will be somewhere here.

52:15

Sort of here.

52:17

So very interesting.

52:18

Once I click on this button, update centroid, step number four, when we're

52:21

take a look at this.

52:22

now we're able to see the story play out.

52:26

Now we go to step number five.

52:28

We'll repeat steps T and three and four.

52:31

Now we're back in three in chaletrymahe.

52:33

We're back in three in actually five is redundant.

52:36

I mean, so what it means is what it means is you are repeating, you're repeating three and four.

52:41

You will repeat three and four until the cluster center stop moving.

52:47

So now we will go back to step three once again.

52:50

So all these are data points.

52:52

This is the red center.

52:52

All these are points.

52:53

This is green centroid.

52:54

This is blue centroid.

52:55

So we will once again assign all these data points to the red centroid, whichever points it is closest

53:04

to.

53:05

So when I run the code now, what will happen?

53:07

You will see all these points will be part of red.

53:10

All this will be part of blue.

53:11

All this will be part of green.

53:12

Step three completed.

53:13

Step three completed.

53:14

Wapers and step four may get at re calculate the means.

53:17

There it is.

53:19

I hope everybody is with me.

53:21

And this is the part.

53:22

it ends. So we'll keep repeating steps three and four until the centers are complete.

53:27

Okay, Arnika, I hope you're clear with this now. What is going on? Okay.

53:31

I'm an one example. So we can see this one. So I will initialize seven clusters right now just to help you

53:40

understand what is happening. Take a look at it. There are seven clusters we have. There are seven

53:46

centroids we have initialized right now. Step number two. Step number three, we will assign every single

53:51

data point to its nearest centroid.

53:52

So we will find out the distance of every data point from its nearest centroid and we will assign

53:58

every data point to its nearest centroid. That is what we are doing now. And if I run the code,

54:05

you will see all these are part of, you know, violet. All these are data points which are part of

54:11

this thing. And just a second, guys. Just a second, please.

54:22

Sorry, guys. Sorry about this. So all, so now we will go back and you will effectively go back and try to assign every single data point as part of the nearest clusters. Step number three.

54:41

Then we're step number four. Step number four is recalculate the mean. Initial centroids were randomly initialized. Now when I update, look at this. Beautiful, right? See how.

54:52

in the problem.

54:53

Okay, don't worry. This will not work. But ah, ah, okay. See how it moved in.

55:00

Okay. Now, let me start from here. So, uh, where are we right now? We are in step number four.

55:08

Recalculate here. Now we will once again reassign. Reassign points. So all of these points are reassigned.

55:16

Step number four again, recalculate. Reassign. Reassign. Recalculate. Three, four. Three, four. Three, four. Three. Four.

55:22

four, three, four. You keep doing this over and over again until there is no further change in the centroids.

55:31

And once you have done that, you can confidently say that yes, we have the perfect positions of the centroids.

55:37

So our total data make, how many clusters were? Excuse me, they've got total seven clusters.

55:42

And we are also able to see the centroids of these clusters.

55:46

Right? I hope absolutely, all of you are absolutely clear.

55:49

Okay. Okay. Wonderful. Let us see one more very interesting.

55:52

one. So this is a nice animation. I wanted to share this with all of you so that people are able to

55:57

work through it. You guys can try this out also later. And another animation I wanted to share with you,

56:06

which is Shebelini. Okay. Okay. You can go here. Ah. This one. Ah. You can take a look at this. Very

56:22

and I will go ahead and just take you back a couple of iterations I'll do just a second guys

56:52

Okay. So everyone can take a look at it. First step, once again, we initialize. We randomly initialize four clusters, four centroids.

57:16

Initially, we don't know what the right positions of the centroids are. We just randomly initialize those centroids. That's step number one.

57:22

Step number two, we assign each data point to the nearest centroid to form clusters.

57:29

That is the second step that we incorporate.

57:33

Okay. It's a little slow. Just give me one second.

57:38

Still loading.

57:41

Step number one, we assign. Step number two. Now, step number three is going to assign nearest.

57:46

Assign the nearest points to the centroids.

57:49

Step number three. And now this is step number four. Recalculate the center.

57:52

Now, look, step number four will. Recalculate. Again, step number three, assign.

58:02

Step number three, assign. Step number three, assign. Then, step number three, recalculate.

58:10

Step number three, recalculate. Again, step number three, assign.

58:16

Step number three, assign. And step number four, recalculate.

58:22

so we keep doing this many many times until we get the best results okay and now we are able

58:31

to finally go ahead and we are able to go ahead and find out what the exact positions of

58:38

the centroids are okay we can do it one more time just so that we are clear what we achieved

58:44

so step one we initialize the centroid step two we assign every single data point to its nearest

58:50

centroid and step four we recalculate the centroids step four recalculate again step three assigned

58:56

step three assigned step three assigned step four recalculate again step three assigned step four

59:03

recalculate again step three assign step four recalculate and you keep doing this ever and over

59:08

again until we have the perfect positions of the centroids okay i hope everybody's aligned

59:13

so this is just to explain to you conceptually what k means clustering is what what go

59:18

how it's how it will be required because in python k means is one line of code

59:24

okay when we go back and do this in python k means is nothing but one line of code

59:29

you will just write a single line of code and all this will automatically happen behind the scenes

59:34

you sit you know initialize android you know uh assign nearest none of that you will have to do

59:39

you will just run one line of code k means dot fit all this magic will happen behind the scenes

59:43

okay now there is one other very interesting uh concept

59:48

i wanted to cover okay so now there is one other very important concept i have to cover which

59:57

is how do we choose the number of clusters you can just say number of clusters um

1:0:02

rest of the journey is very easy all of you followed that right everybody everybody

1:0:07

follow the rest of the journey once i define the initial number of clusters k

1:0:15

then we proceed with number two number three number four

1:0:18

repeat steps three and four whatever story we have discussed right the important thing now is

1:0:24

how do we start with step number one step number one care how we how our examples

1:0:30

the examples were very clear we were able to see visually that okay you know we are able to see

1:0:37

three clusters we are able to see four clusters so we made start to this is the key but how do you

1:0:45

determine the value of k k is the

1:0:48

that variable k that's why the name k means comes k means major the k stands for the

1:0:54

variable that number of centroid's that we'll say we're this many means k means if

1:0:59

three centroid so three means if there are four centroid's four means five centroid's five

1:1:04

means that's why the name k means that's why the name k means okay

1:1:08

kind of that we do using domain knowledge

1:1:13

for about you have to understand your domain you have to know what is

1:1:18

the problem that you're trying to solve what is it that you're even trying to do what is it that

1:1:22

you're even trying to achieve so part of your you know part of the solution will be coming from there

1:1:29

you have to you have to know what you're trying to do what you're trying to achieve right so

1:1:33

part of that will come from there and you will choose the value of k you will choose what is the

1:1:40

optimum value of k from there so find out what is the optimum value of k

1:1:48

based on domain knowledge the second strategy is the second strategy that we look at is we use

1:1:56

something called the elbow method and this is what i will talk about right now what is elbow method

1:2:01

and using the elbow method how do we find out the ideal value of k so i have got one slide of

1:2:07

my own which i will bring it up right now for you so there is the slide all if you can just

1:2:13

just give it a glance once please again just give it a glance there's a lot going

1:2:18

on i know but i think sometimes when you see something first and then i talk about it i think it connects

1:2:23

better so just just give it a glance for a minute okay so even sometimes uh even if you don't understand

1:2:29

anything just if you let your brain you know perceive this for a minute 30 seconds the human brain

1:2:36

has an amazing way to connect the dots you know you won't believe it but it's just a wonderful way

1:2:40

that the dots connect once you just see something even if you don't follow if you see something

1:2:44

the dots connect very nicely just just observe this for a minute and just try to

1:2:48

as fast as you can take a minute i will discuss what is elbow method and what is inertia i will

1:2:53

discuss it now why are we talking about this right now because we are trying to find out what is the

1:2:57

ideal value of k

1:3:18

you know.

1:3:48

You know,

1:3:50

You know,

1:4:20

Thank you

1:4:50

Thank you

1:5:20

Thank you

1:5:50

Thank you

1:6:20

if you take a look at it uh i think all of you're able to observe this you can you can see

1:6:42

very interesting the the scenario that you're considering right now the scenario that we're

1:6:49

considering right now is imagine this is the setup like this is the set of data points and we have

1:6:57

built a model with four centroids let's say we have we have built a clustering model with four

1:7:03

centroids we are able to see that right using the k means algorithm let's say we have taken a

1:7:09

value of k equal to four approximately and we have built a model with four centroids

1:7:14

centroid one centroid two centroid three we are first trying to understand that inertia

1:7:19

yeah what do we even mean by inertia right what is the meaning of inertia inertia is a kind of

1:7:24

error in a cluster whenever you do clustering the clustering also suffers from some kind of an

1:7:30

error so inertia is referred to the error in a cluster so the question is what is the inertia in

1:7:39

the cluster right now so whatever we are seeing on the screen what is the inertia in the

1:7:44

cluster that we are getting that is the problem that we are trying to solve what is inertia

1:7:48

so inertia stands for s a c c is nothing but sum of squared errors i repeat again inertia

1:7:56

stands for s s s c is nothing but sum of squared errors so first we calculate the error

1:8:06

then we square the error then we calculate some of the squared error so that is the way how

1:8:13

we do inertia right i repeat again first we calculate error

1:8:18

then we square the error and then we calculate what is the sum of the square

1:8:26

error so error is nothing but the distance of the data point from the centroid

1:8:31

then we square the distance and then we calculate the sum of the square distances

1:8:41

i repeat again first we calculate the distance of the data points from the centroid

1:8:46

what is the error how far is the point from the centroid

1:8:51

that's why i'm saying first one one

1:8:56

you find out how far is the point from the centroid

1:9:00

then you you square it up

1:9:03

second operation is square care care

1:9:05

third operation that's all squares sum

1:9:08

third operation is sum

1:9:10

so as you can't here here on error is nothing but d1

1:9:16

is the distance of the point from the centroid d1, d2, d3, d4, d5, those square terms

1:9:23

d1 square, plus d2 square, plus d3 square, this entire set of terms taken together is called inertia.

1:9:31

And you can intuitively understand how we look at this whole thing, you can intuitively understand

1:9:40

the you know, the whole idea in this particular context.

1:9:46

Take a look at it. So, the more the inertia, the more the error, we can say that lower the quality of the cluster.

1:9:58

Because if inertia is much, that means what? That means you did not do the clustering correctly.

1:10:05

Quality of a good cluster is that data point should be as close to the cluster as

1:10:12

possible. And this is a very important thing that we are trying to achieve in clustering.

1:10:17

We are trying to build a distinct and compact clusters. Clusters should be compact. So a very

1:10:25

large inertia means it is not good. Because all this while I'm trying to explain to you what

1:10:32

is inertia. S-S-S-S-E. First error, distance of the point from the centroid, error, knock-o, square-carro-s-s-s-s-sum-caro,

1:10:37

right? Now, let's come to Elbow method. Here, I am trying to show you with respect to.

1:10:42

to us to four centroids right now think about it this way how will the story look like if

1:10:48

i had a single single centroid let me take a little bit of space here and uh draw this diagram for you

1:10:59

here okay just a second guys let me let me let me take this up here this one

1:11:12

can relate to it. Now take a look at this all of you. So, uh, same set of data points I'm

1:11:24

having right now. Nothing changes the same set of data points we are having. Now,

1:11:29

look here here, uh, I have these set of points here, right? I have these set of points here

1:11:37

and I have these set of points here. I'm trying to keep it very basic. Okay, and I have these set of points here.

1:11:42

I'm four set of points here per data. So we are able to visually see how many clusters,

1:11:47

right? Whatever. Now, let's say for a minute that while solving the problem, I'm saying that,

1:11:53

hey, I have only, I'm trying to only build a single cluster of the whole data. If I do that,

1:11:59

if I do that, if we're all data points for a single cluster in, do you think this will be a good clustering?

1:12:05

Answer is no. The reason being that the moment you calculate the inertia,

1:12:09

you have this inertia calculate the moment you start to calculate the inertia distance of the

1:12:16

point from the centroid distance of the point from the centroid you try to find out the distance of

1:12:20

every single point you try to find out the distance of every single point from the respective

1:12:26

centroid how far is this from the centroid how far is this from the centroid how far is this from the

1:12:32

centroid you try to find out the distance of every single point from their respective centroid

1:12:36

that is what we are trying to do so we try to find out the distance of every single data

1:12:42

point from their respective centroids and if you do that the error the error a distance

1:12:48

square when you try to find the error you will realize that the error will be extremely large

1:12:53

so that's why we say huh that's that that's why we say that the inertia when k is equal

1:13:02

to one is extremely high now look you this one of the plot he whatever

1:13:06

i have tried to show you here i've clearly said that whenever the number of clusters is equal to

1:13:10

one the inertia is typically very high and intuitively speaking the extreme is k equal to one up

1:13:19

but the one extreme is that for all these data points you have a single single centroid

1:13:29

the other extreme that we have is for every data point you have only one centroid

1:13:34

every data point of every data point you take you will have only one centroid

1:13:41

now in that kind of a scenario what will happen if the number of clusters are too many inertia

1:13:48

will tend to zero because the data point and the centroid will be the same then the distance

1:13:53

of the point from centroid will be zero there'll be no distance so these are the two extremes

1:13:58

i wanted to talk about on one hand if your number of centroid is equal to

1:14:04

is very less if you have only one centroid one cluster inertia will be very high

1:14:12

on the contrary if you have many many clusters inertia will be very low it will drop drastically

1:14:17

we are trying to find out that elbow but now what is the point where it flattens out

1:14:25

where the rate of drop reduces so for example for this beautiful example you can take a look at it

1:14:33

when inertia value was equal to one when inertia was equal to one the sorry when number of

1:14:38

clusters was equal to one one cluster for the inertia was very high when you go from one to two

1:14:46

cluster inertia has reduced a lot when you go from two to three cluster inertia has reduced a lot

1:14:54

and when you go from three to four cluster inertia has reduced a lot

1:14:57

But we're going to be able to see four clusters what it means.

1:15:02

That means as we go from one cluster to two cluster, two cluster to three cluster and three

1:15:07

cluster to four cluster, as we go from one to two, two to three and three to four clusters,

1:15:14

we are able to clearly see that as we reach four clusters, the inertia has kind of become very less.

1:15:27

inertia has kind of become very less now so so as we get to four clusters inertia has become

1:15:35

very less so 4 to 5 5 to 6 you can see is kind of stagnating so there is no meaningful

1:15:41

reduction of inertia from here onwards that we are getting right now so from here onwards

1:15:46

there is absolutely no meaningful reduction of inertia that is happening so this is what we call

1:15:51

the elbow this is the optimum number of centroids

1:15:53

okay one say like a two two say three three say four the center inertia has reduced a lot

1:16:00

as you go from one cluster all the way to four clusters inertia has reduced drastically up to

1:16:05

four clusters here onwards as you go from four to five five to six six to seven

1:16:11

there is no noticeable reduction of the inertia because there is nothing must to achieve

1:16:16

think of it that way so this is how we find out the optimal value of k

1:16:23

will be domain knowledge domain knowledge is where we let's say if you are doing customer segmentation

1:16:27

you're part of amazon so you already have a leadership mandate leadership team or your management

1:16:33

team has told you you know uh in in in in the context of how they want to do customer segmentation

1:16:41

so the leadership team has already told you so then you already know what value of k to work with

1:16:46

otherwise we will do something called inertia elm method a very good question uh you know gurtec but here also

1:16:53

good take what you will have to do even if it is evenly spread you will have some bend you'll

1:16:56

you'll be still be able to see some bend it'll be approximate so there'll be some cases where two

1:17:01

clusters and three clusters there'll be a kind of a bifur you know very close call but you can take any

1:17:07

one of them and you know the most important part is most important part of unsupervised learning

1:17:13

is there's no output there's no output you're completely going by your intuition you're

1:17:18

completely going by your what you think is right because there's

1:17:23

there is no ground truth data to evaluate against so that's why i started my session by saying

1:17:29

that in clustering and unsupervised learning you are learning in an unsupervised

1:17:34

way nobody is supervising you there's no actual ground truth output you have so in

1:17:40

regression classification we had our test data in unsupervised learning there will be no concept

1:17:46

of test data so these are only guidelines that we are using to help us form the right number of clusters

1:17:53

you can absolutely use your own intuition and domain knowledge to find the clusters so what are the

1:17:58

steps we talked about step number one uh use your domain knowledge or use the elbow method to find

1:18:03

the optimal number of cluster what is the point at which we are getting the bend so clusters one two

1:18:08

clusters two clusters two inertia has reduced three to four it has reduced three to four it has

1:18:12

reduced up to cluster four inertia has reduced a lot up to cluster four inertia has reduced a lot

1:18:21

there onwards it is stagnant

1:18:23

so we are able to find out that bend so four centroid is the optimal number of clusters

1:18:30

optimal number of clusters is four

1:18:34

number of clusters increases inertia decreases it will always happen on because I

1:18:40

told you that if the number of clusters equals the number of data points

1:18:43

inertia will become zero other if every data point is like a cluster

1:18:49

inertia of zero you can there will be no distance from the centroid distance

1:18:53

centroidi data point so inertia will be zero so the only thing is that

1:18:57

shuru in the decrease very much more one to two two two two three three to

1:19:02

it'll be a huge decrease but then once you reach four centroid you go from four to five

1:19:06

centroid you here here if we've another one more centriads

1:19:08

added we'll not see a drastic reduction it will reduce very slightly so we are trying

1:19:14

to reach we are trying to choose that point where the rate of decrease has dropped the

1:19:18

most okay so that is how we choose the value

1:19:23

of k and on the basis of that we will go back and do the k means and we can find the clusters we will

1:19:29

see this in python code right now and end in jake we can go back and interpret the clusters

1:19:34

we're gonna clusters one clusters two clusters three whatever uh clusters we end up creating

1:19:41

we can go back and interpret those clusters in a nice way what those clusters really uh even

1:19:46

refer to okay so now we will take a look at the code and this is what is called the elbow method

1:19:51

by the way so now we will see the code and we'll try to understand intuitively what uh how to do k

1:19:57

means so the code is very simple as i told you there is no concept of test data here

1:20:02

so it is only training data you just take the whole data as it is and build clusters on it

1:20:07

there is no test data there is no output data remember this is very important unsupervised learning

1:20:11

we don't have any actual outputs to evaluate against and there is no test data here

1:20:15

okay all right so now uh we will continue on with some code

1:20:25

so guys i think we can take a break now right so i think it's is nine 10 on the clock so let us

1:20:30

quickly take a break let's take a short break in the session so i will see you back after the

1:20:35

break the agenda would be to take you through the code so we'll see the code snippet with

1:20:40

respect to what is uh clustering uh k means clustering k means clustering example

1:20:45

take okay after the break and from there we will discuss a very very interesting

1:20:50

use case of what is referred to as pca okay so that is going to be what we will discuss

1:20:55

after the break okay all right so i'll see you back after the break then

1:21:15

you know.

1:21:45

You know,

1:22:15

You know

1:22:45

I'm

1:23:15

I'm

1:23:45

I'm

1:24:15

I'm

1:24:45

I'm

1:25:15

I'm

1:25:45

You

1:26:15

Thank you.

1:26:45

Thank you.

1:27:15

Thank you.

1:27:45

Thank you.

1:28:15

Thank you.

1:28:45

Thank you.

1:29:15

Thank you.

1:29:45

Thank you.

1:30:15

Thank you.

1:30:45

Thank you.

1:31:15

Thank you

1:31:45

Thank you

1:32:15

Thank you

1:32:17

Thank you

1:32:19

Thank you

1:32:21

Thank you

1:32:23

Thank you

1:32:25

Thank you

1:32:27

Thank you

1:32:29

Thank you

1:32:31

Thank you

1:32:38

Thank you.

1:33:08

Thank you.

1:33:38

Hi, everybody, welcome back.

1:33:48

Hope all if you're back from the break, we'll start with our hands-on exercise right now.

1:34:08

So, guys, quickly, let's start on with the hands-on implementation of K-means.

1:34:26

So we have gone over K-means.

1:34:27

We have talked about some very interesting use cases with respect to how unsupervised learning works.

1:34:33

We talked about what is K-means.

1:34:34

We talked about the algorithm of K-means.

1:34:37

So first we find that.

1:34:38

out what is the value of K. We use something called the Elmo method to find out the optimum

1:34:42

K. And then we'll go clustering k means clusters. So we'll take a very small sample

1:34:47

data set right now and we'll try to go over k means using that particular sample data right

1:34:54

now. You can see. So I've used a sample data here right now and this is the code that we

1:35:02

are using to basically find out the optimal value of k. So what are

1:35:08

we are we doing. There is a term that we use called WCSS. So in my session, in my notes,

1:35:14

I was calling it inertia, but there is another term that is used called WCSS. So in case you get this,

1:35:19

you are asked this particular question. Just remember that inertia is nothing but WCSS within cluster

1:35:25

sum of squares. That's what inertia kater. Whatever I was calculating all this while, that is nothing

1:35:29

but your within cluster, sum of square, that's ikam inertia khae. Just to clarify that for all of you.

1:35:35

So anyways, so we want to actually find out the innerity.

1:35:38

for this entire range of cluster. So we will run a for each loop from 1 to 11.

1:35:44

What it means is that we will start with k equal to 1, k equal to 2, k equal to 3. We'll go all the

1:35:50

way to k equal to 10. So we'll start from k1, k2, k3. We'll go all the way to k

1:35:56

equal to 10. And we'll find out that for all the different different values of k, what is the

1:36:02

like considering all these values of k, what is the best value of the clusters we are getting?

1:36:08

so that is the problem that we are particularly trying to solve right now so what is the

1:36:11

optimal value of k is what we are trying to find out just to clarify so optimal value of k is what we are

1:36:17

again trying to evaluate and find out here okay hope everybody is aligned now so we take 4k and this

1:36:27

is the code for doing k means we are building the clusters using k means dot fit and very very

1:36:34

interesting if you remember all our machine learning conversations until now we were all

1:36:38

doing model dot fit x comma y how we always model dot fit x comma y

1:36:43

but remember in clustering there is no concept of y so that is why we will always do k

1:36:48

k means dot fit of x so we will not do dot fit of x comma y so we are taking k

1:36:53

k values different different k values we are finding out we are fitting the k means model

1:37:02

we are finding over the inertia inertia underscore k

1:37:05

kind of inertia we're we're automatically this is getting calculated and this is how the plot will

1:37:09

look like right if i just go and run this code i'll just go and execute the code you'll be able to see

1:37:16

how the elbow method basically looks like and i think this is very clear in this example

1:37:21

that when the number of clusters is equal to one the inertia is extremely high

1:37:26

when the number of clusters goes down from one to two the inertia has reduced kaffi

1:37:31

kaffi reduced kaffi and as the number of clusters goes from two to three inertia has

1:37:35

has reduced even further so we are able to see that as the number of clusters have have have

1:37:41

increased from one all the way to three we have reached the optimum number of clusters so so so what you

1:37:50

are able to see right now is the optimum number of clusters three is the optimum number of clusters

1:37:54

that we are getting and then as you go from three to four four to five five to six it kind

1:37:59

of stagnates there is no further improvement it's final it kind of stagnates so that's the way how the

1:38:05

k-means clustering is happening and using this we are able to find out what is the optimum value of

1:38:10

k three is the optimum number of clusters once we find that the other step

1:38:16

what is you know how you know kind of the optimum number of clusters three

1:38:22

after we are taking k means n clusters equal to three now we are applying k means with the

1:38:28

optimal k value equal to three so first you find out what is optimal k

1:38:32

after that the optimal value of k means go so now we are taking uh n clusters equal to three

1:38:41

and we are doing kmines dot fit of x and we are predicting the centroids so this is like one line of

1:38:49

code so you don't have to manually do this thing because the algorithm is taking care of all the things

1:38:53

for you so whatever we talked about step one step two step three that internally

1:38:56

go there that dot fit method in the end result the end result of what we are able to get is

1:39:03

if you have a dataset like this imagine this is your feature one and feature two if you have a

1:39:08

data set like this feature one and feature two which is what we have taken and we can put any story behind

1:39:13

it we can consider uh imagine this is the amount of time spent and let's just say this is the amount

1:39:20

of money spent so we have the amount of time spent and the amount of money spent we have how much

1:39:25

time spent how much money spent this is what we have right now overall so every row stands for

1:39:31

one customer and for every customer we have the amount of time spent and we also have the amount of

1:39:36

money spent for each and every customer how much time and how much money spent we have done the clustering

1:39:43

and now these are the cluster labels that we can identify this is the end result of k means so we can say hey

1:39:48

you know this is not the output you output these are the features originally which was there

1:39:52

your features they have k's there right what we started

1:39:55

our session with today you have got x and on the basis of that you formed clusters and these are

1:40:00

only the cluster labels but whatever groups we are able to see we as you can say these are customers

1:40:04

who are part of group zero these are customers who are part of group one these are customers who are

1:40:08

part of group two all these are customers part of group zero all these are customers who are part of

1:40:14

group one and all these are customers are customers who are part of group two so that's the pattern that we

1:40:17

are able to spot overall so customers part of group zero customers part of group one customer customers part of group

1:40:23

too so these are the patterns that we are able to spot right now overall and that's the idea

1:40:28

that we are able to you know overall understand okay i hope everybody's aligned everybody's

1:40:34

kind of getting a sense in terms of what this is uh what the basic concept of clustering

1:40:43

basically is here okay and the final step of k means clustering just as you

1:40:48

you have made clusters made final step what will is interpretation of the clusters

1:40:53

so you did customer segmentation you've got

1:40:55

you know that customers cluster zero

1:40:59

is this is cluster one

1:41:02

means this is clusters two

1:41:03

so i can show you visually to help you understand better

1:41:07

so you can go back and look at the diagram and now you can put a story behind it

1:41:11

you can say like if we say if we say this is x-axis

1:41:13

take no time and your y-axis money

1:41:16

so now you can go back and say

1:41:19

hey these are customers who are spending less time and less money

1:41:22

but these are customers who are very low engagement customers

1:41:25

all these are very low engagement customers

1:41:27

so they are customers spending very less amount of time very less amount of money

1:41:31

they are low engagement customers

1:41:33

so what these customers are not investing in amazon

1:41:38

they are not spending time they're not coming to the website

1:41:40

who browse not are they're not buying not right

1:41:43

whereas if you look at

1:41:46

these kinds of customers you're actually here here

1:41:49

there's not clustered not but this is kind of the average

1:41:51

these are customers who are spending a lot of time

1:41:53

so they are browsing a lot on amazon but ultimately they're not buying that much

1:41:57

that's also a very interesting group and you know this is the kind of

1:42:01

analysis brands actually do

1:42:03

one is okay okay you have you have customers' data have

1:42:07

you're clustering kia and but what after that

1:42:11

there there has to be a business objective to whatever we are trying to achieve

1:42:16

right so the end result is

1:42:18

we're saying who are my customers that's what we call it customer segmentation

1:42:23

and clustering is a big part of it so now we can say these are customers who are spending

1:42:28

lot of time but average amount of money and these are customers who are spending

1:42:31

average time but a lot of money i think i think this is the category everybody wants

1:42:36

but time what if you say that you say that you uh retail physical store

1:42:41

can't right so lot of people will just go to the physical store

1:42:44

that store in goomahs up the store waller said

1:42:47

then what went of shopping nobody wants them right but the best customers are those

1:42:54

customers who store may go they take two minutes two

1:42:58

questions they take the item they buy and go so they spend less time but they might more money

1:43:02

so all brands like them right so think about it that way that is also a very interesting and

1:43:07

maybe you know maybe what the companies can do is now that they are able to see hey this is

1:43:11

is a group of customers who are spending a lot of money but they are spending less time in

1:43:15

my store so maybe i will identify these customers.

1:43:18

we'll this kind of loyalty card system we'll

1:43:21

start in our store and maybe next time i will give them some special service

1:43:26

so next time when they enter the store you know we will have some people standing at the

1:43:29

store you know who will say sir great to see you back again we will assist you because you know that

1:43:34

they will not be there for much time so you will have somebody assist them and maybe you can make them

1:43:39

buy more cross-selling upselling you know we have those terms right so uh so this could be some

1:43:44

very interesting strategies that you can use to target your customers in a in a better way okay

1:43:49

this is the business context of what i want to talk about here

1:43:54

so this is uh and there are a lot of other very interesting data sites which i as i keep

1:43:59

sharing this in my classes and i encourage you so i have discussed uh you know a general

1:44:05

sample use case with all of you obviously this will be part of your other classes as well you

1:44:09

will do another session hands-on session uh you know uh but then yeah i mean do do do do

1:44:14

refer on to these data sets we have i've given a credit card data set for you as reference

1:44:18

data from gaggle it's a good uh very nice data set and you can actually find groups and clusters

1:44:23

of uh you know customers okay so very very interesting so whatever i discussed in the session

1:44:30

was like uh customer data from a retail domain this is customer data from a credit card domain and banks

1:44:36

are actually doing it every row will be a customer your customer

1:44:40

details puttow right this is very similar to the use case very yesterday you see i credit card

1:44:45

volume you have your customer uh credit limit

1:44:48

payment history

1:44:50

pata hube payment status

1:44:52

payment amount

1:44:54

on the basis of that you can build a profile about the customer you can do clustering on it

1:44:59

yesterday we were solving this like a classic sorry monday we were solving this like a classification

1:45:05

problem

1:45:06

but now you can also solve it like a clustering problem you can find out groups and clusters of

1:45:10

customers spotify's data set o'gia you can find groups and clusters of music data

1:45:14

you can find groups and clusters of music so this could be some very interesting use cases

1:45:19

that people can work on okay just wanted to give you some references

1:45:24

which one um where we can look it up actually that's a that's a that's a good question

1:45:36

apparently even i have that question but i was just trying to go back to the website

1:45:43

and it turns out that data set they have removed a valid question there i i take your point

1:45:48

i've taken it from caggle but when i go to caggle right now turns out that they

1:45:54

have removed this data set okay so now so okay i think i'll you can update the spotify

1:46:00

data one more way to find out the uh the caggle data is if you take a look at it one more way to find

1:46:08

out a caggle data sets is you can directly go and search you're

1:46:11

search for spotify data and you'll be able to see the spotify datasets click on data search

1:46:17

search with data sets and this is a good way to identify the data sets here so this is

1:46:22

the data sets that you will find and and always try to solve by let's say relevance and you'll

1:46:27

usually be pointed to some of the top data of spotify okay you're your music data

1:46:32

50 songs data have top spotify songs and what is the problem we are trying to solve you

1:46:36

here here clustering kind of relationship is a music is determined by its features

1:46:42

all this when we were talking about customer level data here here here we

1:46:45

it will be audio music singer who are genre what is the song duration um there'll be some

1:46:53

other audio related features how many beats per second beats per minute whatever you know bass

1:46:58

treble we can talk about audio features and all that and all that you're trying to do is you are trying

1:47:03

to find out groups and clusters of similar songs so whatever story we were discussing with

1:47:08

respect to customers um customer segmentation about karet right we are trying to find clusters of customers now we

1:47:15

we can relate a story to clusters of songs find out the clusters of similar songs

1:47:20

java station play and you might have seen this thing that you go to spotify or amazon prime

1:47:26

music and you start a station to kha borg they're basically starting with one music and they are

1:47:31

trying to play similar music it's a beautiful application of clustering so they already have

1:47:36

clusters of similar songs with similar attributes and all that they're doing is they're playing

1:47:41

all those from the same station that's the way how it looks out

1:47:44

when you click are play similar music play similar song that similar

1:47:48

how's somehow because it's part of the same cluster lowest distance

1:47:51

you're playing a song play in the song which has the least distance

1:47:56

that song your next play over next Netflix maybe going to go

1:47:59

so i was talking about recommendation in the initial part now you can relate to it

1:48:03

Spotify in clusters of songs and Netflix in Netflix

1:48:06

clusters of movies are you're a one movie

1:48:08

you're looking at Netflix by the other recommendation

1:48:10

because that movie closed is part of the same group

1:48:12

okay everyone's able to relate to it

1:48:15

shall

1:48:17

so now we will get to the other

1:48:20

core piece which is called

1:48:22

PCA so PCA

1:48:24

we'll make a contextual

1:48:24

understanding what PCA basically

1:48:27

stands for what exactly is PCA

1:48:29

okay we'll see that in a minute

1:48:42

so before i talk about that there's a very nice kind of a animation that i wanted to

1:48:50

share with all of you right so this will be a great kind of a context before i start my conversation

1:48:57

so PCA is again a very very interesting topic and what we are trying to achieve in this

1:49:02

particular session is to give you the contextual understanding of what pCA actually stands for

1:49:08

so what is pca what pca actually refers to so that is what we are trying to understand to

1:49:12

to understand in this particular leg of the session what what pca basically means

1:49:16

what exactly is what we are trying to see okay and mostly the focus will be more on some

1:49:22

coding because on code way a code snippets we'll try to understand from a practical

1:49:26

perspective how you know PCA can be done in terms of the code so that is what we'll try to

1:49:31

focus on in this particular leg of the journey but before i do that let me play a small

1:49:36

very nice kind of a you know a video

1:49:42

for all of you so i'm just going to take a minute and play that video for everybody so all of

1:49:48

you are able to get a contextual understanding of what is the topic that we are trying to learn right

1:49:56

now okay so this is also a very deep mathematical topic so the focus of the class is not on the

1:50:01

math part uh we share sound aria so very nice share sound did not use to work before

1:50:07

surprisingly uh today i'm able to share the sound which is

1:50:12

is very nice yeah let me play this uh play this for all of you listen in sit back

1:50:20

all of you listen in so i'll just be pausing for three minutes listen to the video and i will

1:50:26

start the conversation uh post the video okay okay everybody listen in please

1:50:42

I'm Daniel. Hi, I'm Martin. Hi, I'm Fernanda. Machine learning is pretty complex, so we've

1:50:51

been experimenting with ways to visualize what's happening. There's a core concept in machine learning

1:50:58

called high dimensional space. Here's one way to wrap your head around this concept. You can think

1:51:04

about people as being high dimensional. For example, take famous scientists. You can think about when

1:51:11

they were born, where they were born, their fields of study. Each of these is like a

1:51:17

dimension of that person. These dimensions become difficult to untangle when you think about different

1:51:23

people because someone might be similar in some ways, but very different in others.

1:51:29

But this is the kind of thing you can use machine learning for. With machine learning, the computer

1:51:35

isn't told the meaning of these dimensions. It just sees them as numbers. And it sees each set of numbers as

1:51:41

as a data point. But by looking across all of these dimensions at once, it's able to place

1:51:47

related points closer together in high dimensional space. Here's a concrete example where words

1:51:54

are treated as high dimensional data points. The important thing to remember is that we haven't told

1:51:59

the computer the meaning of words. Instead, we've shown at millions of sentences as examples of how

1:52:05

words get used. Here is a visualization of the results. We're looking at a substance. We're looking at a

1:52:11

subset of words that the computer has learned about. Each dot represents one word.

1:52:16

Each word is a data point with 200 dimensions. Using a technique called TISNY, the computer

1:52:23

clusters words together that it considers related and clusters form based on meaning, even though we've never

1:52:30

thought it the meaning of words. Here is a cluster of numbers. Months of the year. Words related

1:52:37

to space. People's names. Cities.

1:52:41

and so on. We can also look closely at smaller sets of words. If we search piano,

1:52:48

we can run Tisney only on words related to piano. We get clusters of composers, genres,

1:52:54

genres, musical instruments, and more. And this approach doesn't just work for words. For example,

1:53:02

you can also treat an image as a high dimensional data point. Here's a data set

1:53:07

where lots of people wrote digits between zero and nine. People

1:53:11

write in all kinds of ways. So the question is, instead of us needing to manually code rules

1:53:17

for all the ways people write, could a machine figure it out itself using machine learning? Each image

1:53:24

is 784 pixels. The computer treats each pixel, as it's mentioned. Again, using T SNI,

1:53:32

it clusters these images in a high-dimensional space. We've color-coded them so that it's easier for us to see

1:53:39

what's going on, and you can see groups of digits clustering together. It's learned something

1:53:45

about the meaning of these digits. These visualization techniques we've been exploring can be

1:53:52

useful for all kinds of things. That's why we're working on open sourcing all of this as part of

1:53:58

TensorFlow, so that anyone can use these tools to explore their data.

1:54:06

Okay guys, so, uh,

1:54:09

I think you got a sense of the video, okay? So I'm going to talk about it and though some

1:54:16

parts of it are not so related. I get it images and text was something very different. In fact,

1:54:22

I think towards the portion where we started talking about text, so text was not really related,

1:54:29

but this is exactly the kind of thing that you will talk about, you know, when we come to agents and

1:54:34

embeddings and all that, you will get a better idea of it. But what we really wanted to

1:54:39

to focus on in this particular demo is how data is, I'm sorry, data is inherently high dimensional.

1:54:50

So how data is inherently high dimensional.

1:54:56

If your high dimensional data have, then you have it, like, Mary Curie, you have a person.

1:55:02

Dimensions, what do you mean by dimensions? It means features. And if you, if you, you,

1:55:08

So, look at all the kinds of use cases we have seen so far.

1:55:14

Monday class let's talk about Monday session.

1:55:17

We have credit card data set, right?

1:55:20

Every row was a customer. We have customer credit limit.

1:55:24

Customer credit limit. We have customer payment amount. What is the customer payment amount?

1:55:29

What is the customer balance? What is the customer balance? Credit balance. All these are the different,

1:55:36

different features of the customer.

1:55:38

And based on the different features of the customer, we are trying to find out

1:55:43

what are the groups and clusters of customers. That's the problem that we are trying to solve.

1:55:49

Okay, so first is that your customer's there were so many features. I think they were close to 30

1:55:56

features. Every customer had 30 features. Balance, balance for different months, right? These features

1:56:02

now the point is, it is very difficult to visualize that kind of data.

1:56:08

Feature, feature, if you go back to the introductory machine learning classes we did,

1:56:14

what is a feature? A feature is a dimension. A feature is a dimension. A feature is an attribute.

1:56:19

X is a dimension. It's a dimension of the customer. Every row was like a credit customer,

1:56:25

right? Credit card customer. This customer's customer data that we've seen last week

1:56:28

in UCI credit card. If you, sorry, Monday, it's a high dimensional data because this data has

1:56:36

lot of dimensions, lot of dimensions. You talk about the California housing data set.

1:56:42

We've seen in California housing in regression case study last week. And if you remember in California

1:56:48

housing, every row was a house or a district in California with many features, many dimensions.

1:56:56

We had the population, household, median income, sorry features, high dimensional data.

1:57:03

The point is you cannot visualize this kind of data.

1:57:06

So, what if the need arises for us to visualize this kind of high dimensional data?

1:57:13

We're how we can't. And that is exactly where the concept of PCA comes in at a high level. This is

1:57:20

where the concept of dimensionality reduction comes in. So, this is the first we

1:57:25

this terminology is just to understand. That X is nothing but a feature. This is the term that we have

1:57:30

been using all this while. And today particularly, I'm using the term called dimension.

1:57:36

Dimension is another term that we associated with it.

1:57:39

So we say, what are the dimensions of the customer?

1:57:42

What are the dimensions of the house?

1:57:44

What are the dimensions of the, you know, iris flower?

1:57:49

What are the dimensions of the patient?

1:57:53

Something like that.

1:57:56

And if a data set has too many dimensions, it becomes very difficult to visualize.

1:58:01

We must go do, though, access, in place, so what we do in that case?

1:58:06

what is that we do in that case is we go back and use something called PCA at a high level.

1:58:13

We do something called dimensionity reduction.

1:58:16

So we have these dimensions, we represent all these dimensions.

1:58:20

We represent the whole data only in the form of two dimensions.

1:58:24

Two or three dimensions. At a high level we can talk about two.

1:58:28

Now the moment you do that,

1:58:31

those credit card customers there,

1:58:34

which had 30 features there.

1:58:36

Now we are saying we don't just have 30 features, we have only two features.

1:58:41

And now all of a sudden I can plot them in a two-dimensional surface.

1:58:46

That's the big picture idea of what dimensionary reduction is.

1:58:49

And that is basically what the author was talking about in the video today.

1:58:53

Here PCNI, here here T-Snee, an advanced technique they were talking about.

1:58:56

If you remember in the video they talked about T-S-S-Ni, the story is the same.

1:59:00

What they were doing was the same.

1:59:02

You have a very high-dimensional data.

1:59:03

data.

1:59:04

Here, words are treated as high dimensions, very high dimensional data.

1:59:07

And here we have basically kind of tried to reduce that into clusters of similar words.

1:59:14

Okay?

1:59:15

So you can see what these are similar words that we are getting.

1:59:18

Okay, high dimensional space.

1:59:21

And the same way we have done this for digits.

1:59:24

Images.

1:59:25

So we have done PCA on the image data and this is what we are getting.

1:59:28

And if you want to, there's a very nice website you can kind of kind of,

1:59:32

kind of refer to. Let me show you this thing. What is that? Visualize, visualize

1:59:39

high dimensional data. So let me share this link with you.

1:59:45

This is experiments with Google. It's a very nice website. People can refer to, okay?

1:59:53

And you can go here. And here is also the video you will find and you can click on launch experiment.

1:59:59

And the moment you click on launch experiment, you'll be able to see that animated.

2:0:01

be able to see that animation live on your browser.

2:0:04

So don't try to get too deep into it because these are again very unrelated topics for today's session.

2:0:09

But I think just to help you with that overall end-to-end understanding where the dots really connect.

2:0:15

So this is what they showed in the video.

2:0:17

So this was the Amnist data with images that we took. So these are all the pictures that you are able to see.

2:0:23

And we have done PCA on that. But the image is the high dimension.

2:0:27

The author in video in the video. Every digit is a thing.

2:0:31

collection of 784 pixels. If you remember, 28 cross 28, they don't know, right?

2:0:35

If you remember, so 784 dimensions. Can you believe it?

2:0:39

Monday's class in we have just these features. Now we are talking about 784 features.

2:0:45

How cool is that? Now 784 dimensions don't plot. So what we have done? We have taken those

2:0:53

784 dimensions. We have taken those 784 features and we have kind of tried to compress that information

2:0:59

into only three dimensions to give us this beautiful kind of visualization.

2:1:04

And that's what PCA does. That's what dimensionary reduction does.

2:1:07

You can see very interesting, very interesting. The ones are all very similar. Can you see all the ones?

2:1:13

You can actually literally zoom in and see. Now, look, these are all ones here here. All the ones are

2:1:17

clustered in a similar way. These all ones here here. And it's 3D. You can it. You can't see

2:1:23

where they're clustered here. So these are all clusters of ones here. So we have. So now, how all

2:1:29

all of a sudden we can visualize our data in a very nice way. Every digit is 784 dimensions, right?

2:1:36

We cannot plot it, right? So what we have done is we have done PCA.

2:1:39

We have tried to somehow compress that information that is present in 784 dimensions into only three dimensions.

2:1:47

Here actually, three dimensions. If you're, if you're a little zoomed and you look at, this is an axis, PC1,

2:1:52

is. This here here here here here here is actually.

2:1:55

This is your PC2, green one is. And here here one more will, PC3, blue one.

2:1:59

I think, I think, too, see the clusters. But you can start to very nicely see the clusters.

2:2:05

These are clusters of three, clusters of, okay? So that's the, that's the basic way how it,

2:2:10

how it works out. So this is the general idea behind, how it is doing behind the scenes.

2:2:16

Sir, you can change. Basically, you can go back and take it in 2D as well.

2:2:22

Two D in the, but you can get an idea in terms of how the, you know, how the clusters are actually

2:2:28

getting formed intuitively.

2:2:29

Okay? Now, just to come back to the theory of dimensionality reduction, what it is, basically,

2:2:38

as I told you, in a real world, your data will almost never have only two features, right?

2:2:43

So in the real world, your data will never, will not have only two features. In the real world,

2:2:47

your data will have 10, 50, hundreds of features, your data will, you know, in reality, your data

2:2:52

will have, right? That's the intuition. So in reality, your data will have hundreds of features.

2:2:58

Okay? So humans cannot visual.

2:2:59

lies beyond three dimensions.

2:3:01

And another very important thing I want to talk about is, in a real world scenario, if your number

2:3:06

of dimensions increase, other data in both are many features, if you go back to Monday's session,

2:3:14

random forest, beautiful topic we discussed, we've discussed, we made a critical point

2:3:19

there on called feature importance.

2:3:21

We had you, that if you have to, if you have lots of features, okay, if you have lots of features,

2:3:26

okay if you have lots of features, if you have lots of features in a particular

2:3:34

data set, then sometimes the information and the model quality will deteriorate.

2:3:42

Because there are too many features we'll be having.

2:3:44

So what we do in that case is we try to reduce the irrelevant features and we try to only select

2:3:52

the important features.

2:3:53

And that is another area where dimensionary reduction helps a lot.

2:3:55

It tries to kind of compress all those useless noise and tries to bring out the signal.

2:4:04

So if you have 100 features,000 features using the technique called PCA, using dementiaity reduction,

2:4:13

okay, it's a kind of a compression algorithm, which is the mathematical part we're not getting into.

2:4:16

That's not in the general scope, right?

2:4:18

But then the big picture idea is very important.

2:4:22

We try to retain as much.

2:4:25

information in the original data as possible. But at the same time, we try to reduce the number

2:4:33

of dimensions. And what is the benefit we are able to get? The main benefit we are able to get

2:4:38

is we are able to, one, reduce the data, reduce the size, at the same time, increase the improve the

2:4:46

performance of the model. It is like a win-win situation. So that is the big picture idea behind

2:4:52

what dimensionity reduction is. So we can look at a real scenario, a real use case.

2:4:58

So what I've done is I've tried to simulate our data for you, all of you. You can see.

2:5:05

This is a small simulation data you can see on the screen. Feature 1, feature 2, feature 3,

2:5:11

feature 4. Our feature does take here. There are 10 features we have taken. And you can again

2:5:16

see that some of the features may be important. Some of the features may not be important.

2:5:20

So that is the way how we can look at the whole thing.

2:5:22

So some features may be important. Some features may not be important. That's the big picture idea. Okay.

2:5:30

So first step, we are using something called standard scalar. So first step, we are using something

2:5:37

called standard scalar. And after using standard scalar, we are going ahead and first step we are using

2:5:42

standard scalar and then we are going ahead and we are scaling the data. And then we are using the code

2:5:50

PCA and components equal to 2.

2:5:52

And this is the code. Just remember the code all of you. That's the focus area. Okay. And what will this do? It will bring down the features from 10 to only 2.

2:6:02

A Go ahead we have this data set. And whatever machine learning, whatever clustering, whatever problems we were trying to solve. We were working on the basis of this data.

2:6:13

Right? We were working only on the basis of this data. So we have 10 features. He was trained, test, split, he, model, all that.

2:6:21

Now what we are doing is, we are trying to compress all these 10 features into only two principal

2:6:27

components. And the big picture idea is that these two principal components will contain the major

2:6:35

information in my data. Most of the information of the data, all the core information in the data

2:6:43

will be present in these two principal components. Right? So all the core information will be present in these two principal components.

2:6:46

Right. So all the core information will be present in these two principles.

2:6:51

components that's the important thing so n components equal to two is what we are doing so in these

2:6:58

two principal components the main thing will be present and now we can of course do pcaa.fit transform

2:7:06

back to fit transform again the last time we talked about fit transform was when all if you remember

2:7:12

fit transform we've come discussed all the way when we were discussing about date of preparation

2:7:17

13th may all if you remember 13th may we were talking about uh one-not encoding

2:7:23

had encoding discussed khani remember scaling we've

2:7:26

we talked about fit transform there we talked about fit transform fit transform and then we

2:7:33

talked about leakage imbalance smote discussed kia okay so back to fit transform again so what it

2:7:39

means is even bca is a kind of a feature engineering technique this is the kind of a pre-processing

2:7:46

technique and that's what are right now actually we're going to

2:7:49

now. Now, look, our data as data set as a set as a

2:7:52

time, we are trying to take this data and on the basis of that

2:7:58

we are trying to create this reduced data set.

2:8:04

So in a way we have done feature engineering.

2:8:07

It's the best of both worlds.

2:8:08

So we have data to become

2:8:09

data,

2:8:10

data,

2:8:10

the number of rows will remain the same, but

2:8:16

The information, all the information across all these 10 features that we have,

2:8:24

all the information across all these 10 features that we have is now present in only these two

2:8:31

principal components. That is what we are able to see. So whatever information we have,

2:8:37

you know, in these, you know, three principal components, two principal components.

2:8:45

And now the best of the best.

2:8:46

part is that we can visualize the same story I was talking about before. So because we have only

2:8:52

two columns right now, now we can visualize our data. So imagine this is your housing data,

2:8:57

customer data, whatever, or your customer data, so you, you have visualized not

2:8:59

not you have this to visualize. So you have compressed the information into only these two

2:9:05

components. Almost all the information is contained. And now this is how the thing will look like.

2:9:13

So there goes PC1, there goes PC2. And you know,

2:9:16

Now you will tell me, in this data set, how good clustering will work beautifully on this data set.

2:9:26

In fact, we can continue the story. So today's agenda was clustering. So,

2:9:30

now we're what we're doing. So, what we'll do we can walk you through it. Original data was this.

2:9:36

We have taken the original data. We have done PCA, N components two.

2:9:40

Okay, and components two, we are trying to convert that into two components. And next,

2:9:46

Using the transformed data, using whatever transformed data I have, the transformed data is called

2:9:52

DF underscore PCA. This is your transformed data frame. Now using the transformed data frame,

2:9:58

now we're using the transformed data frame, now we're on this up on clustering

2:9:59

can. So, okay? So where is that? This is the thing. And now I will generate a new

2:10:06

cell and I will use a bit of Gemini. I will say, please use, please use DF underscore PCA. The

2:10:16

you know the data frame and based on the clustering logic in this code file please perform

2:10:46

And then, using the optimum K value, using the optimum K value, using the optimum K value,

2:10:56

using the optimum K value, please perform, please, uh, perform.

2:11:03

K means clustering.

2:11:06

Okay?

2:11:07

Shallo.

2:11:07

It's what we'll take how it's how it.

2:11:09

So, and I always like to say that, try to use a blend of AI in these sessions, right?

2:11:13

So because, uh, I think learning smart is always.

2:11:16

also very important, right? So that is a very, very important skill in today's world.

2:11:19

Sometimes people ask me, that, sir, AI, so everything is everything.

2:11:22

Yeah, AI, everything is, but if you know what to do it, then what can't do? At least you should

2:11:26

know the topic so that you know what to even type. So that is, so you have to build this blended skill.

2:11:31

Learning how to learn is a very important skill nowadays. You have to learn in a very smart

2:11:35

way. Okay, so don't try to learn in the age old 10, 15 years back, however we used to do things, right?

2:11:40

But you have to learn in a smart way. So get a broad idea of the topics. Understanding clear.

2:11:44

So, things, conceptually understand the things, and then understand it good enough, well enough,

2:11:48

so that you can, you're in a position to write prompts.

2:11:51

Okay, you don't have to necessarily memorize everything.

2:11:55

Okay, so code been here.

2:11:56

So this pay nothing to talk about.

2:11:58

Let me accept and run.

2:12:00

So everything is all go-gia.

2:12:02

I think we are able to clearly see that there are four clusters, four centroids right now.

2:12:05

It's very nice.

2:12:06

And this is the other benefit of PCA.

2:12:08

Once you do PCA, the clusters will become very prominent.

2:12:11

This is actually we are able to see that.

2:12:12

that, that clusters equal to one inertia was very high.

2:12:17

Clusters equal to two inertia is reduced.

2:12:20

Clusters free inertia has reduced further and clusters four inertia is very low.

2:12:24

And four, say five, five, six, six to seven, you can see it's almost stagnant.

2:12:28

So what does elbow method tell us?

2:12:31

We will basically take that particular value of K, which is kind of the elbow.

2:12:37

I mean, char to inertia has reduced a lot.

2:12:40

Charr after, inertia is not reducing much.

2:12:42

that is what is going on behind the scenes.

2:12:46

And here, your data, you can see.

2:12:48

Principal PC1, PC2, cluster labeled go here.

2:12:51

This is the same story we have talked about.

2:12:53

And here up herep, you can see if final centroid's how they look like.

2:12:57

So the last part is, now that you know that K equal to 4 is the optimum,

2:13:00

you run the K-means algorithm, you find out what those four centroids are,

2:13:04

and you label those centroids.

2:13:06

And you interpret those clusters, that's what clusters.

2:13:09

So that's the interesting part.

2:13:11

Okay?

2:13:12

So this is the big picture idea of how PCA helps you.

2:13:15

What is the benefit of PCA?

2:13:17

So understanding the benefit of PCA is also, you know, very, very important.

2:13:20

What, you know, benefit, you know, PCA brings to the picture?

2:13:27

So, this is a similar example.

2:13:29

This is our breast cancer data set.

2:13:33

This is the SK.L. Learn, I think, I think, a couple of times we might have taken it.

2:13:36

This we had last week be a one, a similar supervised learning context, we've seen.

2:13:41

And again, very similar supervised learning context, we've seen.

2:13:42

interesting. It's a data set which is having 30 features. There are so many features.

2:13:48

We cannot visualize it. And again, it's a great data set for doing PCA. So code is the same.

2:13:54

So you do PCA and components equal to 2. That means you want to reduce 30 dimensions into only

2:13:58

two dimensions. And then you want to go back and see visually that are we able to separate the classes?

2:14:06

So that's the that's the basic intuition. Okay, so this code can run. Let me just run the code. So this is a

2:14:12

default built-in data set we have already got let me show you how it how it works out.

2:14:16

So you're able to see and I think I think it's a very nice separation we are getting.

2:14:21

Very nice separation.

2:14:22

Now, look, 30 features' data set the original data set was 30 features.

2:14:27

And I have used PCA and reduce that down to only two dimensions.

2:14:31

Like I'm here here the resultant data, there's only two dimensions.

2:14:34

But that basis, we are able to do machine learning.

2:14:38

So what is the story here by the way? I think interesting case some of you are confused.

2:14:41

some of you are confused.

2:14:42

So here we have clustering basis.

2:14:44

So what the example I showed you here was PCA plus K means?

2:14:53

You've first PCA did the data

2:14:57

changed.

2:14:58

We did feature engineering on our data.

2:15:00

Then we did K means.

2:15:02

There was no output here.

2:15:05

What is the story we are talking about right now?

2:15:08

Now we are talking about PCA plus Supervisor.

2:15:10

supervised.

2:15:13

You first PCA, you do data, you change you do feature engineering, you change the features,

2:15:19

you go from 30 features to only two important features

2:15:23

and now using those two important features you try to predict the output.

2:15:27

So that is the story we are talking about right now.

2:15:30

So I think if I have to visually show you, here your output why will be in our breast cancer problem.

2:15:35

You have output why is something, or person has malignant cancer or benign cancer.

2:15:39

something like this.

2:15:40

You have you have got right?

2:15:42

We have seen in the classification classes.

2:15:44

We have seen that briefly.

2:15:45

Now one way you can solve the problem this way.

2:15:48

If you can solve the problem this way,

2:15:51

you might end up getting a poor quality model because you've got too many dimensions and

2:15:56

too many useless features.

2:15:58

What we are trying to discuss is, okay?

2:16:01

Let us go back and do PCA.

2:16:04

Let us go back and do PCA.

2:16:06

And yeah.

2:16:08

Let us go back and do PCA. And what you can go back and do is, you know, after going

2:16:15

after doing PCA, now you want to predict what the output is.

2:16:20

So let us go back and do PCA and on the basis of that you want to predict what the output is.

2:16:25

So this data set we'll go ahead go to machine learning.

2:16:28

So whatever ML we want to do, it will be based on this particular, you know, a dataset.

2:16:33

So that's the way how it will intuitively work out.

2:16:37

Okay. So.

2:16:38

you will actually end up getting very good quality results if you do PCA

2:16:41

because we have kind of only considered the more important sections of our data right now.

2:16:48

So this is the final visualization I wanted to show you.

2:16:50

I have data here, and then this is what we are able to see.

2:16:54

Back to our classification 101 session.

2:16:58

Classification basic session.

2:17:00

What is classification?

2:17:01

We are trying to find out that the surface that best separates the classes.

2:17:07

And as we have PCA, you can see that,

2:17:09

in this data set, we are able to see that,

2:17:12

we are able to find a very nice surface that separates reds from blues.

2:17:17

Yeah, we can debate can debate that

2:17:19

a red point all the way out layer,

2:17:22

we can separate not, but I think majorly,

2:17:25

if we're just going to majorly

2:17:28

majorly separate reds from the blues.

2:17:30

So you can actually build a model with a very high accuracy.

2:17:33

Accuracy is a high over.

2:17:35

Okay, so this is the benefit of doing PCA.

2:17:36

doing PCA okay sure very nice guys any questions all of you okay so this is pretty much the

2:17:44

contents for the session for today any questions anybody so there are some references that

2:17:52

I wanted to share with you okay you can talk about some references here

2:18:00

specifically on the

2:18:06

Mathematical part.

2:18:07

Okay, mathematical part, there are not, like, the focus is not too much on the math part, but if you want to understand behind the scenes,

2:18:15

how it is happening, what is the maths behind PCA, there are some nice tutorials.

2:18:21

There are some, I can share with you a couple of, because what we are focused on is the concept,

2:18:27

what is PCA, but the mathematics of PCA is very, very deep.

2:18:31

Just in case some of you are interested, only if you are interested, it is the only optional thing.

2:18:35

thing.

2:18:36

If you are you, if you can look at the mathematics behind PCA.

2:18:42

So this, I think, is a very nice kind of a thing.

2:18:45

So again, it's a very nice visual, you know, explanation.

2:18:50

I like it a lot.

2:18:51

Because here here, it's a very visually explained here.

2:18:54

Here here, visually explained here.

2:18:56

This is who is coming in?

2:18:58

So let me just go and you can take a look at it.

2:19:05

So this is a very nice video.

2:19:07

Okay, Gurtec, this is for you.

2:19:09

So I've asked you.

2:19:10

I think you want to know the mathematics behind the scenes.

2:19:12

So this is for you.

2:19:13

I think this video will be very helpful for you.

2:19:15

If you still have a question, I will dedicate some time.

2:19:18

Because in class in, you,

2:19:21

your questions are valid, but if you want,

2:19:24

we can do another small session where I can sit only with you

2:19:27

and I'm happy to take you through the maths of PCA.

2:19:30

So we can do that separately.

2:19:32

No problem.

2:19:34

Okay.

2:19:35

If you're able to follow well and good, if you're not able to follow, we will, we will do it outside the regular classes.

2:19:43

We will plan something.

2:19:44

Okay, on this one.

2:19:45

But yeah, but the core idea you can see what is happening, you know.

2:19:49

Yeah, this is very nicely explained.

2:19:51

This is a very nice channel, by the way.

2:19:53

Visually explained.

2:19:54

You know, there are many concepts, you know, visually explained

2:19:57

you know.

2:19:59

Like, you know, logistic regression, why is different?

2:20:02

So we have a sigmoid, but

2:20:03

but it's a little mathematically here here,

2:20:05

things are here.

2:20:06

So this is also very nice,

2:20:09

like, like decision trees,

2:20:11

we have decision trees,

2:20:12

you know,

2:20:13

so some of the things are very mathematical.

2:20:16

We are not getting into that,

2:20:17

because the objective of our course is not ML, right?

2:20:21

So here here, this whole machine learning topics are.

2:20:24

And I think in my very first session,

2:20:27

I did take you to my, this channel.

2:20:29

You can see this, you can absolutely

2:20:32

where is that?

2:20:35

So you can absolutely follow some of the videos in my channel also.

2:20:46

I think you'll find it helpful as well.

2:20:48

Here we have some videos in

2:20:50

how it's going to internally.

2:20:52

So you can use a reference.

2:20:54

There are a lot of good content which you can find.

2:20:57

But many of them will be mathematical.

2:20:59

So if you are comfortable with that, you can see here.

2:21:01

can here.

2:21:02

Yeah, this is the match behind the scenes.

2:21:04

What is going on?

2:21:05

Okay, Gurthik.

2:21:06

Please go through it.

2:21:07

Chalo.

2:21:08

Rest, everybody, followed, all of you.

2:21:11

Everybody is clear.

2:21:14

I think comparatively it was a lighter session.

2:21:19

The concepts were important, obviously, but I hope everybody was able to connect the dots

2:21:23

with respect to how is unsupervised learning different, what is clustering.

2:21:28

You were able to think through the clustering problem from scratch.

2:21:30

from scratch. What are the steps involved? All of you were able to relate to it.

2:21:34

And finally, the last piece was dementia reduction, the case studies we talked about, recommendation.

2:21:39

What are the different cases where clustering gets used? I hope everybody is aligned and clear

2:21:45

in terms of what we discussed.

2:21:47

Just going to pause for a minute more, if there's any other questions.

2:21:54

And Pratab, I think you can parallelly also maybe start your activities.

2:21:58

So while I may, I may,

2:22:00

wait to see if there any other questions.

2:22:04

Yeah, okay. So I'm sorry.

2:22:15

Just to summarize the components once again.

2:22:19

Guys, just to just to summarize once again.

2:22:22

Yeah, so we talked about unsupervised basics.

2:22:24

This was the main agenda items for today.

2:22:27

We talked about unsupervised basics.

2:22:29

We talked about unsupervised basics.

2:22:30

about K-means clustering. So K-means clustering was from an algorithm perspective. We had to talk about it algorithmically. We talked about the K-means workflow, how we assign points to clusters in detail. I think K-means is something we covered in detail because clustering will be an important part for you. And then the last two pieces at a high level, we talked about PCA is not at a mathematical level. PCA is we are not getting to the algorithm details in the course. But everybody in the audience should understand next time you come across principle

2:23:00

component analysis, at least what is it important to reduce dimensions? We understood that intuition. Why should we reduce many features into fewer features?

2:23:09

Why can we do it?

2:23:11

So we have that come features in clustering and

2:23:14

and come features in kind of we did a classification.

2:23:17

Okay. And finally, we did a PCA visualization. If we have a very high dimensional data, we cannot visualize it.

2:23:23

So how do we do PCA and how to we project that data into only two dimensions.

2:23:27

So these were the core learnings that we had from today.

2:23:29

that we had from today, today's session.

2:23:32

And yeah, so there are no other questions.

2:23:34

Thank you, guys.

2:23:34

Thank you so much.

2:23:35

I think today is the last course.

2:23:38

Yeah, business day, right.

2:23:40

Yeah, we'll be meeting again on Monday.

2:23:41

You get a long time to practice to go over some more problems.

2:23:50

And I think we are at a very interesting phase right now where we've got another two to three more machine learning sessions left out.

2:23:57

So everybody utilized.

2:23:59

this time recap the journey that we did and we'll continue on with our machine learning

2:24:05

lecture in the in the next session okay okay thank you all of you take care good night

2:24:14

yeah um so sir just to confirm the

2:24:21

the lecture was supposed to be till 1030 right which one uh

2:24:29

this lecture you can continue on yeah that's okay okay all right we have we should wrap it by

2:24:34

1030 idly because we want to make sure the learners you know yeah you can understand fair enough

2:24:40

so all right guys i am going to be releasing the feedback poll now and you know the drill after the

2:24:47

feedback poll we will have the millimeter quiz

2:24:59

All right guys, so I've released the readback poll and the Mentiator Quiz is also the link is there. I am going to be sharing my screen now.

2:25:29

so can you all see my screen okay it seems 10 people have already joined uh yeah okay

2:25:39

everyone is voted as well all right i'm ending the poll now i'll see you all in the

2:25:44

minty middle quiz now okay we'll start the quiz very quickly just want to see how many people

2:25:54

have joined there are 14 attendees in the class today

2:25:59

so at least 10 12 people i don't know okay yeah i'm the link is in the chat i don't know if i hope everyone can see it all right uh 11 play

2:26:29

i think we can start okay guys thumbs up in the chat if you're ready to start

2:26:36

thumbs up here

2:26:38

thumbs up here five six seven all right we can start

2:26:59

yeah so what is a centroid what is a centroid mean in a k-means clustering

2:27:12

it's a relatively easy problem

2:27:29

wait a second uh hold on hold on hold on hold on one second hold on one second hold on one second i don't think that is correct uh yeah the main position of the assigned points is the correct answer actually um i don't know why let me just give me one second guys let me let me check the

2:27:56

so okay just just one second sorry about that okay uh all right all right all right all right all right no problem i have uh yeah corrected the answer and most of you have gotten it correct so yeah okay uh yeah the main position of the assigned points that is the correct answer that's a centroid in the k means clustering

2:28:26

okay all right moving on to the next question

2:28:32

i hope everyone did it okay yeah yeah changing the option worked

2:28:40

apologies for that i had marked the wrong answer wrong option correct before now now we can

2:28:47

move on to the next question

2:28:56

player um anyone anyone is wants to join okay i'm seeing a lot of people

2:29:13

of people clicking on thumbs up so i'll i'll just go ahead okay all right so all right so second question

2:29:25

of the day after assigning points to centroids what happens next so it is the k means

2:29:36

um loop that you guys saw i see you guys are answering quickly so that's

2:29:55

awesome awesome it seems no one has got that wrong great great great job guys

2:30:04

and i'm so proud of you everyone got it correct all right next question okay starting now

2:30:25

third question if pca clouds overlap which conclusion is the safest so when i when i say pca clouds

2:30:34

it means the region of the pca so like in a diagram if you see in a two-d diagram

2:30:43

x y-axis if there are regions of pca that are overlapping what conclusion is the safest okay guys understand

2:30:55

is the keyword.

2:31:05

Yes, the clustering group must contain exactly one group is a possibility.

2:31:11

The answer is not entirely wrong, but it is not the safest answer.

2:31:16

The safest answer is that we are probably missing some higher dimensional detail.

2:31:21

Right?

2:31:23

Maybe there is there is some some dimensional detail.

2:31:24

Right.

2:31:25

mentioned some information that we have missed which is causing the overlap.

2:31:30

So these answers are all all valid but this is the safest answer.

2:31:36

So good job everyone.

2:31:39

A lot of you are getting everything correct.

2:31:42

Awesome, really awesome.

2:31:46

It seems some people have dropped out maybe.

2:31:54

Oh, okay. No. No, no one has. All right. Next question.

2:32:01

Second last question of the day. What does inertia mean in SK learn key means?

2:32:10

This was just after the break, sir covered.

2:32:24

that was something like S-S-C or S-W-S-S.

2:32:31

If you guys remember, I'm just giving you a hint. I'm not giving you the answer.

2:32:37

Yes, the sum of squared distances.

2:32:41

That is correct.

2:32:44

Inertia does not mean the number of iterations before convergence.

2:32:48

This is just an invalid answer. This makes no sense in the context.

2:32:53

Um, great job everyone.

2:32:56

Wow, it seems everyone is performing well today.

2:32:59

Oh, okay.

2:33:03

Farander somehow missed that one.

2:33:08

But no problem. You have done well so far.

2:33:11

The competition is really close today, actually, if you look at it.

2:33:16

Wow.

2:33:18

Last question, guys.

2:33:20

Farander is okay.

2:33:22

Ferender is okay if you don't win this one.

2:33:25

Okay, try to get it correct.

2:33:27

Don't try to be the first one, sir.

2:33:29

Why can PCA before K means sometimes help?

2:33:34

Remember, if you're doing PCA before K means.

2:33:38

So you know what PCA does, right?

2:33:42

We do PCA first and then if we do K means, what is the benefit of that?

2:33:48

It's a very simple answer if you think about it.

2:33:51

answer if you think about it. It's actually quite logical.

2:33:55

I mean, you need to know the, you need to understand the basics.

2:33:59

But once you do it, it's very, very simple.

2:34:03

Oh, great, great. Awesome.

2:34:07

Yes, this is the correct answer. It can reduce noisy dimensions and computations

2:34:11

because PCA will reduce the number of dimensions

2:34:15

and then K means will easily be able to cluster according to the reduced dimensions

2:34:20

the reduced dimensions.

2:34:22

So yeah, that is a very good, this is a very good answer, and many people have got that correct.

2:34:29

It ensures all centaids are actual rows. This is not really valid.

2:34:35

I mean, PCA does not really help with that.

2:34:38

And also it guarantees the correct number of clusters.

2:34:42

The number of clusters is not, like PCA will not take care of the clusters at all.

2:34:49

PCA will just reduce the number of dimensions and the K in key means stands for the number of clusters.

2:34:56

So it is a possibility that it may guarantee the correct, it may help in getting a correct number of clusters.

2:35:05

It's a possibility, but it does not guarantee it.

2:35:08

Because by reducing noisy dimensions and computations, you can get better K's, right?

2:35:14

So maybe this will also be a secondary effect, but this is not the primary effect.

2:35:18

the primary effect. This is the primary effect. This is what happens first and then maybe this happens or maybe this may not happen. Certainly does not guarantee it. Okay? All right. Let's see the leader board.

2:35:48

and just 63 good job everyone. You all did very well today and it seems you all were paying attention.

2:35:57

So awesome. All right. I will see you guys tomorrow for the tutorial session.

2:36:03

And until then, have a good night.

2:36:07

Bye bye. I will end the session now. Okay. Bye guys.