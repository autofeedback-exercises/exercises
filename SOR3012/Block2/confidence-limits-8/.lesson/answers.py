import matplotlib.pyplot as plt
import numpy as np

def dice_roll() :
  # Insert code so that this function return  the outcome of a roll of a fair six sided dice here.
  return np.floor( 6*np.random.uniform(0,1) ) + 1 
 
def histo_estimate(n) :
  histo = np.zeros(6)
  # Insert code to compute a histogram if you roll the dice n times here.
  for i in range(n) :
      val = dice_roll()
      histo[int(val-1)] = histo[int(val-1)] + 1
  
  return histo / n
  
# This tells us that 50 (nsamples) random variables should be used in the generation of each histogram
# This procedure of generating 50 random variables and calculating the histogram should then 
# be repeated 500 (nresamples) times.
nsamples, nresamples = 50, 500
# This loop resamples your histogram
histo_samples = np.zeros([nresamples,6]) 
for i in range(nresamples) : histo_samples[i] = histo_estimate(nsamples)

# This computes percentiles from your histogram
lower, upper, median = np.zeros(6), np.zeros(6), np.zeros(6)
for i in range(6) : 
  # We find the median 
  median[i] = np.median( histo_samples[:,i] )
  # Generally we quote the error by saying that the the value is between 
  # median - lower and median + upper.  When we compute percentiles we are 
  # getting values for median - lower and median + upper so we have to 
  # do some sums to get the values of lower and upper that we want.
  lower[i] = median[i] - np.percentile( histo_samples[:,i], 5 )
  upper[i] = np.percentile( histo_samples[:,i], 95 ) - median[i] 
 
plt.bar( [1,2,3,4,5,6], median, width=0.1 )
# This plots the small bar around each of the values.
plt.errorbar( [1,2,3,4,5,6], median, yerr=[lower,upper], fmt='ko' )
plt.xlabel("Outcome")
plt.ylabel("Fraction of occurances")
plt.savefig("histo_with_errors.png")
