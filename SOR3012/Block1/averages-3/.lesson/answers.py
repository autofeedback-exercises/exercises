import matplotlib.pyplot as plt
import numpy as np

def average(n) :
  # Your code to compute the average for a set of n uniform random variables goes here.
  var = 0
  for i in range(n) : var = var + np.random.uniform(0,1)
  return var / n 

# You should not need to adjust the code from here onwards
xv, yv1, yv2 = np.linspace(1,100,100), np.zeros(100), np.zeros(100)
for i in range(100) : 
  yv1[i] = np.random.uniform(0,1) 
  yv2[i] = average(100) 
  
plt.plot( xv, yv1, 'ro' )
plt.plot( xv, yv2, 'ko' )
plt.savefig("averages.png")
