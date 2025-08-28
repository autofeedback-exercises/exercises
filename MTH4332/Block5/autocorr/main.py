from ase.io.trajectory import Trajectory
import matplotlib.pyplot as plt
import numpy as np

# This is number of frames that we are calculating the correlation function over
ncorr = 50

# This command uses ase to read in the trajectory
ftraj = Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesII/nve-short.traj')

# This sets up arrays to hold the autocorrelation function and the number of estimates 
# of each dot product we have
acf, norm = np.zeros(ncorr), np.zeros(ncorr)

# Your code to calculate the autocorrelation function goes here




# This will plot the autocorrelation function.  The value of 0.005 is the time 
# between each frame in the trajectory that I have given you here so the xvalues 
# are the time lags between the frames for whcih I have calculated the dot product 
# of the velocity.
times = 0.005*np.linspace(0, ncorr-1, ncorr)
plt.plot( times, acf, 'k-' )
plt.xlabel("time / arbitrary units")
plt.ylabel("velocity autoccoreation function")
plt.savefig("vacf.png")
