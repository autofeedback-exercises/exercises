# Sampling the mean

You have learned a sample mean computed by adding together n identical random variables has a value that close to the value of the expectation of the random variable.  Furthermore, the larger the value of n the closer the sample mean will be to the true expectation.  Importantly, however, the sample mean is not equal to the expectation as the sample mean is a random variable.  When we quote means we therefore need to do what we learned in previous exercises.  We need to provide some information about the distribution that the mean was sampled from.  We cannot simply quote a single number as that number is random.  The randomness makes it impossible for colleagues to reproduce our results.  What they should be able to show, however, is that the distribution they are sampling in their experiment is the same as the distribution we are sampling in ours. 

In this exercise I want to ensure that you understand what it means for us to generate a sample of sample means.  I thus want you to complete the following tasks:

1. Write a function called `sample_mean`.  This function should take in a single argument `n` and should return a sample mean that is computed by adding together `n` uniform continuous random variables that lie between 0 and 1.

2. Write a second function called `sample`.  This function should take in two arguments `m` and `n`.  It should return a NumPy array that contains `m` elements.  Each of these `m` elements should be equal to a sample mean that was computed by adding together `n` uniform continuous random variables that lie between 0 and 1.  

N.B. Your function called `sample` should call your function called `sample_mean`.
