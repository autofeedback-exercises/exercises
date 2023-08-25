import numpy as np

def hamiltonian( coords ) :
  energy = 0
  # Your code goes here
  
  return energy 
  
allzero, allone, alltwo, allthree = np.zeros(10), np.ones(10), 2*np.ones(10), 3*np.ones(10)
print( "ENERGY FOR ALL ZERO", hamiltonian( allzero ) )
print( "ENERGY FOR ALL ONE", hamiltonian( allone ) )
print( "ENERGY FOR ALL TWO", hamiltonian( alltwo ) )
print( "ENERGY FOR ALL THREE", hamiltonian( allthree ) )
