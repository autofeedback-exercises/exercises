import matplotlib.pyplot as plt
import numpy as np

def uniform_discrete(a, b) :
  # Your code for generating a uniform discrete random variable goes here
  return np.floor( 6*np.random.uniform(0,1) ) + 1 
 
# Your code for generating the scatter plot of dice rolls variables goes here
xvals, yvals = np.zeros(100), np.zeros(100) 
for i in range(100) :
    xvals[i] = i+1
    yvals[i] = uniform_discrete(1, 6)

plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Index")
plt.ylabel("dice roll")
plt.savefig("dice.png")
