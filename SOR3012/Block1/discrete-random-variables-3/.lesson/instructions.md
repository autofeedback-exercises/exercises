# Plotting Bernoulli trials

We are now going to combine what you did  the previous exercise with what you did in the previous.  You are going to generate 100 Bernoulli random variables and you are going to draw a scatter plot graph showing the values of all these random variables.

To complete this exercise you will need to:

- Write a function called `bernoulli` that takes a parameter `p.`  This parameter gives the probability that the trial is successful - and that the function thus returns a 1. 

- Use your `bernoulli` function and what you know about loops, lists and functions to generate a NumPy array that contains 100 Bernoulli random variables all of which have the parameter p set to the global variable `prob`.

- Draw a scatter plot showing the values of all your random variables.  The x-coordinates of the points in this graph should be 1, 2, 3 etc and the y-coordinates should be the values of the random variables.  The x-axis label of the graph should be "Index" and the y-axis label should be "random variable".

N.B. The plotting part of this exercise is similar to the exercise that you did with the uniform random variables.
