import numpy as np

def hamiltonian( spins, H ) : 
  energy = 0
  # Your code to calculate the hamiltonian goes here
  
  return energy
  
def partitionfunction( N, H, T ) :
  Z = 0
  # Your code to calculate the partition function goes here
  
  return Z

# Calculate the partition function for a system of 5 spins 
# with no external field at a temperature of 0.1
print( partitionfunction(5,0,0.1) )

# Calculate the paritition function for a system of 6 spins 
# with a magnetic field strength of 1 at a temperature of 0.5
print( partitionfunction(6,1,0.5) )
