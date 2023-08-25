import numpy as np

def hamiltonian( spins, H ) :
  energy = 0
  # Your code goes here
  
  return energy 
  
allup, alldown = np.ones(10), -1*np.ones(10) 
print( "ENERGY FOR ALL SPIN UP", hamiltonian( allup, 1 ) )
print( "ENERGY FOR ALL SPIN DOWN", hamiltonian( alldown, 1 ) )
