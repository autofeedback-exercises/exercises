from pairwise_calc import *

def fff(r):
   # Insert your code to calculate the Lennard Jones energy and forces here
   r2 = r*r 
   r6 = r2*r2*r2 
   r12 = r6*r6 
   e = 4*( ( 1/r12 ) - (1/r6) )
   f = -24*( 2/r12 - 1/r6 ) / r2
   return e, f  # First argument should be energy and second should be force

# You need to setup a very small timestep in order to get the energy to be conserved
tstep = 0.00001

# Insert code from last exercises to create an atoms object and set masses and velocities here.
atoms = 

# Attach the method that should be used to calculate energies and forces to the atoms object

# Calculate the initial energy for me here so I can test your code.  Please dont adjust this line
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()


# And use the ideas that were explained in the instructions file to run 100 steps of constant energy MD.
# Add a method to store the total energy on every step so that you can plot a graph of the energy as a function 
# of time.
