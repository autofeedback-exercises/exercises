# Plotting data

One advantage of using python to do calculations instead of using a calculator is that you can easily draw graphs using python.  In this exercise we are thus going to learn how to plot the seven times table that we have learned to calculate over the last few exercises.  To create plots with python we need to load a library called `matplotlib.pyplot.`  As you can see in `main.py` this library is loaded by including the command:

```python
import matplotlib.pyplot as plt
```

at the top of the script.  We will plot the values from the seven times table on the y-axis.  On the x-axis we will plot the numbers that must be multiplied by seven in order to get the values that have been plotted on the y-axis.  We can generate these 11 x-coordinates using the following code:

```python
xvals = np.zeros(11)
for i in range(11) : 
    xvals[i] = i
```

If you then store the eleven values from the seven times table in a second array called `yvals` you can plot the graph by using:

```python
plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Index")
plt.ylabel("Seven times table")
plt.savefig("seven-times-table.png")
```

__To complete this task you need to combine the information that I have given about plotting with what you have learned in previous exercises to create the plot showing the the first 11 numbers in the seven times table on the y-axis.__

