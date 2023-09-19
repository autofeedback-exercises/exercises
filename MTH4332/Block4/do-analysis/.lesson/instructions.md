# Analysing the MD trajectories

The `main.py` file that you have for this exercise is very similar to the one you had in the previous exericse.
To complete this exericse you are thus going to have to consolidate what you learned in the last exercise 
and copy the codes that you have just written for calculating the Lennard Jones energies and forces, initialising
the MD trajectory and running Langevin dynamics.

As you have seen in previous exercises, just running molecular dynamics caclulations is pointless.  You also need to do
some analysis of the trajectories that are generated and compute some averages.  When we use a code like ASE there are two
ways we can do this analysis:

1. We can modify what is done in the main MD loop for ASE and calculate the quantities that interest us "on the fly".  When you wrote your MD and MC codes for the previous assignments this is what you did.

2. We can save the trajectory that ASE generates to a file.  We can then read this trajectory after the MD simulation is completed and analyse it.

The other exercises for the readings for this assignments will teach you how to analyse the trajectory files that are output when you do (2) 
(this way makes it easier for me to autograde your work).  However, when you come to doing the assignments you may prefer to use method (1) so I will 
show you how to modify ASE's MD loop here as well.

You can ensure that a function is called after every 10 steps of MD by using code like the one below:

```python
# Code to initalise the structure and velocites in atoms needs to go here.

# Code to setup the routines for calculating the energies and forces goes here.

# Now that we have setup our initial positions and our routines for calculating energies and forces
# we can setup an object that does will allow us to do as much Langevin dynamics as we want.
# When we do this Langevin dynamics we will be running simulations with k_B T = 2, a timestep of 0.005 and a thermostat friction of 1.0 here.
dyn = Langevin( atoms, 0.005, 2.0, 1.0 )

# We now create an empty list that is going to hold snapshots of data we are collecting from the trajectory
stats = []

# When this function is called the current value of the potential energy is appended to the array stats
def printenergy(stats = stats, a=atoms ):
    stats.append( a.get_potential_energy() )

# This command ensures that the function printenergy above is called every 10 seconds of MD
dyn.attach( printenergy, interval=10 )
# And run 1000 steps of Langevin dynamics
dyn.run(1000)
``` 

This code calculates the energy potential energy on every 10th MD step and appends these values to the list called stats.  To do this 
we use the `dyn.attach` method from ASE to tell it that it should call the function printenergy on every 10th MD step.  You can see that
this function just appends the instantaneous atom to the list called stats.

To output the trajectory we do something similar.  The only difference is that we use a function that is already part of ASE and that is 
one of the methods in the Trajectory object.  The code to output the trajectory to a file called moldyn3.traj is as follows:

```python
# Code to initalise the structure and velocites in atoms needs to go here.

# Code to setup the routines for calculating the energies and forces goes here.

# Now that we have setup our initial positions and our routines for calculating energies and forces
# we can setup an object that does will allow us to do as much Langevin dynamics as we want.
# When we do this Langevin dynamics we will be running simulations with k_B T = 2, a timestep of 0.005 and a thermostat friction of 1.0 here.
dyn = Langevin( atoms, 0.005, 2.0, 1.0 )

# Create a trajectory object.  This opens the file on which we will output configurations
traj = Trajectory('moldyn3.traj', 'w', atoms)

# Attach the write method for the Trajectory object to the MD loop
dyn.attach( traj.write, interval=10 )

# And run 1000 steps of Langevin dynamics
dyn.run(1000)

# And close the trajectory file once we are done writing to it
traj.close()
```

Notice how this code uses the `dyn.attach` method to attach the `traj.write` method to the MD loop.  It is this that ensures that the trajectory
is output to the file every 10 MD steps.

__Your task in this exercise is to use ASE to write an MD code.  Your MD code should save the values the potential energy took on every 20th step to a 
NumPy array called `energies`.  Your code should also output the positions of all the atoms on every 20th step to a file called `mytraj.traj`.__ The energies
and forces should be calculated using the Lennard Jones potential with cutoff of 4 that you have encountered in previous exercises.  I will test your code by ensuring that 
the energies in the NumPy array `energies` are consistent with energies of the configurations that are output in `mytraj.traj`.

