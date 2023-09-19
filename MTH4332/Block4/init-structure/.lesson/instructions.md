# Setting the initial configuration using Atomistic Simulation Environment

In the assignments you have completed thus far you have written all the python code for doing your simulations from scratch.
Writing code in this way is not particularly common when you do graduate level research.  The simulations that are typically done
as part of a PhD project are far more complicated than the ones you have performed in this module.  We thus need to reuse code that
has been written by other people as there simply is not time to write all the simulation code from scratch.  You are going to learn to 
use a package for doing molecular dynamics simulations called [atomistic simulation environment (ase)](https://wiki.fysik.dtu.dk/ase/) 
in these exercises.  You are then going to use this package to complete the next assignment.

Your task in this exercise involves using the `FaceCenteredCubic` method from ase to create an object called `atoms`.  This object will 
contain the initial positions of the atoms.  The atomic positions should be sat on an face centered cubic lattice that has the [1,0,0] 
direction of the crystal aligned with the x-axis, the [0,1,0] direction of the crystal aligned with the y-axis and the [0,0,1] direction of the crystal 
aligned with the z-axis.  Each of the atoms in the lattice should have the symbol "Ar" and the minimal unit cell should be repeated 
3 X 3 X 3 times.  The structure should be set up so that there are pbc in all three directions.  The lattice constant should be set equal to 2^(2/3).

You then need to use the [set_masses method](https://wiki.fysik.dtu.dk/ase/ase/atoms.html) from `atoms` to set all the masses of the atoms equal to one.

Lastly, because we are planning to do molecular dynamics, you will need to give each atom an initial velocity.  You can do this using the 
[MaxwellBoltzmannDistribution](https://wiki.fysik.dtu.dk/ase/ase/md.html) method from ASE.  You should use this method to set your atoms to have velocities 
that are consistent with the ones they would be expected to have at a temperature at which (k_B T) = 2.0 (to set the temperature you need to use the depreciated
temp argument to this function). 

In completing this task you will likely find [this page](https://wiki.fysik.dtu.dk/ase/ase/lattice.html) of the ASE manual useful as well as the links above. 
