import numpy as np

def magnetisation( spins ) :
    # Your code for calculating the magnetistation goes here
    return sum( sum(spins) ) / ( spins.shape[0]*spins.shape[1] )   

# The rest of this code is just to check if you code is doing something sensible
spins = np.ones([10,10])
print("The magneitation of the all up state is", magnetisation( spins ) )
spins = -1*spins
print("The magneitation of the all down state is", magnetisation( spins ) )
