import numpy as np

def gambler( s, n, p ) :
    while( s>0 and s<n ) :
       if np.random.uniform(0,1)<p : s = s + 1
       else : s = s - 1

    if s==n : return 0 
    elif s==0 : return 1 
    else : assert(False)
