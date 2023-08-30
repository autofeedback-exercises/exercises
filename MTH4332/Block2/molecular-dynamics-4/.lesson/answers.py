import numpy as np

def kinetic( vel ) :
  ke = sum( vel*vel ) / 2
  return ke

# This command sets the velocities of the particles to 10 ranom numbers 
vel = np.random.normal(size=10)
# This prints out the total kinetic energy of the atoms whose velocities are specified 
# in vel.  
print( kinetic( vel ) )
