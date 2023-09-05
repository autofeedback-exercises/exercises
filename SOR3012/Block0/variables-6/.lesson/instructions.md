# Debugging codes with variables

Congratulations on completing the last exercise.  You now can now use variables when you evaluate mathematical expressions.  You can thus exploit Python effectively when doing the more laborious computations that are required in some of the homework assignments.  Using Python to do the calculations in your homework is actually a pretty sensible way of getting better at programming.

In this exercise we are going to look at a pitfall you might run into if you use Python to do the calculations in your homework.  To understand this pitfall consider the code given below: 

```python
a = b+4
b = 2
print( a )
````

You might think that this code will output a value of 6.  It will not do so, however, it will instead return the following error:

````
Traceback (most recent call last):   
  File "python", line 1, in <module> 
NameError: name 'b' is not defined
````

The reason is Python reads the code sequentially.  The variable `b` is defined on the second line of the code above after it is used on the first line.  When Python tries to evaluate `b+4` on the first line it cannot as it does not understand what `b` is.

To check you understand this point I have, in `main.py`, written a program in which a number of variables have been defined after they are used.  You do not need to write any new code here.  You just need to rearrange what is there and to ensure that the code runs.
