# Writing your first function

The next trick you need to learn in order to reduce the amount of code that you write is how to define a function in python.  We can write a function to add two numbers together like this:

```python
def add( a, b )
    return a + b
```

This function takes in two __arguments__, `a` and `b`.  These arguments are variables that are passed into the function. It then returns a single number `a+b`.  

On its own the code above does nothing.  To make it do something we need to call it as shown below:

```python
c = add(3, 4)
```

When the function is called in this way the input argument `a` is set equal to 3 and the input argument `b` is set equal to 3.  The variable `c` is thus set equal to the return value of the function `a+b=3+4=7`.

__To complete the exercise write a function like add above that takes two arguments in input.  The function should multiply these two input arguments together and return the resulting quantity.__
