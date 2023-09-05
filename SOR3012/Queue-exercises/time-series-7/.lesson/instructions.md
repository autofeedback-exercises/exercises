# The poisson process

In this exercise we are going to move to sampling the poisson process.  We have already seen how poisson random variables can be generated in one of the other programming tasks.  The algorithm that we wrote previously was rather complicated, however.  In this exercise we are going to learn a much simpler method for generating Poisson random variables.  The key realisation for this method is that in a Poisson process the distribution for the times between adjacent events is exponential.  Consequently, we can generate a Poisson process by simply generating exponential random variables and adding them together.  The sum of three such exponential random variables will thus give us the time at which the third of the events occurs in our Poisson process.

We will explore this idea using the code in the panel on the right.  To complete this code you must:

1. Write a function called `exponential` that takes a parameter called `lam`.  This function should return the value of an exponential random variable with parameter `lam`.
2. Write a loop in which the function `exponential` is called multiple times.  Within this loop you will need to set the elements of the list called `arrival_times` and the elements of the list called `number_of_events`.  The first of these two lists should be set equal to the times at which the events occurred and the second of these two lists should be equal to the number of events that have occurred by that time. 

The code that is already there will draw a graph with points that have their x-coordinates equal to `arrival_times` and their y-coordinates equal to `number_of_events`.  In other words, the final result is a graph showing the how the number of events that have occurred changes with time.

Notice that in order to pass the test the inter arrival times between the events in your Poisson process must be exponentially distributed random variables with the parameter `lamd`.

  
