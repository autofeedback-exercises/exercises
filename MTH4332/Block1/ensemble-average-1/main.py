import numpy as np

def hamiltonian( spins, H ) : 
  energy = 0
  # Your code to calculate the hamiltonian goes here
  
  return energy
  
def ensemble_average( N, H, T ) :
  numerator, Z = 0, 0
  # Your code to calculate the ensemble average goes here
  
  return numerator / Z

# Calculate the ensemble average of the energy for a system of 5 spins 
# with an external field of 1 at a temperature of 0.1
print( ensemble_average(5,0,1.1) )

# Calculate the ensemble average for a system of 6 spins 
# with a magnetic field strength of 1 at a temperature of 0.5
print( ensemble_average(6,1,0.5) )
