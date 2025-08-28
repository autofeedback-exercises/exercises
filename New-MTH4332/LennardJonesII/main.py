# Execise 1
def fff(r):
   # Insert your code to calculate the Lennard Jones energy and forces here
   r2 = r*r
   r6 = r2*r2*r2
   r12 = r6*r6
   e = 4*( ( 1/r12 ) - (1/r6) )
   f = -24*( 2/r12 - 1/r6 ) / r2
   return e, f  # First argument should be energy and second should be force

# Exercise 2
# Insert code from last exercise to create an atoms object and set masses and velocities here.
atoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
# Attach the method that should be used to calculate energies and forces to the atoms object
atoms.calc = pairwise_calculator( rc=4, pairwise_e=fff )
# Run the optimisation
opt = BFGS(atoms)
opt.run(fmax=0.001)
# And get the vibrations
vib = Vibrations(atoms)
vib.run()
data = vib.get_vibrations()
hessian = data.get_hessian_2d()
eigvals, eigvecs = np.linalg.eig( hessian )
# And get the density of states
frequencies = np.sqrt( eigvals )
minfreq = min(frequencies)
maxfreq = max(frequencies)
nbins = 100
delx = 1.01*(maxfreq- minfreq) / nbins
minx = minfreq - (maxfreq-minfreq)*0.005
histo = np.zeros(nbins)
for e in frequencies :
    ibin = int( np.floor( (e-minx) / delx) )
    histo[ibin] = histo[ibin] + 1
xvals = np.zeros(nbins)
for i in range(nbins) : xvals[i] = minx + (i+0.5)*delx
plt.plot( xvals, histo, 'k-')
plt.xlabel("frequencies / arbitrary units")
plt.ylabel("Number of states")
plt.show() 
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 3
frequency = 1.0
T = np.linspace( 0.1, 10, 200 )
b = np.exp(-frequency/T)
nb = 1-b
CV = (frequency*frequency)/(T*T)*( b /nb + b*b/(nb*nb) )
plt.plot( T, CV, 'k-')
plt.xlabel("Temperature / natural units")
plt.ylabel("Heat capacity / natural units")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 4
frequencies = np.array([1,1,2,2,2,3,4,5,9])
T = np.linspace( 0.1, 30, 200 )
CV = np.zeros(200)
for i, temp in enumerate(T) :
    b = np.exp(-frequencies/temp)
    nb = 1-b
    CVall = (frequencies*frequencies)/(temp*temp)*( b /nb + b*b/(nb*nb) )
    CV[i] = sum(CVall)/3
plt.plot( T, CV, 'k-')
plt.xlabel("Temperature / natural units")
plt.ylabel("Heat capacity per atom / natural units")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 5
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
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 6
ncorr = 50
acf, norm = np.zeros(ncorr), np.zeros(ncorr)
n = 0
for atoms in ftraj :
    vel = atoms.get_velocities().flatten()
    maxn = min( len(ftraj), n + ncorr ) - n
    for i in range(maxn) :
        veln = ftraj[n + i].get_velocities().flatten()
        acf[i] = acf[i] + np.dot( veln.T, vel ) / (3*len( atoms ))
        norm[i] = norm[i] + 1
    n = n + 1
acf = acf / norm
times = 0.005*np.linspace(0, ncorr-1, ncorr)
plt.plot( times, acf, 'k-' )
plt.xlabel("time / arbitrary units")
plt.ylabel("velocity autoccoreation function")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 7
natoms = len(ftraj[0].get_velocities())
vtraj = np.zeros([ 3*natoms, len(ftraj) ])
k = 0
for atoms in ftraj :
    vtraj[:,k] = atoms.get_velocities().flatten()
    k = k + 1
fftraj = np.fft.rfft(vtraj,axis=1)
fdos = np.mean(fftraj*np.conjugate(fftraj),axis=0) / len(ftraj)
freqvals = np.fft.rfftfreq( len(ftraj), d=0.005 )
plt.plot( freqvals, fdos, 'k-' )
plt.xlabel("frequency / arbitrary units")
plt.ylabel("vibrational density of states")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()
