import matplotlib.pyplot as plt
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
# This loop calculates your nblocks estimates of the histogram
for i in range(nblocks) :
    # Your code for calculating each of the nblocks estimate of the histogram goes here



# This part plots the graph.  You need to define and set the variables lower_yv and upper_yv
# as described in the instructions
plt.fill_between( xv, lower_yv, upper_yv )
plt.xlabel("average magnetisation per spin")
plt.ylabel("free energy / natural units")
plt.savefig("free-energy.png")
