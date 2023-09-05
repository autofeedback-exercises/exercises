# Plotting Bernoulli trials

This exercise should be a simple revision of what we did last week.  I want you to generate 100 Bernoulli random variables and draw  a graph showing the values of all these random variables.

To complete this exercise you will need to:

- Write a function called `bernoulli` that takes a parameter `p.`  This parameter gives the probability that the trial is successful - and that the function thus returns a 1. 

- Use your `bernoulli` function and what you know about loops, lists and functions to generate a list called `random_variables` that contains 100 Bernoulli random variables all of which have the parameter p set to the global variable `prob`.

I have included code in the cell on the left that will plot your list of random variables.  To get this code to work, however, you will need to write a second list called `indices` that contains a numerical index for each of these random variables.  The first of these indices should be equal to one, the second should be equal to two, the third should be three and so on.  

N.B. The plotting part of this exercise is similar to the exercise that you did with the uniform random variables.
