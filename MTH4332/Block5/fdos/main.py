from ase.io.trajectory import Trajectory
import matplotlib.pyplot as plt
import numpy as np

# This reads in the trajectory
ftraj = Trajectory('nve-short.traj')

# Your code to calculate the vibrational density of states goes here



# This command generates the xvalues at which your frequencies should be plotted here.
# d here is set equal to the time between adjacent frames in the trajectory
freqvals = np.fft.rfftfreq( len(ftraj), d=0.005 ) 
# This will generate the graph showing the vibrational density of states for you.
plt.plot( freqvals, fdos, 'k-' )
plt.xlabel("frequency / arbitrary units")
plt.ylabel("vibrational density of states")
plt.savefig("vdos.png")
