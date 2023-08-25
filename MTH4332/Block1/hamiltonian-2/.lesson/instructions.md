# Hamiltonian for a three level system

Lets now introduce a Hamiltonian for a three level system.  Each particle in our system will be in one of three states, which we will call state 0, state 1 and state 2.  We can thus specify the microstate for a system of N particles by using a NumPy array in which each element is either 0, 1 or 2.  If a particle is in state 0 it has an energy of 0, if a particle is in state 1 it has an energy of 2 and if it is in state 2 it will have an energy of 3.  The total energy for our N particle system will be the sum of the energies of all the particles.

Modify the code in in main.py so that the function called `hamiltonian` calculates the the energy for a system of N of these (non-interacting) particles.  Notice that this function takes a NumPy array called `coords`, which contains all the particle coordinates, as input.  The number of particles in your system is equal to the number of elements in this list.
