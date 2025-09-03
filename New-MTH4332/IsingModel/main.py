# Exercise 1
def getstate(N) : 
    # Your code for generating the random microstate goes here
    spins = np.ones([N,N])
    for i in range(N) :
        for j in range(N) :
            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1
    return spins
# You don't need to adjust this code.  It is just here
# so you can look at what your function is generating.
# This will generate a state for a 4x4 lattice of spins
print( "Random 4x4 state", getstate(4) )
# This will generate a state for a 5x4 lattice of spins
print( "Random 4x4 state", getstate(5) )

# Exercise 2
def flipSpin( spins, i, j ) : 
    # Your code to flip the spin in the (i,j) position of the lattice goes here
    spins[i,j] = -1*spins[i,j]
    return spins
def flipAllSpins( spins ) :
    # Your code to flip all the spins goes here
    spins = -1*spins
    return spins
def chooseMove( spins ) :
    # Your code to choose whether to flip all or one of the spins goes here
    if np.random.uniform(0,1) < 1/(1+spins.shape[0]*spins.shape[1]) : return 1
    return 0
def chooseSpin( spins ) :
    # Your code to choose a particular spin to flip goes here
    ispin = np.floor( spins.shape[0]*np.random.uniform(0,1) )
    jspin = np.floor( spins.shape[0]*np.random.uniform(0,1) )
    return ispin, jspin

# Exercise 3
def magnetisation( spins ) :
    # Your code for calculating the magnetistation goes here
    return sum( sum(spins) ) / ( spins.shape[0]*spins.shape[1] )
# The rest of this code is just to check if you code is doing something sensible
spins = np.ones([10,10])
print("The magneitation of the all up state is", magnetisation( spins ) )
spins = -1*spins
print("The magneitation of the all down state is", magnetisation( spins ) )

# Exercise 4
def hamiltonian( spins, H ) :
    # Your code for calculating the hamiltonian described in the instruction goes here
    return -H*sum( sum( spins ) )
# The rest of this code is just to check if you code is doing something sensible
spins = np.ones([10,10])
print("The energy of the all up state is", hamiltonian( spins, -1 ) )
print("The energy of the all up state is", hamiltonian( spins, +1 ) )
spins = -1*spins
print("The energy of the all down state is", hamiltonian( spins, -1 ) )
print("The energy of the all down state is", hamiltonian( spins, +1 ) )

# Exercise 5
def hamiltonian( spins ) :
    # Your code for calculating the hamiltonian described in the instruction goes here
    Ene = 0
    for i in range(spins.shape[0]) :
        for j in range(spins.shape[1]) :
            Ene = Ene + spins[i,j]*( spins[ (i+1)%spins.shape[0], j] + spins[ i, (j+1)%spins.shape[1]] + spins[(i-1)%spins.shape[0], j] + spins[ i, (j-1)%spins.shape[1]] )
    return - Ene / 2
# The rest of this code is just to check if you code is doing something sensible
spins = np.ones([10,10])
print("The energy of the all up state is", hamiltonian( spins ) )
spins = -1*spins
print("The energy of the all down state is", hamiltonian( spins ) )

# Exercise 6
def hamiltonian( spins, H ) :
    # Your code for calculating the hamiltonian described in the instruction goes here
    Ene = 0
    for i in range(spins.shape[0]) :
        for j in range(spins.shape[1]) :
            Ene = Ene + spins[i,j]*( spins[ (i+1)%spins.shape[0], j] + spins[ i, (j+1)%spins.shape[1]] + spins[(i-1)%spins.shape[0], j] + spins[ i, (j-1)%spins.shape[1]] )
    return - Ene / 2 - H*sum( sum( spins ) )
# The rest of this code is just to check if you code is doing something sensible
spins = np.ones([10,10])
print("The energy of the all up state is", hamiltonian( spins, 0 ) )
spins = -1*spins
print("The energy of the all down state is", hamiltonian( spins, 1 ) )

# Exercise 7
def energy(x) :
    return x*x / 2
