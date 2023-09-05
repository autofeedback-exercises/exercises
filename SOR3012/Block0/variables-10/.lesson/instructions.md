# Introduction to loops

In `main.py`, you will see our now familiar program for calculating the seven times table. In the last exercise, you learned that although the variable `timesTable` is an array that is treated differently to the variable `table` each of the elements of the array `timesTable` (e.g. `timesTable[3]`) is a single number just like table.  This is an important realisation but it didn't help us to reduce the number of lines in the code further.  To reduce the number of lines we are, in this exercise, going to introduce loops.  To understand what loops do consider this piece of python code:

```python
for i in range(4) :
    print( i )
```

When this code runs it will produce the following output:

````
0
1
2
3
````

as the loop tells python to repeat instructions in the indented code that sits within the for loop four times.  The first time, however,  `i=0`, the second time `i=1`, the third time  `i=2` and the fourth and final time `i=3`.

To see if you have understood this idea see if you can replace these 11 lines from the code in main.py with two lines containing a for loop:

```python
timesTable[0] = 0*table
timesTable[1]  = 1*table
timesTable[2]  = 2*table
timesTable[3]  = 3*table
timesTable[4]  = 4*table
timesTable[5]  = 5*table
timesTable[6]  = 6*table
timesTable[7]  = 7*table
timesTable[8]  = 8*table
timesTable[9]  = 9*table
timesTable[10]  = 10*table
``` 

__To pass the test the variable that you use for your loop must be called `i`.__  To be clear, you can use any variable name for a loop variable.  I need you to use `i` here, however, so that I can test if you have used the loop correctly.
