# Calculating the data range

For these next three exericses I have sampled some random variables from a distribution for you.  The data I have generated is contained in the `data.dat` file.  I have also loaded the data from this file into a NumPy array called `x` by using the command:

```python
x = np.loadtxt("data.dat")
```

The aim of these exercise is to determine something about the distribution that the data in `data.dat` was sampled from.  We do this by calculating quantities know as summary statistics.  Summary statistics are useful because they allow 
us to summarise information contained in our data set using fewer numbers.  For example, if we were writing a report about our results we might want to summarise the experimental data that we obtained using a sentence like the one below:

_N measurements of this quantity were obtained.  The lowest value obtained was L, while the highest value was U._

This sentence provides a one-line summary of the range of results that we obtained in the experiment.  

Notice that we can get the number of elements in a NumPy array called `myarray` by using the command:

```python
number = len( myarray )
```

Furthermore, we can use python to determine the largest and smallest values in a np.array called `myarray` by using the commands:

```python
lowest = min( myarray )
highest = max( myarray )
```

__To complete this task write a program that determines the values that should be used to replace `N`, `L` and `U` in the sentence in italics above given the data in the `data.dat` file.__  
I have loaded the data in this file into an array called `x` for you.  To pass the test you will need to define three variables called `N`, `L` and `U` in your code.  The values of these 
variables should be set so that the sentence in italics above is an accurate description of the information in `data.dat`.     
