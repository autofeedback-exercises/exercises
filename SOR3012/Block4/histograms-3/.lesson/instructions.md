# Multinomial trials

We are now going to move away generating Bernoulli random variables and move towards generating a random variable that can take on any value in the set {0,1,2,3,4}.  The probability mass distribution for this random variable will be:

![](equation.png)

I have started writing a function called `myvariable` that can be used to generate this type of random variable.  Your task is to complete this function and to also complete the process of filling in the array called `probs` that should contain the five elements of the probability mass function that is defined above.  

The function `myvariable` works by generating a uniform random variable between 0 and 1.  An if statement is then used to decide if this random variable falls in the line segment of length P(X=0) between 0 and P(X=0).  In this case a value of 0 is returned.  If the random variable does not fall within this first line segment we then test if the random variable falls into the line segment of length P(X=1) between P(X=0) and P(X=0) + P(X=1) and return a value of 1 if this condition is satisfied.  If this condition is not satisfied we then test if the random variable is the line segment of length P(X=2) between P(X=0) + P(X=1) and P(X=0) + P(X=1) + P(X=2) and return a value of 2 if the condition is satisfied.  This process is then repeated for all the possible values that the random variable can take.
