import matplotlib.pyplot as plt
import numpy as np

def hamiltonian( spins, H ) : 
  energy = 0
  # Your code to calculate the hamiltonian goes here
  
  return energy
  
def ensemble_average( N, H, T ) :
  numerator, Z = 0, 0
  # Your code to calculate the partition function goes here
  
  return numerator / Z
  
energies, k = np.zeros(15), 0
temperatures = np.linspace(0.1,3.1,15)
for temp in temperatures : 
    energies[k] = ensemble_average(8, 1., temp) 
    k = k + 1
plt.plot( temperatures, energies, 'k-' )
plt.xlabel("temperature / arbitrary units")
plt.ylabel("average energy / arbitrary units")
plt.savefig("average_energy.png")
