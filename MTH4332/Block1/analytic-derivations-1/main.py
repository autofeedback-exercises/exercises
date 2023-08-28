import matplotlib.pyplot as plt
import sympy as sy
import numpy as np

# Define symbols that we will use to represent:
# N = number of particles
# H = magnetic field strength
# B = 1/T where T is temperature
N, H, B = sy.symbols("N H B")
# One particle partition function
Z1 = sy.cosh( B*H ) 
# N particle partition function
ZN = Z1**N
# Now ensemble average of the energy 
# sy.diff calculates the derivative with respect to B
E = -sy.diff( sy.log(ZN), B ) 

print("The ensemble average for the energy can be calculated using", E )

# Lets now draw a graph of this result using matplotlib and NumPy
# WE are setting H=1 and N=8 here
temperatures = np.linspace(0.1,3,100)
energies = -8*np.sinh( 1/temperatures ) / np.cosh( 1/temperatures )

plt.plot( temperatures, energies, 'k-' )
plt.xlabel('temperature')
plt.ylabel('average energy')
plt.savefig("analytic_graph.png")