# Set the initial position of the particle, the number of frames,
# the maximum value to shift the position by and the temperature
pos, nframes, maxshift, temp = 0.0, 100, 1.0, 1.0
# Calculate the energy at the start of the simulation
oldenergy = energy(pos)
# Set up some NumPy arrays to hold data
xvals, yvals = np.linspace(1,nframes,nframes), np.zeros(nframes)
for i in range(nframes) :
    # Your code to generate random move goes here
    newpos = pos + maxshift*( 2*np.random.uniform(0,1) - 1 )
    newenergy = energy(newpos)
    # Your code for the accept reject criteria should go here
    if np.random.uniform(0,1)<min( 1.0, np.exp( -newenergy/temp ) / np.exp( -oldenergy/temp )  ) :
       oldenergy, pos = newenergy, newpos

    # You need to store the "time series" of energies in yval to pass the test
    yvals[i] = pos

# This generates the graph 
plt.plot( xvals, yvals, 'ko' )
plt.xlabel("index")
plt.ylabel("particle position")
plt.savefig("pos.png")
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 8
def new_energy( spins, E, H, move ) :
    # Your code to calculate the energy of the configuration in spins after 
    # the move indicated using the variable move goes here
    N = spins.shape[1]
    if move==N*N :
       new_e = E + 2*H*sum( sum( spins ) )
    else :
       i, j = int( np.floor( move / N ) ), move%N
       new_e = E + 2*spins[i,j]*( spins[(i+1)%N,j] + spins[(i-1)%N,j] + spins[i,(j-1)%N] + spins[i,(j+1)%N] + H )

    return new_e

# Exercise 9
def monte_carlo( N, equil, stride, L, H, T, seed ) :
    # Set the seed to the value input
    np.random.seed(seed)
    # Generate the initial configuration 
    spins = np.ones([L,L])
    for i in range(L) :
        for j in range(L) :
            if np.random.uniform(0,1)<0.5 : spins[i,j]=-1
    # Calculate the energy of the initial configuration that you generated
    eng = 0
    # YOUR CODE TO CALCULATE THE INITIAL ENERGY OF THE CONFIGURATION GOES HERE
    for i in range(spins.shape[0]) :
        for j in range(spins.shape[1]) :
            eng = eng + spins[i,j]*( spins[ (i+1)%spins.shape[0], j] + spins[ i, (j+1)%spins.shape[1]] + spins[(i-1)%spins.shape[0], j] + spins[ i, (j-1)%spins.shape[1]] )
    eng = - eng / 2 - H*sum( sum( spins ) )
    # Do the main Monte Carlo loop
    neweng, energies = 0, np.zeros( int( np.floor(N / stride) ) )
    for i in range(equil + N) :
        # Generate the trial move
        move = np.floor( (L*L+1)*np.random.uniform(0,1) )
        if move==L*L :
           # Your code to calculate the energy when all the spins are flipped goes here
           neweng = eng + 2*H*sum( sum(spins) )
        else :
           # This is going to be flipping a single spin
           j, k = int( np.floor( move / L ) ), int( move%L )
           # Your code to calculate the energy when a single spin flips goes here
           neweng = eng + 2*spins[j,k]*( spins[(j+1)%L,k] + spins[(j-1)%L,k] + spins[j,(k-1)%L] + spins[j,(k+1)%L] + H )
        # Now decide whether or not to accept the move
        if np.random.uniform(0,1)<min(1.0, np.exp( -neweng/T ) / np.exp( -eng/T ) )  :
           # Set the energy to its new value
           eng = neweng
           # Update the spins array
           if move==L*L :
               # YOU NEED TO ADD CODE HERE
               spins = -1*spins
           else :
               # YOU NEED TO ADD CODE HERE
               j, k = int( np.floor( move / L ) ), int( move%L )
               spins[j,k] = -1*spins[j,k]

        step = i-equil
        if step>=0 and step%stride==0 :
           energies[int(step/stride)] = eng
    return energies
