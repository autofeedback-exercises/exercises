# Histogram for exponential random variable

I would like you to estimate the probability density function for the exponential random variable by writing a function to generate this type of random variable and by repeatedly sampling the random variable by calling this function multiple times.  

There are two important things to bear in mind that are different when you calculate the histogram for a continuous random variable.  The first is the way that we use the `np.floor` function to describe the continuous interval into `n` discrete bins.
If we know that the random variable is between `min` and `max` then we can work out the widths of these bins using the following python code:

```python
delr = ( max - min ) / n
```

If we now generate a random variable `U` we can work out the bin that the random falls within using the following code:

```python
mybin = int ( ( U - min ) / delr )
```

We can thus use the above within the normal code that we would employ to compute the histogram. Now, however, the height of the bars in the unormalized histogram are equal to the number of random variable that fall into each of the line segments of interest.  
As we are trying to estimate a probablity density function we must sure that the function is normalised correctly so that:

![](normalisation.png)

So the area under your final histogram should be one.  When you normalise the points in the list called counts you should thus divide by the number of points sampled and the width of the bins (`delr`).
The estimates of the probability densities that once you have completed this procedure are plotted at the midpoints of the bins.  These midpoints can be generated using the command:

```python
for i in range(nbins) : xvals[i] = (i+0.5)*delr
```

Furthermore, the probablity density function should be plotted using a line rather than a series of bars as it is a continuous function.  The probablity mass function that we have estimated in previous exercises only has non-zero values for particular discrete values of x.

With all this in mind, for this exercise I want you to estimate the probablity density function for the exponential random variable by sampling.   The one small problem that we have is that the exponential random variable can in theory take any value between 0 and infinity.  The probability of having a very high value for the random variable is, however, very small.  We can thus safely truncate the range and calculate our estimate of the probability density function over some finite range.

Please note that you must set the variable called `lamd` equal to the parameter for the exponential random variable you sample in order to pass the tests for the task.  Furthermore, you must ensure that a graph is plotted using the `plt.plot` and `plt.savefig` commands that appear at the end of the code.
