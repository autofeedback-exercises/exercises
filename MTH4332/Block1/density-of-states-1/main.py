import matplotlib.pyplot as plt 
import numpy as np 

def hamiltonian( spins, H ) :
  eng = 0
  # Your code to calculate the Hamiltonian goes here
  
  return eng

# Generate an index for each microstate
indices = np.zeros(2**8)
for i in range(2**8) : indices[i] = i 

energies = np.zeros(2**8)
for index in indices :
  spins, ind = np.zeros(8), index 
  # Your code to convert the integer index to the corresponding spin coordinates goes here
  
  energies[int(index)] = hamiltonian( spins, 1 )

# This will plot the energies of the configurations against their numerical indexes. 
plt.plot( indices, energies, 'ko')
plt.xlabel("numerical index")
plt.ylabel("energy")
plt.savefig( "index_versus_energy.png")
