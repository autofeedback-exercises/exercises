import numpy as np
import scipy.stats as st

def area(N) : 
  nin = 0
  for i in range(N) : 
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    if x*x + y*y < 1 : nin = nin + 1
  mean = nin / N
  var = (N/(N-1))*( mean - mean*mean )
  sig = np.sqrt( var / N )
  return mean + sig*st.norm.ppf(0.05), mean, mean + sig*st.norm.ppf(0.95)
  
print( area(1000) )
