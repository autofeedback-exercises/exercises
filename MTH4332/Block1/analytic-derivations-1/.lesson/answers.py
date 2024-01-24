import matplotlib.pyplot as plt
import sympy as sy
import numpy as np

# Define symbols that we will use to represent:
# N = number of particles
# B = 1/T where T is temperature
N, B = sy.symbols("N B")
# One particle partition function
Z1 = 1 + sy.exp(-B) + sy.exp(-3*B ) 
# N particle partition function
ZN = Z1**N
# Now ensemble average of the energy 
# sy.diff calculates the derivative with respect to B
E = -sy.diff( sy.log(ZN), B ) 

print("The ensemble average for the energy can be calculated using", E )

# Lets now draw a graph of this result using matplotlib and NumPy
# We are setting H=1 and N=8 here
temperatures = np.linspace(0.1,3,100)
energies = -8*( -np.exp(-1/temperatures ) - 3*np.exp(-3/temperatures) )/ (1  + np.exp(-1/temperatures) + np.exp(-3/temperatures) ) 

plt.plot( temperatures, energies, 'k-' )
plt.xlabel('temperature')
plt.ylabel('average energy')
plt.savefig("analytic_graph.png")

