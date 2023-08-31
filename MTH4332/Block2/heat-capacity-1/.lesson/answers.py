import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

def potential(x) :
  energy = x*x/2 
  forces = -x
  return energy, forces
  
def kinetic(v) :
  ke = v*v/2
  return ke

def gen_traj( pos, vel, nsteps, timestep, stride, temperature, friction ) :
  # This calculates the initial values for the forces
  eng, forces = potential(pos)
  # This is the variable that you should use to keep track of the quantity of energy that is exchanged with 
  # the reservoir of the thermostat.
  therm = 0
  therm1 = np.exp( -friction*timestep / 2 )
  therm2 = np.sqrt( temperature*(1-therm1*therm1) )  

  times = np.zeros(int(nsteps/stride))
  k_energy = np.zeros(int(nsteps/stride))
  p_energy = np.zeros(int(nsteps/stride))
  t_energy = np.zeros(int(nsteps/stride))
  conserved_quantity = np.zeros(int(nsteps/stride))
  for step in range(nsteps) :
    # Apply the thermostat for a half timestep 
    therm = therm + kinetic(vel)
    vel = vel*therm1 + therm2*np.random.normal()
    therm = therm - kinetic(vel) 
  
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
    therm = therm + kinetic(vel)
    vel = vel*therm1 + therm2*np.random.normal()
    therm = therm - kinetic(vel)

    # This is where we want to store the energies and times
    if step%stride==0 : 
      times[int(step/stride)] = step*timestep
      # Write code to ensure the proper values are saved here
      p_energy[int(step/stride)] = eng
      k_energy[int(step/stride)] = kinetic(vel)
      t_energy[int(step/stride)] = eng + kinetic(vel)
      conserved_quantity[int(step/stride)] = eng + kinetic(vel) + therm
      
  return times, p_energy, k_energy, t_energy, conserved_quantity
  
# Set the initial position for the particle (you can change as I assume the initial particle is at init_pos when I test your code)
init_pos, init_vel = 3, 1  
# This command runs the molecular dynamics and generates a trajectory 
temperature = 1.0   # This variable must be defined to pass the tests

# Generate the trajectories.  Please do not change the names of the variables on the left hand side of the 
# equals sign here.  I look for variables with these names when I test your code
tt, potential_e, kinetic_e, total, conserved = gen_traj( init_pos, init_vel, 2400, 0.005, 1, temperature, 2.0 )

# This is the part to compute the block averages for the error estimation
# I use the variable called errors to test your code.  This should contain a 90% confidence limit on your estimate of the error
bsize, averages, errors = [200,400,600,800,1000,1200], np.zeros(6), np.zeros(6)
for i, blocksize in enumerate(bsize) :
  # Your code to calculate the block averages goes here
  nblocks = int( len(total) / blocksize )
  for j in range(nblocks) :
    av = sum( total[j*blocksize:(j+1)*blocksize] ) / blocksize
    averages[i] = averages[i] + av
    errors[i] = errors[i] + av*av
  averages[i] = averages[i] / nblocks
  errors[i] = (nblocks / (nblocks-1))*( errors[i] / nblocks - averages[i]*averages[i] )
  errors[i] = np.sqrt( errors[i] / nblocks )*st.norm.ppf((1+0.90)/2)
  i=i+1 
   
# This will plot the kinetic energy as a function of time
plt.errorbar( bsize, averages, yerr=errors, fmt='ko' )
plt.xlabel("Length of block")
plt.ylabel("Average energy / natural units")
plt.savefig( "average_energy.png" )