# Lets look at the time series of energies from our Monte Carlo simulation 
energies = monte_carlo( 1000, 0, 10, 20, 0, 1.0, 319 )
plt.plot( energies, 'ko' )
plt.xlabel("index")
plt.ylabel("energy")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 10
def monte_carlo( N, equil, stride, L, H, T, seed ) :
    # Set the seed to the value input
    np.random.seed(seed)
    # Generate the initial configuration 
    spins = np.ones([L,L])
    for i in range(L) :
        for j in range(L) :
            if np.random.uniform(0,1)<0.5 : spins[i,j]=-1
    # Calculate the energy of the initial configuration that you generated
    eng = 0
    # YOUR CODE TO CALCULATE THE INITIAL ENERGY OF THE CONFIGURATION GOES HERE
    for i in range(spins.shape[0]) :
        for j in range(spins.shape[1]) :
            eng = eng + spins[i,j]*( spins[ (i+1)%spins.shape[0], j] + spins[ i, (j+1)%spins.shape[1]] + spins[(i-1)%spins.shape[0], j] + spins[ i, (j-1)%spins.shape[1]] )
    mag = sum( sum( spins ) )
    eng = - eng / 2 - H*mag
    # Do the main Monte Carlo loop
    neweng, M, M2, ns = 0, 0, 0, 0
    for i in range(equil + N) :
        # Generate the trial move
        move = np.floor( (L*L+1)*np.random.uniform(0,1) )
        if move==L*L :
           # Your code to calculate the energy when all the spins are flipped goes here
           neweng = eng + 2*H*mag
        else :
           # This is going to be flipping a single spin
           j, k = int( np.floor( move / L ) ), int( move%L )
           # Your code to calculate the energy when a single spin flips goes here
           neweng = eng + 2*spins[j,k]*( spins[(j+1)%L,k] + spins[(j-1)%L,k] + spins[j,(k-1)%L] + spins[j,(k+1)%L] + H )
        # Now decide whether or not to accept the move
        if np.random.uniform(0,1)<min(1.0, np.exp( -neweng/T ) / np.exp( -eng/T ) )  :
           # Set the energy to its new value
           eng = neweng
           # Update the spins array
           if move==L*L :
               # YOU NEED TO ADD CODE HERE
               mag = -mag
               spins = -1*spins
           else :
               # YOU NEED TO ADD CODE HERE
               j, k = int( np.floor( move / L ) ), int( move%L )
               mag = mag + 2*spins[j,k]
               spins[j,k] = -1*spins[j,k]

        step = i-equil
        if step>=0 and step%stride==0 : M, M2, ns = M + mag, M2 + mag*mag, ns + 1
    M = M / ns
    S = ( ns / (ns-1) )*( M2/ns - M*M )
    return S / ( L*L*T )
# Lets look at the time series of energies from our Monte Carlo simulation 
print("The suceptibility at T=2 and H=0 is", monte_carlo( 10000, 1000, 10, 20, 0, 2, 319 ) )
print("The suceptibility at T=5 and H=0 is", monte_carlo( 10000, 1000, 10, 20, 0, 5, 450 ) )

# Exercise 11
# This is the number of bins
nbins = 50
# This is the minimum and maximum for the grid
minx, maxx = -1.1, 1.1
# Your code to calculate and plot the histogram goes here
delx = (maxx - minx) / nbins
histo = np.zeros(nbins)
for m in mags :
    mav = m / (20*20)
    xbin = int( np.floor( (mav-minx) / delx ) )
    histo[xbin] = histo[xbin] + 1
histo = histo / len(mags)
xvals = np.zeros(nbins)
for i in range(nbins) : xvals[i] = (i+0.5)*delx
plt.plot( xvals, histo, 'k--' )
plt.xlabel("average magnetisation per spin")
plt.ylabel("probability density")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 12
# This is the number of bins
nbins = 50
# This is the minimum and maximum for the grid
minx, maxx = -1.1, 1.1
# Your code to calculate and plot the histogram goes here
delx = (maxx - minx) / nbins
histo = np.zeros(nbins)
for m in mags :
    mav = m / (20*20)
    xbin = int( np.floor( (mav-minx) / delx ) )
    histo[xbin] = histo[xbin] + 1
