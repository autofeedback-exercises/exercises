# Arbitrary uniform random variables

You can generate a uniform random variable that lies between 0 and 1 using the `np.random.uniform` function as shown below:

```python
U = np.random.uniform(0,1)
```

The variable you generate in this way is a sample from U(0,1).  To complete this exercise you will need to write a function to generate uniform random variables from U(a,b).  In other words, we want 
a uniform random variable is greater than a and less than b.  It is very straightforward to generate such a random variable if we know how to generate a random variable from U(0,1).  We simply need to 
generate a sample from U(0,1) and then perform the following transformation:

![](equation.png)

The number output here is (obviously) a uniform random variable that lies between a and b.

__To complete the exercise you thus need to complete the function called `uniform`__.  This function takes two arguments; namely, the `a` and `b` parameters that are introduced above.  It should `return` a uniform random variable between `a` and `b`. 
I have included some code at the bottom of the `main.py` file that will draw variables from various uniform continuous distributions and plot them for you.  You can thus see how the spread of the variables is affected by how the `a` and `b` parameters
are set. 
