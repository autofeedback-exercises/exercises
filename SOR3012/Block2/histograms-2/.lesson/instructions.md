# Plotting numbers of successes and failures

In this exercise, we are going to tackle the same problem as we did in the previous one but we are going to modify the way that you wrote the code.  The objective is to write the code to complete this task in a way that can be extended so that we can deal with more complex random variables that have more than two possible outcomes.  Furthermore, I would also like to show you how we can create a visual representation for the fraction of successes and the fraction of failures.

To complete the exercise you must do the following:

1. You will need to write a function called `bernoulli` that takes a parameter `p` (the probability of success) and that returns a Bernoulli random variable.
2. You will need to modify the loop that comes immediately after the function called `bernoulli` so that within this loop 100 Bernoulli random variables with parameter `prob` are generated.  In addition, you should, within this loop, count the number of times these trials were failures in element 0 of the array called `counts` and the number of times these trials were successful in element 1 of the array called `counts`.
3. You need to modify the final loop in the code to the right so that the first element of the array called `counts` is equal to the fraction of failures and the second element of the array called `counts` is equal to the fraction of successes. 

Notice that when you are counting the number of successes and failures in the elements of the list called counts you do not need to use an if statement.  Instead, you can do the following:

```python
myvar = bernoulli(p)
counts[int(myvar)] = counts[int(myvar)] + 1
```

This works because if the trial was unsuccessful the function `bernoulli` returns a 0.  Consequently, the code above will modify element 0 of the list.  By contrast, if the trial is successful `bernoulli` returns a 1 and the above code will modify element 1 of the list.  
If you complete the exercise correctly an estimate of the probability mass function will be generated in the file `bernoulli_histogram.png`.

N.B. The `int` command converts the real number that is output by `bernoulli` into an integer so that it can be used to refer to a particular element of the list.
