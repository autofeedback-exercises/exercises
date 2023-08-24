import numpy as np

nspins = 10 

allup = np.ones(nspins)

alldown = -1*np.ones(nspins)

alternating = np.ones(nspins)
for i in range(nspins) :
    if i%2==0 : alternating[i]=-1
