import numpy as np

def microstate_energies( N ) : 
   # Create an array to hold the energies of all the microstates
   energies = np.zeros( 2**N ) 
   for i in range(2**N) :
       # Generate coordinates of particles for ith microstate
       val, coords = i, np.zeros(N)
       for j in range(N) : 
           ppp = 2**(N-1-j)
           coords[j] = np.floor( val / ppp )
           val = val - ppp*coords[j] 
           if coords[j]==0 : coords[j] = -1 
       # Evaluate the energy of the microstate and store it in the array that we will return
       energies[i] = sum(coords)

   # Return the array that holds the energies of the microstates
   return energies
