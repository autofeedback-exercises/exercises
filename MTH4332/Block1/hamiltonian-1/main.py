def hamiltonian( spins, H ) :
  energy = 0
  # Your code goes here
  
  return energy 
  
allup, alldown = 10*[1], 10*[-1]
print( "ENERGY FOR ALL SPIN UP", hamiltonian( allup, 1 ) )
print( "ENERGY FOR ALL SPIN DOWN", hamiltonian( alldown, 1 ) )
