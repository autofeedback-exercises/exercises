import matplotlib.pyplot as plt
import numpy as np

def hamiltonian(x) : 
    return x*x / 2

# Set the initial position of the particle, the number of frames,
# the maximum value to shift the position by and the temperature
pos, nframes, maxshift, temp = 0.0, 1000, 1.0, 1.0
# Calculate the energy at the start of the simulation
oldenergy = hamiltonian(pos)
# Set up some NumPy arrays to hold data
xvals, yvals = np.linspace(1,nframes,nframes), np.zeros(nframes)
for i in range(nframes) : 
    # Your code to generate random move goes here
    newpos = pos + maxshift*( 2*np.random.uniform(0,1) - 1 )
    newenergy = hamiltonian(newpos)
    # Your code for the accept reject criteria should go here
    if np.random.uniform(0,1)<min( 1.0, np.exp( -newenergy/temp ) / np.exp( -oldenergy/temp )  ) :
       oldenergy, pos = newenergy, newpos

    # You need to store the "time series" of energies in yval to pass the test
    yvals[i] = pos

# This generates the graph 
plt.plot( xvals, yvals, 'ko' )
plt.xlabel("index")
plt.ylabel("particle position")
plt.savefig("monte-carlo.png")
