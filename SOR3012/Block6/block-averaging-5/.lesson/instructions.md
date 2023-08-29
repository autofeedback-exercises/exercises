# The relationship between the error and the size of the blocks

In this final exercise we are going to bring together everything we have learned in order to look at how the block averaging technique allows us to resolve the problems that we would otherwise have in estimating errors with correlated variables.

The previous four exercises have shown you how to compute the average and the standard deviation by block averaging.   In this exercise we are going to look at how the size of the error depends on the size of the blocks.  To do this we will need to encapsulate 
the code that we have written to calculate block averages and errors in a function that takes as input the data and the length of the block, M, into which to divide the data.  In `main.py` I have written the first line of this function for you as follows

```python
def block_average( M, data ) :
    # Your code goes here

    return error
```

You should then use the function you have written to plot a graph that shows how the size of the error depends on the length of the blocks.  In drawing this graph you should calculate the error when block averages with the following lengths 
are used in the calculation of the error:

```python
xvals = [10,20,30,40,60,100,120,200,300,400]
```

The x coordinates of the points of in your graph should be equal to the numbers in the list above.  The y-coordinates of these points should then be the corresponding values of the error for that size of block.  The y value for the point at x=10 is thus
the error that is calculated from block averages that are calculated from the first 10, second 10 points and so on.  In practise you can calculate these y-values by using the function `block_average` that you will have written.

You should see that error is initially small.  It will then grow as the size of the various blocks is increased before plateauing to a constant value.

The x axis label of your graph should be "Size of blocks" and the y axis label should be "Error" 
