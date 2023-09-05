# Beyond the modulo function

We have now gone about as far as we can with the modulo function so lets see if we can do something else using what we have learned about if statements.  I have provided you with a file called `mydata.dat` and have loaded the numerical data in this file into a NumPy array called `xvals` by using the command:

```python
xvals = np.loadtxt("mydata.dat")
```

If you look at the `mydata.dat` file you can see the data that is in the file.  As you can see some of the data points are equal to 5 and some are not.  __I would like you to create an array called `ydata` that has the same length as `xdata`.__ `ydata[i]` should be set equal to 1 if `xdata[i]` is equal to 5.  If `xdata[i]` is not equal to 5 `ydata[i]` should be set equal to 0.    
