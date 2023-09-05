import matplotlib.pyplot as plt
import numpy as np

def exponential(lam):
  # Your code to generate an exponential random variable goes here
  return - np.log( np.random.uniform(0,1) ) / lam  

lamd = 2      # The parameter for the exponential random variable you should sample
xmax = 6     # The maximum value for x that you should use in your histogram
nbins = 200   # The number of bins you should use for your histogram
histo = np.zeros(nbins)     # The variable you should use to store the histogram
xvals = np.zeros(nbins)     # The midpoints of your histogram bins that are used for plotting
delx = xmax / nbins
# Your code to compute an estimate for the probability density function of an exponential random
# variable goes here.
for i in range(500) :
    mybin = int( np.floor( exponential(lamd) / delx ) )
    histo[mybin] = histo[mybin] + 1

histo = histo / (delx*500)
for i in range(nbins) : xvals[i] = (i+0.5)*delx

# This draws the histogram - do not delete this code
plt.plot( xvals, histo, 'k-')
plt.xlabel("Random variable value")
plt.ylabel("Probability")
plt.savefig("myhistogram.png")
