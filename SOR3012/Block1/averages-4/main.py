import matplotlib.pyplot as plt
import numpy as np

ssum, indices, average = 0, np.zeros(200), np.zeros(200)
for i in range(200) : 
  # Add code to setup the numpy arrays called indices and average to generate the desired
  # plot here.
  
  
  
# This will plot the graph for the data.  You should not need to adjust this.
plt.plot( indices, average, 'ro' )
plt.plot( [0,200], [0.5,0.5], 'k--' )
plt.xlabel("Number of random variables")
plt.ylabel("Sample mean")
plt.savefig("average.png")
