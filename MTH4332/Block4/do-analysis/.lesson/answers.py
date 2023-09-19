from pairwise_calc import *

def fff(r):
   # Insert your code to calculate the Lennard Jones energy and forces here
   r2 = r*r
   r6 = r2*r2*r2 
   r12 = r6*r6
   e = 4*( ( 1/r12 ) - (1/r6) )
   f = -24*( 2/r12 - 1/r6 ) / r2
   return e, f  # First argument should be energy and second should be force

# Insert code from last exercise to create an atoms object and set masses and velocities here.
atoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
atoms.set_masses( np.ones(len(atoms)) )
MaxwellBoltzmannDistribution( atoms, 2.0 )


# Attach the method that should be used to calculate energies and forces to the atoms object
atoms.calc = pairwise_calculator( rc=4, pairwise_e=fff )

# And run 1000 steps of Langevin dynamics on the particles.  Use the information in the instructions
# to attach a funtion to the dynamics that keeps track of the values the potential energy took 
# during the simulation.  The values the energy took should be stored in a list called energies.
# You should also output the trajectory to a file called mytraj.traj.  The frequency with which 
# you output the trajectory frames should be the same as the one with which you output energies.
energies = [] 

def printenergy(stats = energies, a=atoms ):
    stats.append( a.get_potential_energy() ) 

traj = Trajectory('mytraj.traj', 'w', atoms)

dyn = Langevin( atoms, 0.005, 2.0, 1.0 )
dyn.attach( traj.write, interval=10 )
dyn.attach( printenergy, interval=10 )
dyn.run(1000)
traj.close()
