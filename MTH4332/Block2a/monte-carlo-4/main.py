import numpy as np
import scipy.stats as st

def area(N) : 
  nin = 0
  for i in range(N) : 
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    if x*x + y*y < 1 : nin = nin + 1
  return nin / N
  
print( area(1000) )
