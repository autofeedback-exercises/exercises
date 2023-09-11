import numpy as np

def hamiltonian( spins, H ) :
    # Your code to calculate the energy of Ising model configuration in the
    # the NumPy array spins goes here
    Ene = 0 
    for i in range(spins.shape[0]) :
        for j in range(spins.shape[1]) :
            Ene = Ene + spins[i,j]*( spins[ (i+1)%spins.shape[0], j] + spins[ i, (j+1)%spins.shape[1]] + spins[(i-1)%spins.shape[0], j] + spins[ i, (j-1)%spins.shape[1]] )
    return - Ene / 2 - H*sum( sum( spins ) )


def new_energy( spins, E, H, move ) :
    # Your code to calculate the energy of the configuration in spins after 
    # the move indicated using the variable move goes here
    N = spins.shape[1]
    if move==N*N : 
       new_e = E + 2*H*sum( sum( spins ) )
    else :
       i, j = int( np.floor( move / N ) ), move%N
       new_e = E + 2*spins[i,j]*( spins[(i+1)%N,j] + spins[(i-1)%N,j] + spins[i,(j-1)%N] + spins[i,(j+1)%N] + H )

    return new_e 


# You might want to add some test code here to test your functions before
# running the tests
