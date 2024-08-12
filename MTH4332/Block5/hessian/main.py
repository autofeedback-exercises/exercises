import matplotlib.pyplot as plt
import numpy as np
from pairwise_calc import *
from ase.optimize import BFGS
from ase.vibrations import Vibrations

def fff(r):
   # Insert your code to calculate the Lennard Jones energy and forces here

   return e, f  # First argument should be energy and second should be force

# Insert code to setup the initial structure here and to setup the function for calculating the potential energy

# Add the code required to do the optimisation that you were given in the instructions 

# Add the code from the instructions to calculate the Hessian matrix and the frequencies for the minimised structure
# the final line of this block of code should set the variable called frequencies equal to the frequencies that you 
# found from the hessian matrix

# Set this variable equal to the frequencies of the hessian
frequencies = 

# This sets up code for calculating a histogram with nbins bins that holds the density of states
# the range of frequncy values starts at slightly less than minfreq and end at slightly more than maxfreq
nbins = 100 
minfreq = min(frequencies)
maxfreq = max(frequencies)
delx = 1.01*(maxfreq- minfreq) / nbins
minx = mineng - (maxfreq-minfreq)*0.005

# Find the position of the center of each bin in the histogram
xvals = np.zeros(nbins) 
for i in range(nbins) : xvals[i] = minx + (i+0.5)*delx

# You now need to loop over the frequencies that emerged from the hessian and determine how many of these frequencies
# are in each bin of your histogram. The number of frequencies in each bin of the histogram should be accumulated in the 
# numpy array called histo below
histo = np.zeros(nbins)
    
    
# This will plot the final density of states for you
plt.plot( xvals, histo, 'k-')
plt.xlabel("frequencies / arbitrary units")
plt.ylabel("Number of states")
plt.savefig("density-of-states.png")