histo = histo / len(mags)
xvals = np.zeros(nbins)
for i in range(nbins) : xvals[i] = (i+0.5)*delx
plt.plot( xvals, -5.0*np.log(histo), 'k--' )
plt.xlabel("average magnetisation per spin")
plt.ylabel("free energy / natural units")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 13
# This is the number of bins
nbins = 50
# This is the minimum and maximum for the grid
minx, maxx = -1.1, 1.1
# These variables should hold the x coordinates of the graph and the upper and lower 
# confident limits on the estimate of the free energy
xv, lower_yv, upper_yv = np.zeros( nbins ), np.zeros( nbins ), np.zeros( nbins )
# This is the size of the blocks.  You will calculate one estimate of the histogram
# over the blocks of this size
blocksize = 200
# This is the number of blocks that you are splitting the trajectory in
nblocks = int( np.floor( len(mags) / blocksize ) )
delx = ( maxx - minx ) / nbins
final_v, final_v2 = np.zeros(nbins), np.zeros( nbins )
# This loop calculates your nblocks estimates of the histogram
for i in range(nblocks) :
    # Your code for calculating each of the nblocks estimate of the histogram goes here
    histo = np.zeros(nbins)
    for j in range(i*blocksize,(i+1)*blocksize) :
        mav = mags[j] / (20*20)
        xbin = int( np.floor( (mav-minx) / delx ) )
        histo[xbin] = histo[xbin] + 1
    histo = histo / blocksize
    final_v = final_v + histo
    final_v2 = final_v2 + histo*histo
final_v = final_v / nblocks
final_v2 = np.sqrt( (1/(nblocks-1))*( final_v2/nblocks - final_v*final_v ) )*scipy.stats.norm.ppf(0.95)
fes, err = -5.0*np.log( final_v ), final_v2
for i in range(len(final_v)) :
    if final_v[i]!=0 : err[i] = 5*final_v2[i] / final_v[i]
lower_yv = fes - err
upper_yv = fes + err
for i in range(nbins) : xv[i] = (i+0.5)*delx
# This part plots the graph.  You need to define and set the variables lower_yv and upper_yv
# as described in the instructions
plt.fill_between( xv, lower_yv, upper_yv )
plt.xlabel("average magnetisation per spin")
plt.ylabel("free energy / natural units")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 14
# This is the number of bins
nbins = 50
# This is the minimum and maximum for the grid
minx, maxx = -1.1, 1.1
# This is the list of block sizes you should investigate
blocksizes = np.array([10, 20, 25, 100, 200, 250, 500])
# Your code to draw the graph described in the instructions goes here.
# I would recommend writing a function to calculate the histogram with 
# different block sizes
def get_histo_error( data, nbins, minx, maxx, blocksize ) :
    delx = ( maxx - minx ) / nbins
    nblocks = int( len(data) / blocksize )
    final_v, final_v2 = np.zeros(nbins), np.zeros( nbins )
    # This loop calculates your nblocks estimates of the histogram
    for i in range(nblocks) :
        # Your code for calculating each of the nblocks estimate of the histogram goes here
        histo = np.zeros(nbins)
        for j in range(i*blocksize,(i+1)*blocksize) :
            mav = data[j] / (20*20)
            xbin = int( np.floor( (mav-minx) / delx ) )
            histo[xbin] = histo[xbin] + 1
        histo = histo / blocksize
        final_v = final_v + histo
        final_v2 = final_v2 + histo*histo
    final_v = final_v / nblocks
    final_v2 = np.sqrt( (1/(nblocks-1))*( final_v2/nblocks - final_v*final_v ) )*scipy.stats.norm.ppf(0.95)
    errtot, n = 0, 0
    for i in range(len(final_v)) :
        if final_v[i]>0 :
           errtot += 5*final_v2[i] / final_v[i]
           n = n + 1
    return errtot / n
error = np.zeros(len(blocksizes))
for n,b in enumerate(blocksizes) :
    error[n] = get_histo_error( mags, nbins, minx, maxx, b )
plt.plot( blocksizes, error, 'ko' )
plt.xlabel("Length of block")
plt.ylabel("Average error on free energy")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()
~                                                                        
