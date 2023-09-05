# Calculating the expectation

As discussed in the previous couple of exercises the sample mean that we calculate is a random variable.  In order to make our result reproducible we must provide some information about the distribution whenever we quote this quantity.  When we calculate the mean, however, we are estimating the expectation of the random variable.  The expectation of a discrete random variable can be calculated exactly by using the following expression:

![](equation-1.png)

The sum in this expression runs over all the values that the random variable can take and P(X=x) is the probablity mass function.  Critically the value of the expectation that is calculated using the sum above is __not__ random.  You can thus calculate it exactly.

In these exercises we are calculating sample means by adding together independent and identical uniform, binomial, Bernoulli, geometric, exponential, negative binomial and normal random variables.  You know exact expressions for the expectations of all these types of random variable.  For expample, you know that the expectation of a binomial random variable Y with parameters n and p is:

![](equation-2.png)

Whenever you write codes to estimate the expectation of one of these variables you should check that the true expectation lies within the confidence limit that you calculate as a sanity check on your code.

For this expression I want you to write functions that return the true expectations for the following kinds of random variables:

* Bernoulli random variables
* Binomial random variables
* Geometric random variables
* Uniform discrete random variables
* Uniform continuous random variables
* Negative binomial random variables
* Exponential random variables
* Normal random variables

As you can see in the stub code on the left, each of your functions take the parameters of the random variable as input.  You then need to use the formula for the expectation within the function.  N.B. If you have forgotten the expression for the expectation of any one of these types of random variable you can easily look it up on Wikipedia.  
