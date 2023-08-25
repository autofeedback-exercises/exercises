import numpy as np

def hamiltonian( coords ) :
  energy = 0
  # Your code goes here
  for c in coords : 
      if c==1 : energy = energy + 2
      elif c==2 : energy = energy + 3 
  return energy 
  
allzero, allone, alltwo = np.zeros(10), np.ones(10), 2*np.ones(10)
print( "ENERGY FOR ALL ZERO", hamiltonian( allzero ) )
print( "ENERGY FOR ALL ONE", hamiltonian( allone ) )
print( "ENERGY FOR ALL TWO", hamiltonian( alltwo ) )
