import numpy as np

def nplays( s, n, p ) : 
    nt = 0
    while( s>0 and s<n ) :
        nt = nt+1
        if np.random.uniform(0,1)<p : s = s + 1 
        else : s = s - 1 
    return nt
