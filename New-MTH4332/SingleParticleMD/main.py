# Exercise 1
def potential(x) :
  energy=0
  # Your code to calculate the potential goes here
  return x*x/2
# Here are a few calls of the potential function
print( potential(0), potential(1), potential(2) )

# Exercise 2
def potential(x) :
  energy = 0.5*x*x
  force = -x
  return energy, force
# This calculates and force and prints the energy of the configuration in the input file.
pot, force = potential(-1)
print( "The potential at x=-1 is", pot, "and the force is", force )
pot, force = potential(0)
print( "The potential at x=0 is", pot, "and the force is", force )
pot, force = potential(1)
print( "The potential at x=1 is", pot, "and the force is", force )

# Exercise 3
def potential(x) :
  energy = 0.5*x*x
  forces = -x
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
  # I have stored the trajectory here so we can plot how the positions 
  # of each of the atoms changes with time.  
  if step%stride==0 :
    trajectory[int(step/stride)] = pos
# This will plot how position of the atoms during trajectory
times = np.linspace( 0, (nsteps-stride)*timestep, len(trajectory) )
plt.plot( times, trajectory, 'ko'  )
plt.xlabel("time")
plt.ylabel("position")
plt.plot()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 4
def kinetic( vel ) :
  ke = sum( vel*vel ) / 2
  return ke
# This command sets the velocities of the particles to 10 ranom numbers 
vel = np.random.normal(size=10)
# This prints out the total kinetic energy of the atoms whose velocities are specified 
# in vel.  
print( kinetic( vel ) )

# Exercise 5
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
plt.plot() 
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 6
def gen_vel(temp) :
  #Your code goes here
  vel = np.random.normal()*np.sqrt(temp)
  return vel
# To test your code I have written the following code, which will generate multiple
# random initial velocities and illustrate the distribution of values for these 
# velocities
velocities = np.zeros(1000)
for i in range(1000) : velocities[i] = gen_vel(1.0)
plt.hist( velocities )
plt.savefig("velocity_dist.png")

# Exercise 7
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
plt.plot() 
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 8
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
# This is the variable that you should use to keep track of the quantity of energy that is exchanged with 
# the reservoir of the thermostat.
therm = 0
therm1 = np.exp( -friction*timestep / 2 )
therm2 = np.sqrt( temperature*(1-therm1*therm1) )
# We now run 500 steps of molecular dynamics
nsteps, stride = 500, 10
times = np.zeros(int(nsteps/stride))
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
  eng, forces = eng, forces = potential(pos)
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
    conserved_quantity[int(step/stride)] = eng + kinetic(vel) + therm
# This will plot the kinetic energy as a function of time
plt.plot( times, conserved_quantity, 'r-' )
plt.ylim([min(conserved_quantity)-0.05, max(conserved_quantity)+0.05 ])
plt.xlabel('time')
plt.ylabel('conserved quantity / energy units')
plt.plot() 
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 9
average = sum(eng) / len(eng)

# Exercise 10
# Create a list with 10 elements that you will use to hold the average eneriges
av_eng = np.zeros(10)
# Your code goes here
bsize = int( len(eng) / 10 )
for i in range(10) :
    av_eng[i] = sum( eng[bsize*i:bsize*(i+1)] ) / bsize
x = np.linspace(1,10,10)
plt.plot( x, av_eng, "ko")
plt.xlabel("Index")
plt.ylabel("Average energy / natural units")
plt.plot()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 11
# Create a list with 10 elements that you will use to hold the variances
eng2 = eng*eng
variances = np.zeros(10)
# Your code goes here
for i in range(10) :
    mean = sum( eng[100*i:100*(i+1)] ) / 100
    mean2 = sum( eng2[100*i:100*(i+1)] ) / 100
    variances[i] = (100/99)*( mean2 - mean*mean )
mean = sum( eng ) / len(eng)
mean2 = sum( eng2 ) / len(eng)
total_var = (len(eng)/(len(eng)-1))*( mean2 - mean*mean )
# This will draw a graph of your variances
x = np.linspace( 1, 10, 10 )
plt.plot( x, variances, 'ko')
plt.plot( [1,10], [total_var,total_var], 'r-' )
plt.xlabel("Index")
plt.ylabel("Variance / energy^2")
plt.plot()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca() 

# Exercise 12
# Create a list to hold the block averages
blocks = np.zeros(10)
# Your code goes here
k=0
for i in range( len(eng) ) :
  blocks[k] = blocks[k] + eng[i]
  if (i+1)%100==0 and i>0 :
    blocks[k] = blocks[k] / 100
    k = k + 1
mean, sq = 0, 0
for bb in blocks : mean, sq = mean + bb, sq + bb*bb
average, sq = mean / len(blocks), sq / len(blocks)
var = ( len(blocks) / ( len(blocks) - 1 ) ) * ( sq - average*average )
error = np.sqrt( var / len(blocks) )
print( average, error )

# Exercise 13 
def block_average( M, data ) :
  # Your code goes here
  nblocks = int( np.floor(len(data) / M) )
  blocks = nblocks*[0]
  k=0
  for i in range( len(eng) ) :
    blocks[k] = blocks[k] + eng[i]
    if (i+1)%M==0 and i>0 :
      blocks[k] = blocks[k] / M
      k = k + 1
  mean, sq = 0, 0
  for bb in blocks : mean, sq = mean + bb, sq + bb*bb
  average, sq = mean / len(blocks), sq / len(blocks)
  var = ( len(blocks) / ( len(blocks) - 1 ) ) * ( sq - average*average )
  error = np.sqrt( var / len(blocks) )
  return error
