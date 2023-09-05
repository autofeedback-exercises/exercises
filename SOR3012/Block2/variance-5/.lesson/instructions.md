# Variance of mean

In this exercise I want you to calculate the variance of the sample mean: 

![](equation.png)

In the expression above each of the X_ij values is a uniform continuous random variable that lies between 0 and 1.  The sums over j are thus simply calculations of the sample mean.  The sample variance is thus calculated from n estimates fo teh sample mean.

I would like you to investigate how the value of the variance  changes as the number of variables (i.e. m) that were used in the calculation of __the sample mean__ changes.  As in the previous exercise, you will need to complete the two functions:

1.  `sample_mean` - takes a single integer `m` in input.  It should return a sample mean that is computed by generating `m` uniform random variables that lie between 0 and 1.
2. `variance` - takes two integers in input `m` and `n`.  This function should return an estimate of the variance for a sample mean computed from `m` uniform random variables that lie between 0 and 1.  This variance should be calculated by generating `n` estimates of the sample mean.

You then need to write the internals of the loop that I have started to set the variables `xvals` and `yvals`:

1. The first element of `xvals` should be set equal to 1, the second element should be set to two and so on.
2. The first element of `yvals` should be set equal to an estimate of the variance for a sample mean computed from one random variable, the second element should be set equal to an estimate of the sample variance for a sample mean computed from two random variables, the third element should be set equal to an estimate of the sample variance for a sample mean computed from three random variables.  This process should be continued until you have an estimate of the sample variance for a sample mean computed from 50 random variables.

All your estimates for the sample variance should be computed from 10 random variables.  

You should plot a graph showing your values for the sample variance on the y-axis and the number of random variables that were added together to compute the mean on the x-axis.  The label 
for the x-axis should be "Number of variables used to calculate mean" and the y-axis label should be "Variance"
