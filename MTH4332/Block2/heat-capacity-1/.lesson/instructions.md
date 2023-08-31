# The average energy and error bars

This exercise is going to teach you how we can calculate heat capacities from molecular dynamics simulation.  This first task is going to revise the material that was covered in the previous set of exercises on molecular dynamics simulation.  We will also review what you have learned about the method of block averaging.  The objective is to use molecular dynamics to calculate an estimate for the ensemble average of the energy.  As we are computing an estimate for the ensemble average for the energy, we must also compute suitable error bars for this estimate, and we will calculate these errors using block averaging.

You will notice that I have written an outline for a constant temperature MD code in `main.py`.  This outline should, by now be getting somewhat familiar, and you should by now know that to complete this code, you will need to:

1. Write a function called `potential` that computes the potential energy and the forces for each of the configurations you generate.
2. Write a function called `kinetic` that calculates the instantaneous kinetic energy.
3. Use your potential function to write code that uses the velocity Verlet algorithm and the thermostat to integrate the equations of motion.
4. Every stride MD steps store the instantaneous values of the potential, kinetic, total and conserved quantity in the lists called `p_energy`, `k_energy`, `t_energy` and `conserved_quantity`.

Notice that, at variance with what has been done in previous exercises, a function called `gen_traj` has been written.  This function generates the molecular dynamics trajectory and takes seven input arguments:

1. `pos` - the initial positions of the atoms
2. `vel` - the initial velocities of the atoms
3. `nsteps` - the number of steps in the trajectory that will be generated
4. `timestep` - the simulation timestep
5. `stride` - the frequency with which to store the energies - energies are stored every stride MD steps.
6. `temperature` - the temperature at which to run the simulation
7. `friction` - the friction parameter for the thermostat

It then returns five lists:

1. `times` - the times at which data has been collected
2. `p_energy` - the potential energy as a function of time.
3. `k_energy` - the kinetic energy as a function of time
4. `t_energy` - the total energy of the system as a function of time
5. `conserved_quantity` - the value of the conserved quantity as a function of time.

Notice that to get this function for generating the trajectory to work correctly, you are going to need to fill in the blanks in the code within it using what you have learned about constant temperature molecular dynamics.  Furthermore, also notice that encapsulating this code for generating trajectories in a function like the one we have written here is useful.  For the project, you will need to run MD simulations at multiple different temperatures so you will need to use the MD code multiple times.

You will notice that there is a call to `gen_traj` after the definition of this function and that arrays called `tt`, `potential_e`, `kinetic_e`, `total` and `conserved` are used to hold the values that the energy took during the trajectory that was generated.  You need to use the data in these arrays to compute block averages and errors with blocks of trajectory that are 200 steps, 400 steps, 600 steps, 800 steps, 1000 steps and 1200 steps long.  The errors should be indicate of the 90% confidence limit.  

You will only need to compute these block averages for the data in one of these lists.  Remember I would like the ensemble average for the __total energy__.  The value of the average of the block averages should be stored in the list called `averages` and the error bar for a 90 % confidence limit should be stored in the list called `errors`.  Look back at the notes you made on block averaging if you are struggling with this part of the exercise.

The final result should be a graph showing how the error bar changes as the size of the blocks from which it is computed changes.

 


