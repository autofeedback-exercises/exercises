# Using the normal distribution for error bars

It is reasonable to assume that any sample mean we calculate is a sample from normal distribution.  This assumption is useful because it makes it straightforward to calculate confidence limits.  If the mean is a sample from a normal distribution we no longer need to do any resampling as we know the distribution we are sampling from.  In this exercise, we are going to see how easy this realisation makes the process of calculating error bars.  

The fact that sample means are samples from normal distribution is a consequence of a the central limit theorem.  This theorem tells us the cumulative probability distribution function for the sample mean.  __The cumulative probability distribution function for the sample mean is that of a normal distribution with an expectation equal to the sample mean and a variance equal to the sample variance divided by the number of random variables from which the sample mean was computed.__  To compute error bars around a sample mean we need simply to compute the sample variance and to then use the inverse of the cumulative probability distribution for a normal random variable to get the percentiles.  There is no longer any need to resample.

The exercise in the panel on the left will hopefully help you to understand how you can compute an error bar by using the central limit theorem.  To complete this code you will need to write a function called `mean_with_errors` that takes in a parameter called `n`.  This function should return a sample mean computed from `n` uniform random variables that lie between 0 and 1.  This quantity should be returned in the variable called `mean`.  In addition, you should also compute the 5th and 95th percentiles for the distribution that mean was sampled from.  These two quantities should be retuned as `lower` and `upper`.  When calculating `lower` and `upper` you should assume that the sample mean is a sample from a normal distribution with suitable parameters.

Within the function called `mean_with_errors` you will need to compute the sample mean and the sample variance for your sample of `n` uniform random variables.  You should then be able to calculate lower and upper using your computed values for the sample mean and sample variance and the following python function:

```python
ppp = scipy.stats.norm.ppf(0.95)
```

The call above computes the 95th percentile for a standard normal random variable.  i.e. A normal random variable with expectation 0 and variance 1.
