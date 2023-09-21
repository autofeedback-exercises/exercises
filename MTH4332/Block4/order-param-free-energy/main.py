from ase.io.trajectory import Trajectory
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

minx, maxx, nbins = -.5, 1.1, 70
# Your code to calculate the estimates of the histogram goes here

# You then need to calculate the average histogram and the errors on the histogram here

# And lastly you need to convert the histogram to a free energy surface here


# This variable should be set equal to your final estimate of the free energy as a function of the order parameter
fes = 
# This variable should be set equla to the error on your estimate of the free energy as a function of the order parameter
error =


# This sets the coordinates at which the x values of the points in your free energy surface should be plotted
xbins = np.zeros( nbins )
for i in range(len(gat_average)) :
    xbins[i] = (i+1)*delx


# This will draw a graph showing your free energy surface. Notice that the free energy surface
# we are plotting here is not well converged.  
plt.fill_between( xbins, fes - error , fes + error )
plt.xlabel("order parameter")
plt.ylabel("free energy")
plt.savefig("fes.png")
