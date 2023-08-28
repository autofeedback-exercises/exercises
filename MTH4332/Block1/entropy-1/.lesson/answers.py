import matplotlib.pyplot as plt 
import numpy as np 

def hamiltonian( spins, H ) :
  eng = -H*sum(spins)
  return eng
  
# Create a list of the posssible values the energy can take
energies = np.zeros(9) 
for i in range(9) : energies[i] = -8+i*2

# Create a list that will hold the number of microstates with each energy 
number_of_microstates = np.zeros(9) 
# Your code to do the loop over all the microstates and to count how many times each 
# of the energy values appear goes here
for i in range(2**8) : 
    vv, spins = i, np.zeros(8)
    for j in range(8) :
        ppp = 2**(7-j)
        spins[j] = np.floor( vv / ppp )
        vv = vv - spins[j]*ppp
        if spins[j]==0 : spins[j] = -1
    eng = hamiltonian( spins, 1 )
    number_of_microstates[ int((eng + 8)/2) ] = number_of_microstates[ int((eng + 8)/2) ] + 1

entropy = np.log( number_of_microstates )  

# This will plot the possible values for the energy against the number of microstates with 
# that particular energy.
plt.bar( energies, entropy, width=0.1 )
plt.xlabel("energy")
plt.ylabel("Entropy")
plt.savefig( "entropy.png")
