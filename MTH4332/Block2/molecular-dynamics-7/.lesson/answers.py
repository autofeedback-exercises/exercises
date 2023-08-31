import matplotlib.pyplot as plt
import numpy as np

def potential(x) :
  energy = x*x/2
  # Your code to calculate the potential goes here
  forces = -x
  return energy, forces
  
def kinetic(v) :
  ke = v*v / 2
  return ke

# Set the initial position for the particle (you can change as I assume the initial particle is at init_pos when I test your code)
init_pos, init_vel = 3, 1
# This is the value to use for the timestep (the delta in the equations on the other side)
timestep = 0.005
# This is the value of the temperature
temperature = 1.0 
# Now set the position equal to the inial position that was set above
pos, vel = init_pos, init_vel
# This is the value of the friction for the thermostate (the \gamma in the equations on the other side)
friction = 2.0
# This calculates the initial values for the forces
eng, forces = potential(pos)
therm1 = np.exp( -friction*timestep / 2 )
therm2 = np.sqrt( temperature*(1-therm1*therm1) )

# We now run 5000 steps of molecular dynamics
nsteps = 5000
stride=10
times = np.zeros(int(nsteps/stride))
vels = np.zeros(int(nsteps/stride))
for step in range(nsteps) :
  vel = vel*therm1 + therm2*np.random.normal()
  
  # Update the velocities a half timestep
  # fill in the blanks in the code here
  vel = vel + 0.5*timestep*forces
    
  # Now update the positions using the new velocities
  # You need to add code here
  pos = pos + timestep*vel
  
  # Recalculate the forces at the new position
  # You need to add code here
  eng, forces = potential(pos)
  
  # Update the velocities another half timestep
  # You need to add code here
  vel = vel + 0.5*timestep*forces

  # And finish by applying the thermostat for the second half timestep 
  vel = vel*therm1 + therm2*np.random.normal()

  # This is where we want to store the energies and times
  if step%stride==0 : 
    times[int(step/stride)] = step*timestep
    # Write code to ensure the proper values are saved here
    vels[int(step/stride)] = vel
   
   
# This will plot the kinetic energy as a function of time
plt.plot( times, vels, 'r-' )
plt.xlabel('time')
plt.ylabel('velocity')
plt.savefig( "velocity.png" )
