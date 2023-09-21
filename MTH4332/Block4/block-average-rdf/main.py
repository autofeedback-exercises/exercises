from ase.io.trajectory import Trajectory
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

maxd, nbins = 3, 150
# This is the width of each of the bins in your histogram 
delx = maxd / nbins
# Your code to calculate the five estimates of the radial distribution from the blocks goes here


# I have calculated the x-coordinates at which to plot the histogram here
xbins = np.zeros(nbins)
for i in range(nbins) : xbins[i] = (0.5+i)*delx

# The first of these variables (average) should be the average rdf from the 5 blocks 
# The secould (error) should contain the errors on the estimates of the density in each bin.
# Your error should be indicative of a 95 % confidence limit
average = 
error = 

# This will draw a graph showing your radial distribution function.  Notice that the radial distribution 
# function we are plotting here is not well converged.  None of the radial distribution functions in your final
# project should look like this.  The big spikes suggest there is a problem.
plt.fill_between( xbins, average - error, average + error )
plt.xlabel("r / sigma")
plt.ylabel("g(r)")
plt.savefig("rdf.png")
