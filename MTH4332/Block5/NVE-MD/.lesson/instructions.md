# Running constant energy molecular dynamics

In the conclusions of the final report you write you will calculate dynamical properties from molecular dynamics simulations.
When we are calculating these properties we need to be careful about controlling temperature using thermostats.  Thermostats
work by perturbing the velocities of the particles in our simulation box and in doing so can change the measured dynamic properties.

One way to avoid this issue is to run a simulation __without__ a thermostat.  In other words, you can run your simulation in the NVE
rather than the NVT simulation.  You will be running these sorts of simulatiosn to complete the exercises so in this exercise, we are 
thus going to learn to run a NVE simulation using ASE.

The procedure that should be followed here is similar to the one that you have follwed in setting up the NVT simulations.  In particular 
you need to:

1. Set up an `Atoms` object by calling the `FaceCenteredCubic` method.  As you have done in previous exercises you should run a 3x3x3 cell with a lattice constant of 2^(2/3).
2. Set the masses of all the atoms in your `Atoms` object equal to one.
3. Use the Maxwell Boltzmann distribution to set the velocities of all the atoms in accordance with a temperature of 2.0 natural units.
4. Setup the atoms object to use the `pairwise_calculator` method to calculate the potential energy.  You should use a cutoff of 4 sigma when determining the interactions.  You will also need to write a function called `fff` to calculate the energy and forces on a pair of atoms as you have done in previous exercises.
5. Next you need to set the variable `initial_energy` equal to the total energy of the N particle system you are studying.
6. Once you have done this you are in a position to run the NVE MD using the following commands:

```python
dyn = VelocityVerlet( atoms, tstep )
dyn.run(100)
```

Before running these commands you will need to use what you learned in previous exercises about the `dyn.attach` method to capture the total energy of the system on each timestep as your final task is to generate a graph that shows the 
total energy as a function of simulation time.  The labels on the axis of this graph should be "time / arbitrary units" and "total energy / arbitrary units".  The test code here checks that the total energy values that you plot in your 
graph are the same as the variable `initial_energy`.  This is a valid test as in NVE MD the total energy of the system should be constant.  In practise (because of cutoffs and the like) energy changes by a small amount in any simulation.  
I thus recommend using a small timestep for your MD simulation.

N.B.

For this exercise I asked you to run a NVE simulation started directly from the input fcc structure.  In practise you would __never__ run a simulation like this.  Before you start running NVE simluations you should run some equilibration 
in the NVT ensemble.  These equilibration steps allow the system to equilibrate and get the energy to a reasonable equilibrium value for the temperature of interest.  In other words, you run the equilibration in the NVT ensemble to ensure that 
the potential energies of the structures that are being visted are reasonable.
