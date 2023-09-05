import numpy as np

def variance(n) :
  # Your function to calculate the variance for a set of n uniform random variables goes here
  myrand = np.random.uniform(0,1)
  S, S2 = myrand, myrand*myrand 
  for i in range(n-1) : 
      myrand = np.random.uniform(0,1)
      S, S2 = S + myrand, S2 + myrand*myrand 
  S = S / n 
  return ( n / (n-1) )*( S2 / n - S*S )
