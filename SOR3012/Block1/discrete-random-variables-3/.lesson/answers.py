import numpy as np
import matplotlib.pyplot as plt

def bernoulli(p) : 
  # Your code for generating a Bernoulli random variable goes here
  if np.random.uniform(0,1)<p : return 1
  return 0   
 
# Your code for generating the list of Bernoulli random variables goes here
prob=0.5
xvals, yvals = np.zeros(100),np.zeros(100)
for i in range(100) : 
   xvals[i] = i+1
   yvals[i] = bernoulli(prob)

plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Index")
plt.ylabel("random variable")
plt.savefig("graph.png")
  
