import numpy as np
import scipy.stats 

def mean_with_errors(n) : 
  # Your code to calculate the sample mean and sample variance 
  # for a set of n uniform random variables between 0 and 1 goes 
  # here.  
  
  
  # When complete this function should return
  # lower = the 5th percentile of the distribution that was sampled
  # mean = your estimate for the sample mean
  # upper = the 95th percentile of the distribution that was sampled
  # N.B. To compute lower and upper you should be using the central
  # limit theorem as discussed in the explanatory text.
  return lower, mean, upper 
  
print( mean_with_errors(100) )
print( mean_with_errors(100) )
print( mean_with_errors(100) )
print( mean_with_errors(100) )
