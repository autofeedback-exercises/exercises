import numpy as np

def kinetic( vel ) :
  ke = 0
  # Your code to calculate the kinetic energy should go here
  
  return ke

# This command sets the velocities of the particles to 10 ranom numbers 
vel = np.random.normal(size=10)
# This prints out the total kinetic energy of the atoms whose velocities are specified 
# in vel.  
print( kinetic( vel ) )
