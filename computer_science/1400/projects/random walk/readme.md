https://codio.com/rkingsford/random-walk---description/guides

Problem:

In 1827, the Scottish botanist Robert Brown observed that pollen particles suspended in water seemed to float around at random. He had no plausible explanation for what came to be known as Brownian motion, and made no attempt to model it mathematically. Louis Bachelier presented a clear mathematical model in his doctoral thesis, The Theory of Speculation in 1900. His thesis was largely ignored by respectable academics because it dealt with the then disreputable field of understanding financial markets. In 1905, Albert Einstein used similar stochastic thinking in physics to describe how it could be used to confirm the existence of atoms. People seemed to think that understanding physics was more important than making money, and the world started paying attention.
Brownian motion is an example of a random walk. Today, random walks are widely used to model physical processes like diffusion, biological processes like the kinetics of displacement of RNA from heteroduplexes by DNA, and social processes like movements of the stock market.
We are interested in random walks because of their wide applications to many problems, and for learning more about how to structure simulations nicely in Python.

Farmer John has an old grandparent (Pa) that likes to wander off randomly when working in the barn. Pa starts from the barn and every second takes one step in a random direction North, South, East or West. What is Pa’s expected distance away from the barn after 1000 steps? If Pa takes many steps, will Pa be likely to move ever further from the origin, or be more likely to wander back to the origin over and over, and end up not far from where he started? Let’s write a simulation to find out.

This particular barn is in the center of a large grassy field. One day Pa starts to wander off, and notices that the grass has been mysteriously cut (by John) to resemble graph paper. Notice that after one step Pa is always exactly one unit away from the start. Let’s assume that Pa wanders eastward from the initial location on the first step. How far away might Pa be from the initial location after the second step? John sees that with a probability of 0.25 Pa will be 0 units away, with a probability of 0.25 Pa will be 2 units away, and with a probability of 0.5 Pa will be √2 units away. So, on average Pa will be further away after two steps than after one step. What about the third step? If the second step is to the north or south, the third step will bring the farmer closer to origin half the time and further half the time. If the second step is to the west (back to the start), the third step will be away from the origin. If the second step is to the east, the third step will be closer to the origin a quarter of the time, and further away three quarters of the time.

It seems like the more steps Pa takes, the greater the expected distance from the origin. We could continue this exhaustive enumeration of possibilities and perhaps develop a pretty good intuition about how this distance grows with respect to the number of steps. However, it is getting pretty tedious, so it seems like a better idea to write a program to do it for us.

However, there are a couple more twists to the situation. Pa’s wife Mi-Ma, another grandparent of John’s, also likes to wander away randomly, but riding an old mule. The mule goes South twice as often as any other direction. Lastly, John’s favorite hog Reg has an odd habit of wandering off too, but only randomly going east or west at each step, never north or south. People think he’s a sun-follower, but nobody’s really sure. John figures your Python program ought to model these two as well, while you’re at it.

simulate()

Define a function called simulate() that takes three parameters:
A list of “walk lengths” to simulate,
The number of trials (how many times to do walks of the specified lengths), and
Which walker we are modeling: 'Pa’, 'Mi-Ma’, 'Reg’, or 'all’.
For your convenience, define a main() function (that runs with conditional execution, per usual). main() should read the following three arguments from the command line:
A list of comma-separated “walk lengths” to simulate (there should be no spaces in this list),
the number of trials, or times to try each walk length, and
which type of walk we are modeling: 'Pa’, ‘Mi-Ma’ or ‘Reg’ or 'all’.
If invoked with python3 random_walk.py 100,1000 50 all, your main() function should call simulate([100,1000], 50, 'all').
Assume the wanderer always starts each walk at (0,0) in an infinite grid. On individual tests, your output values should be close to the examples given below, though they won’t be exactly the same. The format of the output should be the same.
Pa random walk of 100 steps
Mean = 8.5 CV = 0.6
Max = 19.8 Min = 1.4
Pa random walk of 1000 steps
Mean = 31.4 CV = 0.5
Max = 57.0 Min = 1.4
Mi-Ma random walk of 100 steps
Mean = 26.7 CV = 0.4
Max = 52.6 Min = 7.6
Mi-Ma random walk of 1000 steps
Mean = 243.4 CV = 0.2
Max = 318.2 Min = 156.2
Reg random walk of 100 steps
Mean = 7.6 CV = 0.8
Max = 22.0 Min = 0.0
Reg random walk of 1000 steps
Mean = 33.2 CV = 0.7
Max = 86.0 Min = 0.0
In the output above:
Mean is the average distance over all walks of that length as the crow flies,
Max is the longest distance as the crow flies,
Min is the shortest distance as the crow flies, and
CV is the Coefficient of Variance, defined as the standard deviation divided by the mean.
Round all values to one decimal point, as shown.
All distances should be in steps.

