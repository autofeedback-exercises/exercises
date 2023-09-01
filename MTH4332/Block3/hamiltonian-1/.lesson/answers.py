import numpy as np

def hamiltonian( spins, H ) :
    # Your code for calculating the hamiltonian described in the instruction goes here
    return -H*sum( sum( spins ) )   

# The rest of this code is just to check if you code is doing something sensible
spins = np.ones([10,10])
print("The energy of the all up state is", hamiltonian( spins, -1 ) )
print("The energy of the all up state is", hamiltonian( spins, +1 ) )
spins = -1*spins
print("The energy of the all down state is", hamiltonian( spins, -1 ) )
print("The energy of the all down state is", hamiltonian( spins, +1 ) )
