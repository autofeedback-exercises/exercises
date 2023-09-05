# Plotting the probability mass function

In the previous exercise you learned how to estimate the probablity mass function for a random variable by repeatedly sampling that random variable and by using those samples to construct a histogram.  In the instructions for that exercise I stated that the heights of the bars in the histogram were all random variables.  In fact, the whole point of the previous exercise was to plot a confidence limit around the estimate of the distribution that is obtained by sampling.

When we first encountered this idea of providing confidence limits around estimates of quantities that were found by taking a sample mean we also discussed  the expectation.  When we calculated a sample mean we noted that we were estimating the expectation and that, furthermore, for many of the random variables we have been investigating in this exercise, this expectation can be calculated exactly.  The natural question one might, therefore, ask is: is there some exact set of quantities that can be compared to the histograms we learned to estimate in the last exercise?  In other words, we know that the sample mean converges on the expectation.  Does the histogram similarly converge and if it does what does it converge to?

You should not be suprised to learn that the histogram does indeed converge.  You should not be surprised by this fact as I told you in the very first sentence of these instructions that when we calculate a histogram we are __estimating the probablity mass function__ for the random variable.  Consequently, similarly to how we check whether the true expectation lies within our confidence limit we can also check whether the true probablity mass function lies within the confidence limit for our histogram.

__Your task in this exercise is thus to plot two bar charts.__  One of these bar charts should show the exact probablity mass function for a discrete uniform random variable that can take any integer value that is greater than or equal to 1 and less than or equal to 6.  The second should show the probablity mass function for a binomial random variable with n=6 and p=0.5.  Notice that you can calculate the exact probability mass function for a binomial random variable by using scipy as follows:

```python
import scipy.stats

# Calculate P(X=x) where X is a binomial random variable with parameters n and p
p = scipy.stats.binom.pmf( x, n, p )
```

See [this](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.binom.html) website for more details.   

Notice that I have written stub code in the panel on the left to plot the two probablity mass functions side by side.  In your final figure the probablity mass function for the uniform discrete random variable will appear in blue while the probablity mass function for the binomial random variable plot will appear in red.  Examine the code for generating side by side bar charts carefully as you will need to produce side by side plots like these for the exercises in future weeks.

Functions exist for plotting the probablity mass/density functions for other types of random vairables.  You can find information here:

* [Geometric](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.geom.html)
* [Negative binomial](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nbinom.html)
* [Exponential](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html)
* [Normal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)
