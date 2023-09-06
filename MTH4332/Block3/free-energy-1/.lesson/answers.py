import matplotlib.pyplot as plt
import numpy as np

# Read in the list of magnetisation values
mags = np.loadtxt("magnetisations")

# This is the number of bins
nbins = 50
# This is the minimum and maximum for the grid
minx, maxx = -1.1, 1.1
# Your code to calculate and plot the histogram goes here
delx = (maxx - minx) / nbins

histo = np.zeros(nbins)
for m in mags : 
    mav = m / (20*20)
    xbin = int( np.floor( (mav-minx) / delx ) )
    histo[xbin] = histo[xbin] + 1

histo = histo / len(mags)
xvals = np.zeros(nbins)
for i in range(nbins) : xvals[i] = (i+0.5)*delx

plt.plot( xvals, histo, 'k--' )
plt.xlabel("average magnetisation per spin")
plt.ylabel("probability density")
plt.savefig("myhisto.png")
