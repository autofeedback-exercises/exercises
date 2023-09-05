# Estimating the histogram for a binomial random variable

We are now going to merge this business of computing a histogram with what you know about generating different types of random variables.  In this exercise for instance I would like you to generate a histogram for a binomial random variable.  In order to do this you will need to:

1. Write a function called `binomial` that takes parameters `n` (the number of trials to perform) and `p` (the probability of success in each of these trials) and that returns a binomial random variable.
2. Write a loop that generates multiple binomial random variables with parameters `nparam` and `prob` using the function called `binomial`.  You should use the list called `counts` to count how often each of the various outcomes in the sample space for this type of random variable appears just as you did for the random variable in the previous exercise.  In addition, you will also notice that you need to set the variable `noutcomes` equal to the number of possible values that the random variable can take.
3. You need to write a loop that converts each of the quantities in the list called `counts` from the number of times that the random variable was equal to a particular value into the fraction that the random variable took on this particular value.  In addition, you need to set the elements of the list called `sample_space` equal to the values that you would like to be plotted on the x-axis of your histogram.
4. You need to plot the estimate for the probablity mass function.  In your graph you should use __Random variable value__ as the x-axies label and __Fraction of occurances__ as the y-axis label.

The final result should resemble the probability mass function for a binomial random variable with parameters `nparam` and `prob`.  
