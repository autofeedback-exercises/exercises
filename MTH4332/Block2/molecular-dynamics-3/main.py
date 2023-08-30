import matplotlib.pyplot as plt
import numpy as np

def potential(x) :
  energy = 0 
  
  return energy, forces

# Set the initial position for the particle (you can change as I assume the initial particle is at init_pos when I test your code)
init_pos, init_vel = 3, 1
# This is the value to use for the timestep (the delta in the equations on the other side)
timestep = 0.005
# Now set the position equal to the inial position that was set above
pos, vel = init_pos, init_vel
# This calculates the initial values for the forces
eng, forces = potential(pos)

# We now run 500 steps of molecular dynamics
nsteps = 500
# And store every 10th frame
stride = 10
trajectory = np.zeros([int(nsteps/stride)])
for step in range(nsteps) :
  # First update the velocity a half timestep
  # fill in the blanks in the code here
  vel = 
    
  # Now update the positions using the new velocities
  # You need to add code here
  pos = 
  
  # Recalculate the forces at the new position
  # You need to add code here
  eng, forces = 
  
  # And update the velocities another half timestep
  # You need to add code here


  # I have stored the trajectory here so we can plot how the positions 
  # of each of the atoms changes with time.  
  if step%stride==0 : 
    trajectory[int(step/stride)] = pos
 
# This will plot how position of the atoms during trajectory
times = np.linspace( 0, (nsteps-stride)*timestep, len(trajectory) )
plt.plot( times, trajectory, 'ko'  )
plt.xlabel("time")
plt.ylabel("position")
plt.savefig( "trajectory.png" )
