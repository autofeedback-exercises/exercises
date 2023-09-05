# The discrete uniform random variable

We learned in a previous series of exercises that we can generate a uniformly distributed random variable between `a` and `b+1` using:

```python
U = np.random.uniform(a,b+1)
``` 
 
To generate this variable we generate a uniform random variable between 0 and 1 and then transform using:

```python
U = a + (b-a+1)*np.random.uniform(0,1)
```

As you can see when `np.random.uniform` returns a 0 `U` will equal `a`.  By contrast, when `np.random.uniform(0,1)` returns a 1 `U` will equal `b+1`.

In this exercise, we are going to introduce the code to generate another type of random variable.  The particular type of random variable we will discuss here will be the discrete uniform distribution.  This type of random variable can take one of `n` possible values and all these values have equal probabilities of `1/n` of being observed.  We sample from a distribution of this sort when we roll a fair dice and the probabilities of rolling 1, 2, 3, 4, 5 and 6 are all 1/6.  

We could use the code that we learnt to generate the multinomial distribution in order to complete this task.  There is an easier way, however, which involves taking advantage of the floor function:

```python
a = np.floor(b) 
```

The floor of `b` is the integer that you obtain when you strip everything after the decimal point in `b`.  Thus if in the above `b=9.85` then `a=np.floor(b)=9`.  Similarly, if `b=3.1` then `a=np.floor(b)=3`.

__Your task is thus to write a function called `uniform_discrete` that takes the arguments `a` and `b` and that returns a uniform discrete random variable that is an integer that is greater than or equal to `a` and less than or equal to `b`.__  You will need to use the `np.floor` function discussed above in your function and you should not need to use any conditional (if) statements or for loops.   
