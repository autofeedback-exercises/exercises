import numpy as np

def microstate_energies( N ) : 
   # Create an array to hold the energies of all the microstates
   energies = np.zeros( 2**N ) 
   for i in range(2**N) :
       # Generate coordinates of particles for ith microstate

       # Evaluate the energy of the microstate and store it in the array that we will return
       energies[i] = 

   # Return the array that holds the energies of the microstates
   return energies
