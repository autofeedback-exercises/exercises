# Simulating a random walk

In this exercise you are going to learn how to simulate a random walk in 1 dimension.  During this walk you will thus take discrete steps either forward or backwards by one unit.  The decision to move forward or backward on each turn is made by generating a Bernoulli random variable with parameter `p`.  If the Bernoulli random variable is equal to 1 the walker moves forward one step.  If the Bernoulli random variabel is equal to 0 the walker moves backwards one step.  This process of generating Bernoulli random variables and deciding how to move in response is then repeated multiple times

I want you to write a function called `random_walk` to simulate the random walker.  This function should take three arguments:

- `startpoint` is the initial locatin of the walker on the line.
- `nsteps` is the number of random steps that you would like the walker to take
- `p` is the probablity that the walker takes a step forward (i.e. in the positive direction)

Your function should return the final position that the walker arrives at after his series of `nsteps` random steps.
