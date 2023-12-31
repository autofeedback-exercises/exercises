# Implementing thermostated MD

Now that we know how an MD code is written and what the distribution of velocities for a system at a particular temperature is we should be in a position to implement a constant temperature MD algorithm.  As was already discussed in the previous sections a wide variety of different techniques can be used to couple the velocities of the atoms in the system with a heat bath.  In this exercise, we are going to learn about the so-called Langevin thermostat.  This thermostat works adjusting the velocities before and after the first step of the velocity Verlet algorithm using the following expression:

![](eq1.png)

Here \delta is half the simulation timestep, \gamma is a parameter known as the friction of the thermostat and N(0,1) is used to indicate a sample from a standard normal random variable.  

The details as to how this expression is derived are beyond the scope of this module.  We can begin to understand how it works by looking at its structure.  The e^{-\gamma\delta} in the first term, for instance, is less than one.  By multiplying the old velocity by this expression repeatedly we thus cause the old velocity to decay away to zero.  Ignoring the factor of (1-e^{-2\gamma\delta}) in the second term gives us the expression that we used to set the initial velocities of the atoms.  Consequently, if we use a very large time step, it is as if we are simply setting the velocities as we did in the first exercise. Notice last of all that the coefficients of the terms in the sum above are constant.  You can thus calculate these coefficients outside the main MD loop to improve computational efficiency 

Finally, notice that by setting the coefficients of the second term equal to \sqrt{1-e^{-2\gamma\delta}} we ensure that the sum of the squares of the coefficients of v_{old} in the first part and the value we would set for the initial velocity in the second part is one.  In other words, in setting the coefficients we are using Pythagoras theorem in some way.

Lets now turn to what you need to do in order to complete the code.  As in the previous exercise, I have written a skeleton code for the MD algorithm that you need to fill in.  To complete this you need to:

1. Write a function called `potential` that computes the potential energy and the forces for each of the configurations you generate.
2. Write a function called `kinetic` that calculates the instantaneous kinetic energy.
3. Every 10 MD steps store the instantaneous values of the potential, kinetic and total energies in the lists called `p_energy`, `k_energy` and `t_energy`

In addition, you then need to complete the skeleton code that implements the dynamics.  In each loop this code should:

1. Use the equation given above to modify the velocities.  When using the above equation in this step \delta should be set equal to half the simulation timestep.  This step is the first step in controlling the simulation temperature.

2. Update the velocities, v, by a half timestep using:

![](eq2.png)

3. Update the positions, x, by a full timestep using:

![](eq3.png)

4. Recalculate the forces F(t+\delta) at the new position.

5. Use the new values of the forces to update the velocities by another half timestep using:

![](eq4.png)

6. Use the equation given above to modify the velocities one more.  As in the first step \delta should be set equal to half the simulation timestep as you do this.

Notice that the algorithm I have just described is very similar to the velocity Verlet algorithm that you implemented in the previous exercise.  In this new algorithm, the steps of the velocity Verlet algorithm are just sandwiched between the initial and final steps that control the simulation temperature. 

In the outline code, you will notice that I have created three variables to hold the positions (`pos`), velocities (`vel`) and forces (`forces`).  Notice that whenever you update the velocities, positions or forces in the velocity Verlet algorithm you never again need the old positions velocities or forces.  You thus can (and should) use these three matrices to hold the instantaneous positions, velocities and forces.  I have written some code that will keep track of the velocities the particle takes during the trajectory and that can be used to visualise what happens to the velocity as the calculation proceeds.

The final result from the calculation should be a graph showing how the velocity of the particle changes with time during the simulation.  If the code has been implemented correctly you should see that the value of the velocity fluctuates around 0.  The variance of the distribution of velocities the particle takes during the simulation should be equal to the temperature. 
