# Printing rethought

At the end of the last task, you should have arrived at a code that looked something like the one shown in `main.py`.  By using an array you have reduced the number of variables from 12 down to two and the number of lines of code from 23 down to 15.  This reduction was achieved by introducing a second type of variable - an array.  The net result of this is that although the symbol `table` refers to a single number the symbol `timesTable` refers to a list of 11 numbers.  These two variables are of different types.

This trick of using symbols to refer to different things is called the object-oriented paradigm and it was not invented by computer scientists.  Mathematicians were using this idea well before computers were even invented!  In a mathematical derivation, for instance, we might use the symbols a and b to refer to scalars or we might use the symbols a and b to refer to vectors.  In both cases, we can write c = a + b.  What we would do to evaluate c is, however, dependent on whether a and b are scalars or vectors.  We can see a difference like this in the print statement for the code on the left.  The two commands:

```python
print(table)
print(timesTable)
```

look very similar.   Both are asking us to print the value of a variable.  The first, however, will print a single number as the variable `table` has been set equal to an integer.  The second command, meanwhile, will print 11 numbers as the variable `timesTable` has been set equal to an array.  Notice also that, the 11 numbers output by this second command appear in square brackets to indicate that these 11 numbers are grouped together in an array.

This trick of using symbols to refer to more than just a single number makes our mathematical derivations and our programs longer.  To test if you have understood this I would like you to think about what is output by the command:

```python
print( timesTable[2] )
```

Now try the command:

```python
print( timesTable[2], timesTable[5] )
```

You will pass the tests for this exercise once you have worked out how to use what you have learned from these experiments to modify the code in the cell on the left so that it gives the following output:

````
7
0.0 7.0 14.0 21.0 28.0 35.0 42.0 49.0 56.0 63.0 70.0
````

Hint: Notice the absence of square brackets in the second line here.
