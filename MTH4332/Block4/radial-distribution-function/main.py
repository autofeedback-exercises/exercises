from ase.io.trajectory import Trajectory
import matplotlib.pyplot as plt
import numpy as np


# Set the maximum distances that you are going to plot out to 
# and the number of bins to use when calculating the radial distribution function
maxd, nbins = 3, 150

# Do a loop over all the trajectory frames
for atoms in Trajectory('trajectory.traj') :
    # Calculate the distances between all pairs of atoms
    distances = atoms.get_all_distances( mic=True )
    # Do a double loop over all the distances
    for i in range(1,distances.shape[0]) : 
        for j in range(0,i) :
            if  distances[i,j]>maxd : continue 
            # You need to add code to accumulate the histogram here


# Now you need to add code to normalise and plot the radial distribution function
