# The median and percentiles

Plotting the cumulative probability distribution is useful as if we know this function we can use it to describe the data using a sentence such as:

_z % of the data points are less than or equal to x._ 

In this exercise I am going to show you how to determine the value of x if you are given z.
We can do this using the function `np.percentile` as shown below:

```python
x = np.percentile( data, z ) 
```

The quantity, x, that is output by this function can gives us a value that z % of the data in the NumPy array `data` is less or equal to.

__To complete this exercise I would like you to use `np.percentile` to calculate:__

1. the minimum of the data set
2. the lower quartile
3. the median
4. the upper quartile 
5. the maximum 

for the data contained in the np array called `x`.  These quantities should be saved in variables called `dmin`, `lowq`, `median`, `highq` and `dmax`.  

We can display these 5 points graphically by using a box plot.  I have included some code at the end of the program that will produce a box plot for you.
