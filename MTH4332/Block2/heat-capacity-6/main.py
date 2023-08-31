import matplotlib.pyplot as plt
import numpy as np

# This loads the data from the input file and generates the lists 
# that are described in the text on the right.
data = np.loadtxt("md_results.txt")
temperatures = data[:,0]
energies = data[:,1]
error_energies = data[:,2]
energies2 = data[:,3]
error_energies2 = data[:,4]

# These are the lists that hold the temperatures at which the 
# heat capacity has been computed and the values that you obtained for 
# the heat capacity.
# N.B. I check that the variables in cv_errors have been computed correctly
# when I run tests.  Please ensure that there is a variable with this name in your code
cv_temperatures, cv, cv_errors = np.zeros(10), np.zeros(10), np.zeros(10)

# Your code to calculate the values of the heat capacity and the errors goes here


# This will plot a graph of the heat capacity as a function of temperature
plt.errorbar( cv_temperatures, cv, yerr=cv_errors, fmt='ko' )
plt.xlabel("temperature / natural units")
plt.ylabel("heat capacity / natural units")
plt.savefig("heat_capacity.png")
