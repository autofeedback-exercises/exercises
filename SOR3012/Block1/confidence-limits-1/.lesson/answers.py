import numpy as np

def uniform_discrete(a,b) :
  # Your code goes here
  return np.floor( (b+1-a)*np.random.uniform(0.1) ) + a 


print( uniform_discrete(1,6), uniform_discrete(1,6), uniform_discrete(1,6), uniform_discrete(1,6) )
