import matplotlib.pyplot as plt
import numpy as np

def bernoulli(p) : 
  # Your code to generate a bernoulli random variable goes here
  if np.random.uniform(0,1)<p : return 1
  return 0 

prob, counts = 0.3, np.zeros(2)
# Your code to generate n bernoulli trials and to count the number of 
# successes and failures goes here.
for i in range(100) :
    myvar = bernoulli(prob)
    counts[myvar] = counts[myvar] + 1
  
# Your code to ensure that the sum of the two heights is equal to one 
# and that the bar chart plotted is thus an estimate for the probablity
# mass function goes here.
for i in range(2) : counts[i] = counts[i] / 100
  
  
# This will draw a bar chart showing the fraction of successes and 
# the fraction of failures.
plt.bar( [0,1], counts, width=0.1 )
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.savefig('bernoulli_histogram.png')
  
  
