import numpy as np

def hamiltonian( spins ) :
    # Your code for calculating the hamiltonian described in the instruction goes here
    Ene = 0 
    for i in range(spins.shape[0]) :
        for j in range(spins.shape[1]) :
            Ene = Ene + spins[i,j]*( spins[ (i+1)%spins.shape[0], j] + spins[ i, (j+1)%spins.shape[1]] + spins[(i-1)%spins.shape[0], j] + spins[ i, (j-1)%spins.shape[1]] )
    return Ene / 2   

# The rest of this code is just to check if you code is doing something sensible
spins = np.ones([10,10])
print("The energy of the all up state is", hamiltonian( spins ) )
spins = -1*spins
print("The energy of the all down state is", hamiltonian( spins ) )
