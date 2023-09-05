import numpy as np
import scipy.stats 

def sample_mean(n) :
  # Your code for calculating the sample mean for n 
  # uniform random variabels between 0 and 1 goes here.
  v = 0
  for i in range(n) : v = v + np.random.uniform(0,1)
  return v / n

def limit(n,m) : 
  # Your code to calculate the m sample means goes here.
  # Each of these sample means should be computed from 
  # n uniform random variables between 0 and 1 goes 
  # here.  
  samples = np.zeros(m)
  for i in range(m) : samples[i] = sample_mean(n)
  lower = np.percentile( samples, 5 )
  median = np.median( samples )
  upper = np.percentile( samples, 95 )
  
  # When completed this function should return
  # lower = the 5th percentile of the distribution for the sample mean
  # median = your estimate for the median
  # upper = the 95th percentile of the distribution for the sample mean
  return lower, median, upper 
  
print( limit(10,100) )
print( limit(10,100) )
print( limit(10,100) )
print( limit(10,100) )
