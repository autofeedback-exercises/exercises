import numpy as np

def bernoulli(p):
   # Your code goes here
   if np.random.uniform(0,1)<p : return 1
   return 0

print( bernoulli(0.5), bernoulli(0.5), bernoulli(0.5)  )
