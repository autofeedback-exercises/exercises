import matplotlib.pyplot as plt
import numpy as np

# This loads the data from the input file and generates the lists 
# that are described in the text on the right.
data = np.loadtxt("md_results.txt")
temperatures = data[:,0]
energies = data[:,1]
error_energies = data[:,2]
energies2 = data[:,3]
error_energies = data[:,4]

# These are the lists that hold the temperatures at which the 
# heat capacity has been computed and the values that you obtained for 
# the heat capacity.
cv_temperatures, cv = np.zeros(9), np.zeros(9)

# Your code to calculate the values of the heat capacity goes here
for i in range(9) :
   cv_temperatures[i] = (temperatures[i] + temperatures[i+1])/2
   cv[i] = (energies[i+1]-energies[i]) /(temperatures[i+1]-temperatures[i])

# This will plot a graph of the heat capacity as a function of temperature
plt.plot( cv_temperatures, cv, 'ko' )
plt.xlabel("temperature / natural units")
plt.ylabel("heat capacity / natural units")
plt.savefig("heat_capacity.png")
