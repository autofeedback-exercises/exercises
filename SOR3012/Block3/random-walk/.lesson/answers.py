import numpy as np

def random_walk( startpoint, nsteps, p ) :
    for i in range(nsteps) : 
        if np.random.uniform(0,1)<p : startpoint = startpoint + 1 
        else : startpoint = startpoint - 1
    return startpoint   