plot()
Define a function called plot() that plots a sample of final locations in a turtle window in order to visualize their behaviors. plot() should expect no arguments. Your output should be similar to the picture below. Do only one plot: plot all three characters for 50 trials on walk length 100. Don’t plot the 1000 walk length; it takes too long.
Hint: The fastest programs calculate all final locations first, separate from plotting, and only move turtles to plot final locations.
.guides/img/random_walk
Details of plot()
The autograder will compare your output to expected output. In order to ensure that your output matches the expected output, do the following:
Use turtle.shape() (docs) to change the turtle’s shape (the three shapes are 'circle’, 'square’, and ‘triangle’).
Use turtle.color() (docs) to change the turtle’s color ('black’, 'green’, and ‘red’).
Use turtle.stamp() (docs) to plot individual points.
Use turtle.shapesize() (docs) to scale the shapes to half of their original size in both dimensions.
Use turtle.speed() (docs) and set it to the fastest speed if you have trouble with timing out.
Use a scale of five pixels (for the turtle) per step (for Pa, Mi-Ma, or Reg).
Set the size of the screen to 300x400.
When you are finished, call the provided save_to_image() function to save the results to a file.
Logistics
Autograder hints
There are many correct ways to use random number generation to perform this simulation. Because the autograder expects exact results, you may find the following hints useful. If you have followed these hints and still get different results, please check with your instructor or with the academic tutors for help.
Use python’s built-in random module (docs) to simulate the random behaviors.
Order choices of direction in a clockwise manner: north, then east, then south, then west.
Be sure that you make use of every random sample you make.
When simulating or plotting all walkers, use the order in which they were introduced: Pa, then Mi-Ma, then Reg.
Perform all trials for a given walk length before moving onto another walk length.
Perform all walks for a given trial before moving onto another walker.
Grading
0-20 points: design doc is correct and complete
21-100: all automated and manual tests pass
Rubric
(5 points) simulate() produces correct results for Pa for 100 steps for 50 trials.
(5 points) simulate() produces correct results for Pa for 1000 steps for 50 trials.
(5 points) simulate() produces correct results for Mi-Ma for 100 steps for 50 trials.
(5 points) simulate() produces correct results for Mi-Ma for 1000 steps for 50 trials.
(5 points) simulate() produces correct results for Reg for 100 steps for 50 trials.
(5 points) simulate() produces correct results for Reg for 1000 steps for 50 trials.
(20 points ) simulate() produces correct results for undisclosed inputs.
(10 points) plot() produces an image as shown.
(4 points) Code has a main function with conditional execution.
(4 points) File has a module docstring with required information in it.
(4 points) Every function has a proper function docstring.
(4 points) Variables use snake case.
(4 points) The style checker emits no warnings.
Frequently Asked Questions
Q: What is standard deviation?
A: You don’t need to understand the details, if you do not already know what it means, but it is one measure of how spread out the dots are. Coefficient of Variance is another measure of spread.
Q: How to we compute the standard deviation?
A: You could write your own function if you want, but it is simpler to import the statistics module and use functions defined there.
Q: My numbers don’t match up to the example numbers. Should they be exactly the same?
A: Since we are dealing with random numbers, your results will be close but slightly different.
Q: I was looking on the web, and somebody posted a solution to this project already, including screenshots. Can I use that, look at it for inspiration if I get stuck, maybe?
A: If you find it, don’t use it and tell your instructor. Remember that the goal of the assignment is not the program or even the grade; the goal of the assignment is to develop your skills and knowledge. Anything that short-circuits that process cheats you of your education.
This problem is adapted from Introduction to Computation and Programming Using Python (MIT Press) revised and expanded edition by John V. Guttag, 2013.