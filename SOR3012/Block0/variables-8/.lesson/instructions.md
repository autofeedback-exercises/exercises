# Arrays

Good work on completing the last task.  You clearly understand the code so lets now follow the first rule or programming and make it shorter.  

In this first exercise, we are going to reduce the number of variables we have used from 12 down to 2 by using arrays.  An array is essentially a list of N numbers.  We can create an array containing 11 elements by using the following command:

```python
timesTable = np.zeros(11)
```

This command tells python to create 11 spaces for storing numbers in memory and sets them all to zero.  What we want to do, however, is to set the first of these spaces in memory equal to the first number in the seven times table, the second space equal to the second number in the seven times table and so on.  We thus have to learn how to set the elements of the array.  Setting these elements is easy, though.  To set the first element equal to zero we simply have to write:

```python
timesTable[0] = 0
```
 
We can then set the second element using:

```python
timesTable[1] = 7
```

and so on for all subsequent elements.

- Use what you have just learned about arrays to modify the code in the cell so that the 11 numbers from the seven times table are stored in an array called `timesTable` instead of being stored in 11 distinct variables.
- In addition, replace the 11 print commands with the single command:

```python
print( timesTable )
```

Make sure to run your code and to see what the output looks like before running the tests.

***

Notice that for the command:

```python
timesTable = np.zeros(11)
``` 
 
to work we need to have the command:

```python
import numpy as np
```

at the top of the program.  As you will hopefully learn in future this command allows us to use functionality from something called NumPy that sits on top of the Python programming language.  In theory, we can use Python lists (which are a bit like arrays) to complete this task.  The advantage of using lists is that we then do not need to import the functionality from numpy.  NumPy arrays, however, are, unlike lists, specifically designed for doing maths, which is why I am using them here. 


