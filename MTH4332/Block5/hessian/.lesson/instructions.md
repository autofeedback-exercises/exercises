# Calculating the density of states

In assignments previous to this one you learned two ways to calculate the heat capacity as a function of temperature from molecular dynamics simulations.
When you use the methods that have been introduced thus far you assume that the particles the system is composed of are classical and that the effect of
the quantum nature of matter on the heat capacity is tiny.  In this final assignment we are going to examine this approximation that the particles are classical 
in more detail by learning one approach for determining the nuclear quantum effects.

In the approach we will use, we extract properties of the 0 K structure and use these properties to determine the partition function at finite temperature by assuming that the 
system behaves as a system of independent quantum harmonic oscillators.  We can derive an exact expression for the partition function of quantum harmonic osciallator and can thus 
calculate the properties of such systems at all temperatuures.  Furthermore, the only non-thermodynamic variable that enters the expression for the partition 
function of a quantum harmonic oscillator is the oscillators characteristic frequency.  The first thing we will thus need to do is to extract a set of characteristic frequencies from 
the 0K structure.

We can use ASE to find the 0 K structure of a material by running an optimisation.  Such a calculation moves the atoms to the positions where they have the lowest energy, which is the position
they should adopt when the system is at 0 K.  To find the minimum energy positions for the atoms in the atom type object `atoms` we can use the following ASE commands:

```python
opt = BFGS(atoms)
opt.run(fmax=0.001)
```

The initial position of the atoms and the potential that acts between them can be set here by using what we learned about ASE last week.

Once we have found the minimum energy structure we can use ASE to calculate a matrix of second derivatives of the potential (the hessian matrix) by using the following commands:

```python
vib = Vibrations(atoms)
vib.run()
data = vib.get_vibrations()
hessian = data.get_hessian_2d()
```

It is striaghtforward to show that the Hessian matrix has units of one over seconds squared.  The square roots of the eigenvalues of this matrix are thus frequencies.  

We can find these eigenvalues and store them in a NumPy array called `eigvals` by using the following commands:

```python 
eigvals, eigvecs = np.linalg.eig( hessian )
```

If we do this when the energy is minimised we should find that the eigenvalues are all non-negative.  There should thus be no imaginary frequencies.

__Your task in this exercise is to use the information above about ASE to calculate the frequencies for a system of 108 Lennard Jones particles.__  To complete this exercise you will need to use 
the code that you learned last week that generates an initial configuration for the 108 atoms by placing all the atoms on the lattice sites for an FCC crystal.  You will then need to use the
`pairwise_calc` module that I introduced last week to setup ASE so that it can calculate the potential energy for any configuration of Lennard Jones particles. To do this you will need to complete 
the function `fff` so that it returns the energy energy of a pair of atoms that are separated by a distance r_ij and the force that acts on this distance.  

You should use a cutoff of 4 natural units when computing the Lennard Jones potential.  Hint: setting up the calculator was covered in the exercise called calculator-setup last week.

Once you have setup the initial structure and calculator you should be able to use the functions described above for minimising the energy, calculating the hessian and calculating the frequencies that 
are described above.

__The task is not completed once you have calculated the frequencies as I would like you to generate a graph that shows the density of states as a function of the frequencies.__  To construct this graph
you will need to place each of the frequencies that you obtained by diagonalising the Hessian matrix into one of the `nbins` histogram bins with centers at `xvals` that I have created for you in `main.py`.
The final lines of codes that I have written should then generate the plot of the density of states for you.  

