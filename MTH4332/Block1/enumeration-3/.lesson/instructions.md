# Generating all the microstates 

Now that we know how to convert a number into its base M representation we have all that we need to enumerate all the microstates for a system of N particles that can each be in one of M distinct states.  Such a system can be in one of M^N distinct microstates.  Each of these microstates can be represented using a single integer that is greater than or equal to 0 and less than M^N.  You generate the microstate for the number X by converting X to its base M representation.  The N digits of this base M representation of the number then represent the states of the N particles.

If you want to generate all the microstates you thus:

1. Write a loop that runs from 0 up to M^N like this:

```python
for i in range(M**N) : 
```

2. You then generate the binary representation for each i value in the loop.

With all that in mind to complete this task you must complete the function `microstate_energies`.  This function takes a single argument `N`, which should be equal to the number of particles in the system.  Within the function you should generate all the microstates for a system with N particles that can be each be in 2 states with energies of -1 and +1.  The energies of all these microstates should be computed and stored in a numpy array with 2^N elements, which the function will return.  In other words, you will need to write a loop something like this in the function:

```python
for i in range(2**N):
   # Generate coordinates of particles for ith microstate
   coords = genstate( i )
   # Evaluate the energy of the microstate
   energies[i] = hamiltonian( coords )
```

You may choose to generate the coordinates of the particles in a separate function called `coords` and to evaluate the energy using a separate `hamiltonian` function as I have done here.  However, if I were coding this I would likely only write the single function `microstate_energies` as the `genstate` and `hamiltonian` functions would be very short.