i, errors, block_sizes = 0, 10*[0], [10,20,30,40,60,100,120,200,300,400]
for bb in block_sizes :
  errors[i] = block_average( bb, eng )
  i = i + 1
# And plot a graph
plt.plot( block_sizes, errors, 'k.-' )
plt.xlabel("Size of blocks")
plt.ylabel("Error")
plt.plot()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 14
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
plt.plot() 
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 15
# Set the initial position for the particle (you can change as I assume the initial particle is at init_pos when I test your code)
init_pos, init_vel = 3, 1
# This command runs the molecular dynamics and generates a trajectory 
temperature = 1.0   # This variable must be defined to pass the tests
# Generate the trajectories.  Please do not change the names of the variables on the left hand side of the 
# equals sign here.  I look for variables with these names when I test your code
tt, potential_e, kinetic_e, total, conserved = gen_traj( init_pos, init_vel, 2400, 0.005, 1, temperature, 2.0 )
# This is the part to compute the block averages for the error estimation
# I use the variable called errors to test your code.  This should contain a 90% confidence limit on your estimate of the error
total2, bsize, averages, errors = total*total, [200,400,600,800,1000,1200], np.zeros(6), np.zeros(6)
for i, blocksize in enumerate(bsize) :
  # Your code to calculate the block averages goes here
  nblocks = int( len(total2) / blocksize )
  for j in range(nblocks) :
    av = sum( total2[j*blocksize:(j+1)*blocksize] ) / blocksize
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
plt.plot()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 16
cv_temperatures, cv = np.zeros(9), np.zeros(9)
# Your code to calculate the values of the heat capacity goes here
for i in range(9) :
   cv_temperatures[i] = (temperatures[i] + temperatures[i+1])/2
   cv[i] = (energies[i+1]-energies[i]) /(temperatures[i+1]-temperatures[i])
# This will plot a graph of the heat capacity as a function of temperature
plt.plot( cv_temperatures, cv, 'ko' )
plt.xlabel("temperature / natural units")
plt.ylabel("heat capacity / natural units")
plt.plot()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 17
cv_temperatures, cv, cv_errors = np.zeros(9), np.zeros(9), np.zeros(9)
# Your code to calculate the values of the heat capacity and the errors goes here
for i in range(9) :
   cv_temperatures[i] = (temperatures[i] + temperatures[i+1]) / 2
   cv[i] = (energies[i+1]-energies[i]) / (temperatures[i+1]-temperatures[i])
   cv_errors[i] = ( error_energies[i+1] + error_energies[i] ) / ( temperatures[i+1] - temperatures[i] )

# This will plot a graph of the heat capacity as a function of temperature
plt.errorbar( cv_temperatures, cv, yerr=cv_errors, fmt='ko' )
plt.xlabel("temperature / natural units")
plt.plot()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()plt.ylabel("heat capacity / natural units")

# Exercise 18
cv_temperatures, cv = np.zeros(10), np.zeros(10)
# Your code to calculate the values of the heat capacity and the errors goes here
for i in range(10) :
   cv_temperatures[i] = temperatures[i]
   cv[i] = ( energies2[i] - energies[i]*energies[i] ) / ( temperatures[i]*temperatures[i] )
# This will plot a graph of the heat capacity as a function of temperature
plt.plot( cv_temperatures, cv, 'ko' )
plt.xlabel("temperature / natural units")
plt.ylabel("heat capacity / natural units")
plt.plot()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()plt.ylabel("heat capacity / natural units")

# Exercise 19
# These are the lists that hold the temperatures at which the 
# heat capacity has been computed and the values that you obtained for 
# the heat capacity.
cv_temperatures, cv, cv_errors = np.zeros(10), np.zeros(10), np.zeros(10)
# Your code to calculate the values of the heat capacity and the errors goes here
for i in range(10) :
  cv_temperatures[i] = temperatures[i]
  cv[i] = ( energies2[i] - energies[i]*energies[i] ) / ( temperatures[i]*temperatures[i] )
  cv_errors[i] = ( error_energies2[i] + 2*energies[i]*error_energies[i] ) / ( temperatures[i]*temperatures[i] )
# This will plot a graph of the heat capacity as a function of temperature
plt.errorbar( cv_temperatures, cv, yerr=cv_errors, fmt='ko' )
plt.xlabel("temperature / natural units")
plt.ylabel("heat capacity / natural units")
plt.plot()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()plt.ylabel("heat capacity / natural units")

# Exercise 20
# Lets first define some symbols
# x = position of particle
# p = momentum of particle
# T = temperature 
x, p, T  = sy.Symbol("x"), sy.Symbol("p"), sy.Symbol("T", real=True, positive=True )
# Now calculate the partition function 
# First the hamiltonian
H = x**4 + p*p / 2
# And the boltzmann weight
f = sy.exp( - H / T )
# Now integrate along p
pint = sy.integrate( f, (p,-sy.oo,sy.oo) )
# and integrate the result from the last step along x to get Z
Z = sy.integrate( pint, (x,-sy.oo,sy.oo) )
print("The partition function is", Z )
# Now get the ensemble average for the energy by differentiating log(Z) with respect to beta
E = (T**2)*sy.diff( sy.log(Z), T )
print("The ensemble average of the energy is", E )
# And finally get the heat capcity
# N.B I test that the variable with this value has the correct value when I test your code
CV = sy.diff( E, T )
print("The heat capacity is", CV )
