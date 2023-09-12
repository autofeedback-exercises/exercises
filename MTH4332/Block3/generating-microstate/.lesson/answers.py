import numpy as np

def getstate(N) : 
    # Your code for generating the random microstate goes here
    spins = np.ones([N,N])
    for i in range(N) : 
        for j in range(N) :
            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1
    return spins        

# You don't need to adjust this code.  It is just here
# so you can look at what your function is generating.
# This will generate a state for a 4x4 lattice of spins
print( "Random 4x4 state", getstate(4) )  
# This will generate a state for a 5x4 lattice of spins
print( "Random 4x4 state", getstate(5) )  
