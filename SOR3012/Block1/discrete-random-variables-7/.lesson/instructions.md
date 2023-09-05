# The geometric random variable

Let's now turn our attention to the second of the random variables that we can generate from Bernoulli random variables - the geometric random variable.  We have learned that the geometric random variable measures the number of trials that we have to perform until we get a success.  It thus stands to reason that to generate such a variable we will need to perform multiple Bernoulli trials and stop generating Bernoulli trials once one of them is equal to one.

We cannot use a for loop to generate a geometric random variable because, unlike the binomial random variables, we do not know how many trials we will have to perform in advance.  We thus need to use a while loop instead.  An example of a while loop is shown below:

```python
var=0
while var<10 : 
   var = var + 1
```

This while loop runs until the variable called var is equal to 10 - in other words it runs while the variable var is less than 10.  You can do a similar thing with while loop with a function call in place of the variable as shown below:

```python
while bernoulli(p)==0 : 
   var = var + 1
```

In this case the loop will be entered into every time a call to the function bernoulli returns 0.

To complete the exercise you will need to:

- Write a function called `bernoulli` that takes in a single argument called `p`. This argument gives the probability that the trial is successful - and that the function thus returns a 1.

- Use your bernoulli function in a second function called `geometric`.  This `geometric` function should take one parameter `p` (the probability of success in each individual trial).  The function should then return a geometric random variable.

The idea you will use to generat the random vairable is explained in [this video](https://www.youtube.com/watch?v=fna3ysWxP0E)
