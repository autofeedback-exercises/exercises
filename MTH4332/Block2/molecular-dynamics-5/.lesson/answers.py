import matplotlib.pyplot as plt
import numpy as np

def potential(x) :
  energy = x*x / 2 
  forces = -x
  return energy, forces
  
def kinetic(v) :
  ke = v*v / 2
  return ke

# Set the initial position for the particle (you can change as I assume the initial particle is at init_pos when I test your code)
init_pos, init_vel = 3, 1
# This is the value to use for the timestep (the delta in the equations on the other side)
timestep = 0.005
# Now set the position equal to the inial position that was set above
pos, vel = init_pos, init_vel
# This calculates the initial values for the forces
eng, forces = potential(pos)

# We now run 500 steps of molecular dynamics
nsteps, stride = 500, 10
times = np.zeros(int(nsteps/stride))
k_energy = np.zeros(int(nsteps/stride))
p_energy = np.zeros(int(nsteps/stride))
t_energy = np.zeros(int(nsteps/stride))
for step in range(nsteps) :
  # First update the velocities a half timestep
  # fill in the blanks in the code here
  vel = vel + 0.5*timestep*forces
    
  # Now update the positions using the new velocities
  # You need to add code here
  pos = pos + timestep*vel
  
  # Recalculate the forces at the new position
  # You need to add code here
  eng, forces = potential(pos)
  
  # And update the velocities another half timestep
  # You need to add code here
  vel = vel + 0.5*timestep*forces

  # This is where we want to store the energies and times
  if step%stride==0 : 
    times[int(step/stride)] = step
    p_energy[int(step/stride)] = eng 
    # Write code to ensure the proper values are saved here
    k_energy[int(step/stride)] = kinetic(vel)
    t_energy[int(step/stride)] = p_energy[int(step/stride)] + k_energy[int(step/stride)]
  
 
# This will plot the potential, kinetic and total energy as a function of 
# time
plt.plot( times, p_energy, 'b-', label='potential' )
plt.plot( times, k_energy, 'r-', label='kinetic' )
plt.plot( times, t_energy, 'k-', label='total' )
plt.xlabel('time')
plt.ylabel('energy')
plt.savefig( "energies.png" )
