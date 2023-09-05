# Calculating the cumulative distribution for the data

Each of the random variables that you have learned to sample in the earlier parts of this exercise has a corresponding distribution that is sampled when we generate the data.
A question we might ask, therefore, is whether we can calculate the distribution if we are given a sample of random variables from a particular distribution.  The answer to this is no.  There are, however, 
a number of ways we can estimate the distribution function for a random variable.  In this exericse I am going to show you how we can estimate the cumulative probability distribution function, P(X<=x).

Watching [this video](https://www.youtube.com/watch?v=VaZTKmcxLvY) will help you to better understand this exercise.  

I have started writing the code to calculate the cumulative distribution for you in the file `main.py`.  As you can see I have loaded the data set from the file data.dat saved it in a list called `x`.  The two lines at the end of the script that read:

```python
plt.plot( x, y, 'k-' )
plt.savefig("cumulative-pdf.png")
```

Are then going to plot our cumulative probability distribution function.  You will notice that the list called `y` that we are plotting with the plot command is not defined anywhere in the code.  One of your tasks is, therefore, to write the code that calculates this variable.  

Recall from the video that calculating the cumulative distribution for a dataset involves two steps:

1. Sorting the data.  You can sort the data in the array called `x` by issuing the command `x.sort()` 
2. Plotting a graph in which the x-coordinates give the sorted data values and the y-coordinates are the index of the corresponding x coordinate in the sorted list divided by the total number of points in the list. .
3. Label the x-axis of your graph "x" and the y-axis of your graph "cumulative distribution"

Once you have sorted `x` you just need to create the list called `y` that you are going to plot.  This list is going to contain the numbers between 1 and the number of data points in your list divided by the total number of data points.  If you had four data points `y` would thus be:

```python
y = [1/4, 2/4, 3/4, 4/4]
```

Try to write the rest of the code to plot your cumulative probability distribution now.
