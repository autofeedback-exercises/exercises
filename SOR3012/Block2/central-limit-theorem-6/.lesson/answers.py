import numpy as np
import scipy.stats 

def mean_with_errors(n) : 
  # Your code to calculate the sample mean and sample variance 
  # for a set of n uniform random variables between 0 and 1 goes 
  # here.  
  S, S2 = 0,0 
  for i in range(n) : 
      myvar = np.random.uniform(0,1)
      S = S + myvar 
      S2 = S2 + myvar*myvar
  mean = S / n
  var = (n/(n-1))*( S2/n - mean*mean )
  lower = mean + np.sqrt(var/n)*scipy.stats.norm.ppf(0.05)
  upper = mean + np.sqrt(var/n)*scipy.stats.norm.ppf(0.95) 
  
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
