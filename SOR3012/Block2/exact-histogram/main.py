import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

# This sets the x-coordinates for your bar charts
xvals = np.linspace(0,6,7) 

# Your code for setting the values in uniform_pmf and binom_pmf goes here




# This is the part for plotting the probablity mass functions
# side by side.  Notice that the x-coordinates
# define the position of the centers of the bars.  You 
# thus get the center of the two side by side bars to appear at 
# the coordinates in xvals by shifting one set of bars left
# by half the width of the bar and the other set of bars 
# right by half the width of the bar.
plt.bar( xvals-0.05, uniform_pmf, width=0.1, color="blue" )
plt.bar( xvals+0.05, binom_pmf, width=0.1, color="red" )
plt.xlabel("x")
plt.ylabel("P(X=x)")
plt.savefig("exact_probablity_mass.png")
