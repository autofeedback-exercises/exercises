# Generating binomial random variables

In this exercise you are going to generate binomial random variables.  To complete the exercise you must:

- Write a function called `bernoulli` that takes in a parameter called `p`. This parameter gives the probability that the trial is successful - and that the function thus returns a 1.

- Use your bernoulli function in a second program called `binomial`.  This `binomial` function should take two parameters as input `n` (the number of trials to perform) and `p` (the probability of success in each individual trial).  The function should 
then return a binomial random variable.  This function `binomial` must call the first function `bernoulli` that you wrote.

Remember that the binomial random variable simply counts the number of successes when you perform __n__ independent and identical Bernoulli trials. 

The idea that you will need to use to complete the function is explained in [this video](https://www.youtube.com/watch?v=RNQFAH2wCos)
