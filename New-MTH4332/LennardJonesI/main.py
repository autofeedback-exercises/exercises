# Exercise 1
atoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
atoms.set_masses( np.ones(len(atoms)) )
MaxwellBoltzmannDistribution( atoms, 2.0 )

# Exercise 2
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
# And run 1000 steps of Langevin dynamics on the particles. We are running Langevin dynamics
# with k_B T = 2, a timestep of 0.005 and a thermostat friction of 1.0 here.
dyn = Langevin( atoms, 0.005, 2.0, 1.0 )
dyn.run(1000)

# Exercise 3
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

# Exercise 4
maxd, nbins, nf, N, V = 3, 150, 0, 0, 0
delx, histo = maxd / nbins, np.zeros(nbins)
for atoms in Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesI/trajectory.traj') :
    nf, N, V = nf + 1, len(atoms), atoms.get_volume()
    distances = atoms.get_all_distances( mic=True )
    for i in range(1,distances.shape[0]) :
        for j in range(0,i) :
            if  distances[i,j]>maxd : continue
            xbin = int( np.floor( distances[i,j] / delx ) )
            histo[xbin] = histo[xbin] + 2
xbins = np.zeros(nbins)
for i in range(nbins) :
    if i==0 :
        xbins[i] = 0.5*delx
        vol = (4/3)*np.pi*delx**3*(N/V)
        histo[i] = histo[i] / ( vol*nf*N )
    else :
        xbins[i] = (i+0.5)*delx
        vol = (4/3)*np.pi*((delx*(i))**3 - (delx*(i-1))**3)*(N/V)
        histo[i] = histo[i] / ( vol*nf*N )
plt.plot( xbins, histo, 'k-' )
plt.xlabel("r / sigma")
plt.ylabel("g(r)")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 5
mytraj = Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesI/trajectory.traj')
maxd, nbins, nf, N, V = 3, 150, 0, 0, 0
delx, histo = maxd / nbins, np.zeros([5,nbins])
bsize = int( np.floor( len(mytraj) ) / 5 )
for atoms in mytraj :
    bnum = int( np.floor( nf / bsize ) )
    nf, N, V = nf + 1, len(atoms), atoms.get_volume()
    distances = atoms.get_all_distances( mic=True )
    for i in range(1,distances.shape[0]) :
        for j in range(0,i) :
            if  distances[i,j]>maxd : continue
            xbin = int( np.floor( distances[i,j] / delx ) )
            histo[bnum,xbin] = histo[bnum,xbin] + 2
xbins = np.zeros(nbins)
for i in range(nbins) :
    if i==0 :
        xbins[i] = 0.5*delx
        vol = (4/3)*np.pi*delx**3*(N/V)
        histo[:,i] = histo[:,i] / ( vol*bsize*N )
    else :
        xbins[i] = (i+0.5)*delx
        vol = (4/3)*np.pi*((delx*(i))**3 - (delx*(i-1))**3)*(N/V)
        histo[:,i] = histo[:,i] / ( vol*bsize*N )
average, average2 = np.zeros(nbins), np.zeros(nbins)
for i in range(5) :
    average = average + histo[i,:]
    average2 = average2 + histo[i,:]*histo[i,:]
average = average / 5
error = np.sqrt( (1/4)*( average2 / 5 - average*average ) )*scipy.stats.norm.ppf(0.95)
plt.fill_between( xbins, average - error, average + error )
plt.xlabel("r / sigma")
plt.ylabel("g(r)")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 6
def fcc_cubic( atoms ) :
    N = len(atoms)
    order_p = np.zeros(N)
    distances = atoms.get_all_distances( mic=True )
    vecs = atoms.get_all_distances( mic=True, vector=True )
    # Your code goes here
    for i in range(distances.shape[0]) :
        fcc_numer, fcc_denom = 0, 0
        for j in range(distances.shape[1]) :
            if i==j or distances[i,j]>1.5 : continue
            fcc_denom += 1
            x, y, z, r = vecs[i,j,0], vecs[i,j,1], vecs[i,j,2], distances[i,j]
            fcc_numer += ( ( (x*y)**4 + (x*z)**4 + (y*z)**4 ) / (r**8) - ( 27*(x*y*z)**4 ) / r**12 )

        order_p[i] = 80080/(2717+16*27)*(fcc_numer/fcc_denom) + 16*(27-143)/(2717+16*27)
    return order_p

# Exercise 7
minx, maxx, nbins = -.5, 1.1, 70
nf, delx = 0, 1.6 / 70
histo = np.zeros([5,nbins])
bsize = int( np.floor( len( Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesI/trajectory.traj') ) / 5 ) )
for atoms in Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesI/trajectory.traj') :
    bnum = int( np.floor( nf / bsize ) )
    nf = nf + 1
    distances = atoms.get_all_distances( mic=True )
    vecs = atoms.get_all_distances( mic=True, vector=True )
    for i in range(distances.shape[0]) :
        fcc_numer, fcc_denom = 0, 0
        for j in range(distances.shape[1]) :
            if i==j or distances[i,j]>1.5 : continue
            fcc_denom += 1
            x, y, z, r = vecs[i,j,0], vecs[i,j,1], vecs[i,j,2], distances[i,j]
            fcc_numer += ( ( (x*y)**4 + (x*z)**4 + (y*z)**4 ) / (r**8) - ( 27*(x*y*z)**4 ) / r**12 )

    final = 80080/(2717+16*27)*(fcc_numer/fcc_denom) + 16*(27-143)/(2717+16*27)
    xbin = int( np.floor( (final + 0.5) / delx ) )
    if xbin<0 : raise ValueError('xbin should not be negative')
    histo[bnum,xbin] = histo[bnum,xbin] + 1
histo = histo / bsize
average, average2 = np.zeros(nbins), np.zeros(nbins)
for i in range(5) :
    average = average + histo[i,:]
    average2 = average2 + histo[i,:]*histo[i,:]
gat_average = average / 5
gat_error = np.sqrt( (1/4)*( average2 / 5 - gat_average*gat_average ) )*scipy.stats.norm.ppf(0.95)
xbins = np.zeros( nbins )
fes, error = -2.0*np.log( gat_average ), gat_error
for i in range(len(gat_average)) :
    xbins[i] = (i+1)*delx
    if gat_average[i]!=0 : error[i] = 2*gat_error[i] / gat_average[i]

plt.fill_between( xbins, fes - error , fes + error )
plt.xlabel("order parameter")
plt.ylabel("free energy")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()
