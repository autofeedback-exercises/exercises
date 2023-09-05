# Calculating the sample mean

We can calculate the sample mean from a set of random variables using the expression below:

![](equation.png)

It is worth considering what happens if each of the Xi in the sum on the right-hand side of the expression is a random variable from one of the distributions that we learned about last week.  Obviously, as all the Xi are random, it 
stands to reason that the quantity on the left-hand side is also a random variable.  We thus would like to know something about how the statistic on the left-hand side is distributed.

The easiest way to investigate this distribution is to sample random variables from this distribution multiple times.  __To complete this exercise I would thus like you to complete the function called `average` in `main.py`__.  This function takes an integer called `n` as input.  Within the function, you should generate `n` uniform random variables between 0 and 1.  You should then calculate the sample mean from these `n` variables using the expression above and then `return` this quantity from your function.   

When your code is complete a graph will be generated.  The red points are all uniform random variables that lie between 0 and 1.  The black points, meanwhile, are all sample means computed from sets of 100 uniform random variables.  __Before moving on take a look at this graph and consider which of the two distributions is more precisely distributed.__ 
