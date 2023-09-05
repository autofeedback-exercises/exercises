import numpy as np

def exponential(lam):
  # Your code to generate an exponential random variable goes here
  return -np.log( np.random.uniform(0,1) ) / lam  
  
# Here is some code that just tests your function is working correctly
print( exponential(2), exponential(2), exponential(2), exponential(2) )
