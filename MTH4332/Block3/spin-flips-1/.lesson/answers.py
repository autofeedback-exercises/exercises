import numpy as np

def flipSpin( spins, i, j ) : 
    # Your code to flip the spin in the (i,j) position of the lattice goes here
    spins[i,j] = -1*spins[i,j]
    return spins

def flipAllSpins( spins ) :
    # Your code to flip all the spins goes here
    spins = -1*spins
    return spins

def chooseMove( spins ) : 
    # Your code to choose whether to flip all or one of the spins goes here
    if np.random.uniform(0,1) < 1/(1+spins.shape[0]*spins.shape[1]) : return 1
    return 0 

def chooseSpin( spins ) :
    # Your code to choose a particular spin to flip goes here
    ispin = np.floor( spins.shape[0]*np.random.uniform(0,1) )
    jspin = np.floor( spins.shape[0]*np.random.uniform(0,1) )
    return ispin, jspin

# You may want to add code here to test your functions
