Rabbits, Rabbits, Rabbits - Description
Problem
Expected Duration: 3-4 hours
Suppose that a scientist is doing some important research work that requires her to use rabbits in her experiments. She always starts out with one adult male rabbit and one adult female rabbit. At the end of each month, a pair of adult rabbits produces one pair of offspring, a male and a female. These new offspring will take one month to mature and become adults.
To illustrate this, consider the first two months. At the beginning of month one, the scientist just has the original one pair of adult rabbits. A table for month one will look something like:
Month Adult Babies Total
1 1 0 1
At the end of month one this pair of adults produces one pair of offspring. Thus, at the beginning of month two the table will look like this:
Month Adult Babies Total
1 1 0 1
2 1 1 2
At the end of month two the adults have another pair of baby rabbits. The first pair of babies, born at the end of last month are not old enough to have babies yet, but we will categorize them as adults. So, at the beginning of month three the table looks like this:
Month Adult Babies Total
1 1 0 1
2 1 1 2
3 2 1 3
The scientist has 500 cages in which to hold her rabbits. Each cage holds one pair of rabbits. Assuming that no rabbits ever die, when will she run out of cages?
Requirements
Write a function in rabbits.py named do_research that does the following:
Accepts parameters (in this order) for the number of cages, the number of adults in the first month, and the number of babies in the first month.
Open a text file rabbits.csv for writing. Where it says “print” below, it means "write to the output file". Remember to close the file when done.
Print a table that contains the following information for each month.
The number of months that have passed.
The number adult rabbit pairs (those over 1 month old).
The number of baby rabbits pairs produced this month.
The total number of rabbit pairs in the lab.
Calculate how many months it will take until the number of rabbits exceeds the number of available cages.
Stop printing when you run out of cages.
Print a message giving how many months it will take to run out of cages
The output file should look like the following. Comments in the file begin with #, and must appear as shown:
Table of rabbit pairs
Month, Adults, Babies, Total
1, 1, 0, 1
2, 1, 1, 2
3, 2, 1, 3
4, 3, 2, 5
5, 5, 3, 8
6, 8, 5, 13
7, 13, 8, 21
8, 21, 13, 34
9, 34, 21, 55
10, 55, 34, 89
11, 89, 55, 144
12, 144, 89, 233
13, 233, 144, 377
14, 377, 233, 610
Cages will run out in month 14
Rubric
(12 points) A function named do_research exists and has the appropriate number of parameters. There is no global code.
(12 points) When run, the function’s output is printed to rabbits.csv. No output goes to the terminal.
(12 points) The expected comments exist in the output file.
(14 points) The output file contains correct, properly formatted data.
(10 points) The program contains a module docstring with the required information in it.
(10 points) Variables use PEP8 Python Style convention (snake case).
(10 points) The style checker (pylint with a custom configuration) emits no warnings.
Frequently Asked Questions
Q: What is a .csv file?
A: A .csv file is a text file where the data on a single line is separated by commas rather than spaces or tabs. There’s nothing else special about creating one.
Q: The example output has comments in it. Does my output file need comments like that too?
A: Yes, even though it’s a .csv file, you need to put the comments in there too.
Q: This project does not ask for user input for anything. So what are the program inputs?
A: What are numbers if changed, would change the result of the function? Values can be inputs even if they are not asked for from the console, a file, or the command line.
