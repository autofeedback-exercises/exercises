import matplotlib.pyplot as plt 
import numpy as np 

def hamiltonian( spins, H ) :
  eng = 0
  # Your code to calculate the Hamiltonian goes here
  
  return eng
  
# Create a list of the posssible values the energy can take
energies = np.zeros(9) 
for i in range(9) : energies[i] = -8+i*2

# Create a list that will hold the number of microstates with each energy 
number_of_microstates = np.zeros(9) 
# Your code to do the loop over all the microstates and to count how many times each 
# of the energy values appear goes here


# use the number of microstates array to calculate the entropy
  
# This will plot the possible values for the energy against the number of microstates with 
# that particular energy.
plt.bar( energies, entropy, width=0.1 )
plt.xlabel("energy")
plt.ylabel("Entropy")
plt.savefig( "entropy.png")
