from pairwise_calc import *

def fff(r):
   # Insert your code to calculate the Lennard Jones energy and forces here

   return e, f  # First argument should be energy and second should be force

# Insert code from last exercise to create an atoms object and set masses and velocities here.



# Attach the method that should be used to calculate energies and forces to the atoms object
atoms.calc = pairwise_calculator( rc=4, pairwise_e=fff )

# And run 1000 steps of Langevin dynamics on the particles. We are running Langevin dynamics
# with k_B T = 2, a timestep of 0.005 and a thermostat friction of 1.0 here.
dyn = Langevin( atoms, 0.005, 2.0, 1.0 )
dyn.run(1000)
