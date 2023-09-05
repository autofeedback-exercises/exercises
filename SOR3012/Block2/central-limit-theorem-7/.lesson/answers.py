import matplotlib.pyplot as  plt
import numpy as np
import scipy.stats 

# You may want to add some code here

def binomial(n,p) :
  # Your code to generate the binomial random variables goes here.
  nv = 0 
  for i in range(n) : 
      if np.random.uniform(0,1)<p : nv = nv + 1
  return nv 

nsamples = 500 
histo = np.zeros(6)
# Insert code to compute a histogram by generating nsamples binomial random variables with
# n=5 and p=0.5 here.  
for i in range(nsamples) :
    myval = binomial(5,0.5)
    histo[myval] = histo[myval] + 1

# Don't forget to normalise your histogram.
histo = histo / nsamples

# Include the code to compute the error bars at the 90% confidence limit here.  The list
# called error should contain the difference between the 95th percentile for the distribution of the 
# mean and the mean 
error = np.zeros(6) 
error = np.sqrt( histo*(1-histo) / nsamples )*scipy.stats.norm.ppf(0.95)

# This will plot the histogram and the error bars
plt.bar( [0,1,2,3,4,5], histo, width=0.1 )
# This plots the small bar around each of the values.
plt.errorbar( [0,1,2,3,4,5], histo, yerr=error, fmt='ko' )
plt.xlabel("Outcome")
plt.ylabel("Fraction of occurances")
plt.savefig("histo_with_errors.png")
