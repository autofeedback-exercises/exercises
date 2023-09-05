# Counting successes and failures

We will start this exercise by doing something that by now should be very familiar.  We are going to write a function that generates a series of Bernoulli random variables.  Now, however, I want you to calculate the number of failures in these 
n trials as well as the number of successes.  

To complete the exercise you will need to do the following:

1. You will need to write a function called `bernoulli` that takes a parameter `p` (the probability of success) and that returns a Bernoulli random variable.
2. You will need to modify the function called `repeated_trials`.  This function takes two parameters `n` (the number of trials to perform) and `p` (the probability of success in each trial).  It should return two numbers `nsuccess` and `nfail`, which will give the number of successes and the number of failures respectively.  Within this function you will need to write the code to generate the `n` Bernoulli variables required and to compute `nsuccess` and `nfail`.
