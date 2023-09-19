from pairwise_calc import *

def fff(r):
   # Insert your code to calculate the Lennard Jones energy and forces here

   return e, f  # First argument should be energy and second should be force

# Insert code from last exercise to create an atoms object and set masses and velocities here.



# Attach the method that should be used to calculate energies and forces to the atoms object
atoms.calc = pairwise_calculator( rc=4, pairwise_e=fff )

# And run 1000 steps of Langevin dynamics on the particles.  Use the information in the instructions
# to attach a funtion to the dynamics that keeps track of the values the potential energy took 
# during the simulation.  The values the energy took should be stored in a list called energies.
# You should also output the trajectory to a file called mytraj.traj.  The frequency with which 
# you output the trajectory frames should be the same as the one with which you output energies.
 
