# Counting the number of fives

For this exercise I have once again loaded the data in the file `mydata.dat` into the NumPy array called `xvals` by using the command:

```python
xvals = np.loadtxt("mydata.dat")
```

__I would like you to write a program to count the number of fives that are in `xvals` to complete this exercise.__  To complete the exercise the variable `nfives` must be set equal to the number of fives in `xvals`.  

Notice that you can count the total number of elements in `xvals` by writing a program like this:

```python
nelements = 0
for i in range(len(xvals)) : 
    nelements = nelements + 1
    
print( nelements )
```

You will need to write something like the code above to commplete this exercise.  You will also need to include an if statement in your code, however.
