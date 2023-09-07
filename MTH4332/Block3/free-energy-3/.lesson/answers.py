import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

# Read in the list of magnetisation values
mags = np.loadtxt("magnetisations")

# This is the number of bins
nbins = 50
# This is the minimum and maximum for the grid
minx, maxx = -1.1, 1.1
# These variables should hold the x coordinates of the graph and the upper and lower 
# confident limits on the estimate of the free energy
xv, lower_yv, upper_yv = np.zeros( nbins ), np.zeros( nbins ), np.zeros( nbins )

# This is the size of the blocks.  You will calculate one estimate of the histogram
# over the blocks of this size
blocksize = 200
# This is the number of blocks that you are splitting the trajectory in
nblocks = int( np.floor( len(mags) / blocksize ) ) 

delx = ( maxx - minx ) / nbins
final_v, final_v2 = np.zeros(nbins), np.zeros( nbins )
# This loop calculates your nblocks estimates of the histogram
for i in range(nblocks) :
    # Your code for calculating each of the nblocks estimate of the histogram goes here
    histo = np.zeros(nbins)
    for j in range(i*blocksize,(i+1)*blocksize) :
        mav = mags[j] / (20*20)
        xbin = int( np.floor( (mav-minx) / delx ) )
        histo[xbin] = histo[xbin] + 1
    histo = histo / blocksize
    final_v = final_v + histo
    final_v2 = final_v2 + histo*histo

final_v = final_v / nblocks
final_v2 = np.sqrt( (1/(nblocks-1))*( final_v2/nblocks - final_v*final_v ) )*scipy.stats.norm.ppf(0.95)

fes, err = -5.0*np.log( final_v ), final_v2
for i in range(len(final_v)) : 
    if final_v[i]!=0 : err[i] = 5*final_v2[i] / final_v[i]  

lower_yv = fes - err
upper_yv = fes + err
for i in range(nbins) : xv[i] = (i+0.5)*delx

# This part plots the graph.  You need to define and set the variables lower_yv and upper_yv
# as described in the instructions
plt.fill_between( xv, lower_yv, upper_yv )
plt.xlabel("average magnetisation per spin")
plt.ylabel("free energy / natural units")
plt.savefig("free-energy.png")
