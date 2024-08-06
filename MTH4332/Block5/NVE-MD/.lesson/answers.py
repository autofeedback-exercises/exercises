from pairwise_calc import *

def fff(r):
   # Insert your code to calculate the Lennard Jones energy and forces here
   r2 = r*r 
   r6 = r2*r2*r2 
   r12 = r6*r6 
   e = 4*( ( 1/r12 ) - (1/r6) )
   f = -24*( 2/r12 - 1/r6 ) / r2
   return e, f  # First argument should be energy and second should be force

tstep = 0.00001

# Insert code from last exercise to create an atoms object and set masses and velocities here.
atoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
atoms.set_masses( np.ones(len(atoms)) )
MaxwellBoltzmannDistribution( atoms, 2.0 )

# Attach the method that should be used to calculate energies and forces to the atoms object
atoms.calc = pairwise_calculator( rc=4, pairwise_e=fff )

# Calculate the initial energy
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# And run 1000 steps of Langevin dynamics on the particles. We are running Langevin dynamics
# with k_B T = 2, a timestep of 0.005 and a thermostat friction of 1.0 here.
dyn = VelocityVerlet( atoms, tstep )

stats = []
def printenergy(a=atoms):
    """Function to print the potential, kinetic and total energy"""
    epot = a.get_potential_energy()
    ekin = a.get_kinetic_energy()
    stats.append( epot + ekin )

dyn.attach( printenergy, interval=1 )
dyn.run(100)

xvals = np.zeros(101)
for i in range(101) : xvals[i] = i*tstep

print( initial_energy, stats )
plt.plot( xvals, stats, 'ko' )
plt.xlabel("time / arbitrary units")
plt.ylabel("total energy / arbitrary units")
plt.savefig("constant_energy.png")
