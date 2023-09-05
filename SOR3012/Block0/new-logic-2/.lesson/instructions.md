# Using logic within a for loop

To complete the previous exercise you probably had to copy and paste the same piece of code three times.  You had one if statement for the variable `x`, one for `y` and one for `z`.  In previous exercises, we have always said that copy and pasting code is a bad way to program as if we write more code we will create more bugs.  We thus want to learn how we can reuse one if/else statement multiple times.  The answer as we have seen in previous exercises is to use a for loop and lists. 

In the code in `main.py` the line:

```python
xvals = np.loadtxt("values.dat")
```

creates a NumPy array that contains 100 elements by reading in the numbers in the file called `values.dat`.  __Your task is to write a code that sets `yvals[i]` equal to the modulus of `xvals[i]`.__  Notice that you can print all the numbers in `xvals` on different lines by using a command like this:

```python
for i in range(len(xvals)) :
    print( xvals[i] )
```

Notice also that the following code:

```python
for i in range(6) :
    if i<3 : 
       print( -1*i )
    else :
       print( i )
```       

Would output:

````
0
-1
-2
3
4
5
````

****
Code like this:

```python
for i in range(len(xvals)) :
    print( xvals[i] )
```

works fine.  This way of coding is not very "pythonic" though.  If you are interested and have time do a bit of reading.  You will find that you can write loops like this one that use less code and that are thus better.  Count how many symbols you have used to write your program.   I had 188 symbols in the solution I would expect you to write based on the instructions I have given here.  I can reduce this down to 126 symbols though by using the features I can find to shorten my code. 

    
