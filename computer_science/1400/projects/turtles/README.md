Turtle Patterns I - Description
Problem
Expected Duration: 3-4 hours
If you look around the web, you can find examples of many projects that draw pictures, scenes, landscapes, geometric patterns, or interesting “doodles” using Python turtles. For this project you will draw a picture, scene, landscape or doodle that has identifiable patterns. The things that appear in your “doodle” must be built by combining 3 different “atomic” shapes or patterns and using repetition. Atomic means it’s a building block that you don’t break down into anything else. Use your imagination, but if you struggle too much, simplify your goals. Some examples of common geometric shapes, which might give you ideas can be found here.
User inputs for this project should be the turtle window’s width and height values from the console. They should be positive integers only and should be validated. These values should then be used to set the size of the window. You must document in your module docstring what the window size should be.
Key ideas in this project are HOW you organize your code. Use parameterized functions as building blocks and loops wherever there is repeated code with variations.
Do not copy code from anyone else, including internet sources, though you may look at code for ideas. You may use any code provided in your book. Here is one example of an approved resource for scene building.
They give you an idea, some skeleton code, some test code, and a little bit of example code to use, but you have to do the real thinking and the developing work. As always, if you are unsure about some resource, you can ask the instructor for approval.
The Python turtle graphics documentation can be found here.
Keep in mind that you will revisit this code later for Project 6, but don’t get hung up on that, and save any advanced features for Project 6–don’t do them for this project.
Logistics
Starter Code
You are given the starter code in the file doodles.py. You must use this file. Add code and comments in the places indicated. Do not change the other parts that have been given, and do not worry if you don’t fully understand all of the code now, because you will later. You’ll notice that there are test cases for the code that has been given. By intent, if you do mess up certain parts of the code, your program won’t pass those cases.
Grading
Late submissions receive 50 points and no feedback.
0-20 points: design doc is correct and complete
21-100: all automated and manual tests pass
Rubric
In the cases below, “shape” refers to any shape or pattern.
Automatic Tests (29 points)
(9 points) If user enters anything other than positive integers for window width and height, print “Width and height must be positive integers.” and exit.
(9 points) Code has a main function with conditional execution.
(5 points) Code uses snake case for variable names.
(6 points) The style checker (pylint with a custom configuration) emits no warnings.
Manual Tests (51 points)
(9 points) The scene includes at least 3 different shapes, each encapsulated by a function with parameters.
(9 points) Atomic shapes appear with different fill colors and border colors in different locations.
(9 points) Atomic shapes appear tilted or rotated.
(9 points) Atomic shapes appear in different sizes.
(9 points) Loops are used to reduce any repeated code.
(6 points) Your file has a module docstring with required information in it.
Frequently Asked Questions
Q: I don’t have a clue how to even start–what should I draw?
A: If you don’t know where to start, then start by creating 3 functions: one that draws a circle, one that draws a rectangle, and one that draws a triangle. Once you can draw a circle in one spot, make it so your code can draw many circles of different sizes, colors and borders in different locations. Now do the same thing with a tree, where a tree is a rectangle and a triangle combined.
Q: Do I have to draw a scene or a landscape? Can I draw a mathematical pattern instead?
A: You don’t have to draw a scene. You can draw a tessellation or pseudo-tessellation of some kind, or draw other constructs as long as it’s clear that you satisfy the test cases above. We would just define shape loosely. If you’re not sure, ask your instructor.
Q: Do you have an example I can look at?
A: I could show you a picture, but we want you to express yourself, not just copy other people. If you are struggling, start simple. Draw something by hand first, then ask yourself if it meets all the criteria. If not, add more until it does.
Q: How do I rotate or tilt a shape?
A: Change the heading of the turtle before you start to draw a shape.
Q: Do I have to put all of my code inside functions?
A: Yes. All of your code should be inside main or inside other functions that are called by main or called by other functions.
Q: I’m only using one turtle in my code everywhere. My code works if I define it at the top of the file, but my code breaks if I define it in main. So is it okay to have the turtle defined outside of main or any other function?
A: No. Define your turtle in main and pass it as a parameter to each function that uses it.
Q: How do I reduce the amount of copied code?
A: When you notice that you are copying the exact same code but changing a few numbers, such as when drawing a bunch of trees or bubbles, try to find a pattern in the changes. Then you can do two things: 1) put the repeated block of code in a function with parameters, and 2) put the repeated block of code in a loop that changes the numbers.
Q: Can I use more than one turtle in my program?
A: Yes, if you want. It’s up to you.
Q: What do you mean by "atomic shape"?
A: It’s a shape that we don’t think or draw as a combination of other shapes. For example, a triangle is an atomic shape. A spiral might be an atomic shape. A house made out of rectangles and triangles is not an atomic shape. Olympic rings is not an atomic shape.
