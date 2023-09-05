# Histograms and Percentiles

Notice that the heights of the bars in a histogram that we generate by sampling random variables are all averages.  In other words, the heights of the bars in a histogram are all random variables.  We should thus quote error bars on these error bars
to make our results reproducible.  In this exercise I am going to show you how to do this by resampling.

I have done a lot of the work for you here you still have to do a few things; namely:

1. You have to write a function called `dice_roll` that returns the (random) outcome of a roll of a fair six-sided dice.  Remember that when we roll a fair, six-sided dice we are generating a uniform discrete random variable that can take values of 1, 2, 3, 4, 5 or 6.
2. You need to write a function called `histo_esimtate` that takes a parameter called `n`.   Within this function, you should compute a histogram by taking `n` samples using your `dice_roll` function.  The fraction of times you get each of the six possible outcomes on rolling the dice should be stored in the array called `histo`, which will be returned from your function.
3. You need to work out how to set the elements of the array `upper`.  The elements of this array should be set equal to the difference between the 95th percentile of the distribution of histogram estimates and the median for the distribution of histogram estimates.  N.B. This number should be positive. 

When you have written this code and run the code a graph showing the histogram with suitable error bars on each of the bars in this is produced.  Look at the code that I have written in `main.py` and try to understand how it works.  We are only using ideas about 
percentiles that you have learned about in this course.  It is a little more complicated, however, as we have to use two dimensional NumPy arrays as we are estimating multiple random variables simultaneously.

Please note that the code checks the values of the error bars that are stored in the arrays called lower and upper.  You must therefore have these arrays defined in your code in order to pass the test
