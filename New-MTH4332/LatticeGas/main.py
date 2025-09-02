# Exercise 1
nspins = 10 
allup = np.ones(nspins)
alldown = -1*np.ones(nspins)
alternating = np.ones(nspins)
for i in range(nspins) :
    if i%2==0 : alternating[i]=-1

# Exercise 2
def rising_states( nspins, nstates ) :
    spins = np.zeros( nspins )
    for i in range(nspins) :
        spins[i] = i%nstates
    return spins
def lowering_states( nspins, nstates ) :
    spins = np.zeros( nspins )
    for i in range(nspins) :
        spins[i] = nstates - 1 - i%nstates
    return spins
def updown_states( nspins, nstates ) :
    spins = np.zeros( nspins )
    for i in range(nspins) :
        base = np.floor( i / nstates )
        if base%2==0 : spins[i] = i%nstates
        else : spins[i] = nstates - 1 - i%nstates
    return spins

# Exercise 3
def hamiltonian( spins, H ) :
  # Your code goes here
  return -H*sum(spins)
allup, alldown = np.ones(10), -1*np.ones(10)
print( "ENERGY FOR ALL SPIN UP", hamiltonian( allup, 1 ) )
print( "ENERGY FOR ALL SPIN DOWN", hamiltonian( alldown, 1 ) )

# Exercise 4
def hamiltonian2( coords ) :
  energy = 0
  # Your code goes here
  for c in coords :
      if c==1 : energy = energy + 2
      elif c==2 : energy = energy + 3
  return energy
allzero, allone, alltwo = np.zeros(10), np.ones(10), 2*np.ones(10)
print( "ENERGY FOR ALL ZERO", hamiltonian2( allzero ) )
print( "ENERGY FOR ALL ONE", hamiltonian2( allone ) )
print( "ENERGY FOR ALL TWO", hamiltonian2( alltwo ) )

# Exercise 5
def hamiltonian3( coords ) :
  energy = 0
  # Your code goes here
  for c in coords :
      if c==1 or c==2 : energy = energy + 1
      elif c==3 : energy = energy + 2
  return energy
allzero, allone, alltwo, allthree = np.zeros(10), np.ones(10), 2*np.ones(10), 3*np.ones(10)
print( "ENERGY FOR ALL ZERO", hamiltonian3( allzero ) )
print( "ENERGY FOR ALL ONE", hamiltonian3( allone ) )
print( "ENERGY FOR ALL TWO", hamiltonian3( alltwo ) )
print( "ENERGY FOR ALL THREE", hamiltonian3( allthree ) )

# Exercise 6
def getBinary( N ) : 
  # Your code goes here
  bina = np.zeros(6)
  for i in range(6) :
     pp = 2**(5-i)
     bina[i] = np.floor( N / pp )
     N = N - bina[i]*pp
  return bina
for i in range(16) :
  print("The binary representation of", i, "is", getBinary(i) )

# Exercise 7
def convertToBase( N, base ) :
  # Your code goes here
  state, v = np.zeros(7), N
  for i in range(7) :
      vv = base**(6-i)
      state[i] = np.floor( v / vv )
      v = v - state[i]*vv
  return state
# This will print some output that will allow you to test your function
for b in range(2,10) :
  for n in range(10) :
    print("The number", n, "in base", b, "is", convertToBase(n,b) )

# Exercise 8
def microstate_energies( N ) : 
   # Create an array to hold the energies of all the microstates
   energies = np.zeros( 2**N )
   for i in range(2**N) :
       # Generate coordinates of particles for ith microstate
       val, coords = i, np.zeros(N)
       for j in range(N) :
           ppp = 2**(N-1-j)
           coords[j] = np.floor( val / ppp )
           val = val - ppp*coords[j]
           if coords[j]==0 : coords[j] = -1
       # Evaluate the energy of the microstate and store it in the array that we will return
       energies[i] = hamiltonian( coords, -1 )
   # Return the array that holds the energies of the microstates
   return energies

# Exercise 9
def partitionfunction( N, H, T ) :
  Z = 0
  # Your code to calculate the partition function goes here
  for k in range(2**N) :
      val, spins = k, np.zeros(N)
      for i in range(N) :
          ppp = 2**(N-1-i)
          spins[i] = np.floor( val / ppp )
          val = val - spins[i]*ppp
          if spins[i]==0 : spins[i] = -1
      Z = Z + np.exp( -hamiltonian( spins, H ) / T )
  return Z
# Calculate the partition function for a system of 5 spins 
# with no external field at a temperature of 0.1
print( partitionfunction(5,0,0.1) )
# Calculate the paritition function for a system of 6 spins 
# with a magnetic field strength of 1 at a temperature of 0.5
print( partitionfunction(6,1,0.5) )

# Exercise 10
def hamiltonian( spins, H ) :
  eng = -H*sum(spins)
  return eng
# Generate an index for each microstate
indices = np.zeros(2**8)
for i in range(2**8) : indices[i] = i
energies = np.zeros(2**8)
for index in indices :
  spins, ind = np.zeros(8), index
  # Your code to convert the integer index to the corresponding spin coordinates goes here
  for j in range(8) :
      ppp = 2**(7-j)
      spins[j] = np.floor( ind / ppp )
      ind = ind - spins[j]*ppp
      if spins[j]==0 : spins[j] = -1
  energies[int(index)] = hamiltonian( spins, 1 )
# This will plot the energies of the configurations against their numerical indexes. 
plt.plot( indices, energies, 'ko')
plt.xlabel("numerical index")
plt.ylabel("energy")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 11
def hamiltonian( spins, H ) :
  eng = -H*sum(spins)
  return eng
# Create a list of the posssible values the energy can take
energies = np.zeros(9)
for i in range(9) : energies[i] = -8+i*2
# Create a list that will hold the number of microstates with each energy 
number_of_microstates = np.zeros(9)
# Your code to do the loop over all the microstates and to count how many times each 
# of the energy values appear goes here
for i in range(2**8) :
    vv, spins = i, np.zeros(8)
    for j in range(8) :
        ppp = 2**(7-j)
        spins[j] = np.floor( vv / ppp )
        vv = vv - spins[j]*ppp
        if spins[j]==0 : spins[j] = -1
    eng = hamiltonian( spins, 1 )
    number_of_microstates[ int((eng + 8)/2) ] = number_of_microstates[ int((eng + 8)/2) ] + 1

# This will plot the possible values for the energy against the number of microstates with 
# that particular energy.
plt.bar( energies, number_of_microstates, width=0.1 )
plt.xlabel("energy")
plt.ylabel("Number of microstates")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 12
def hamiltonian( spins, H ) :
  eng = -H*sum(spins)
  return eng
# Create a list of the posssible values the energy can take
energies = np.zeros(9)
for i in range(9) : energies[i] = -8+i*2
# Create a list that will hold the number of microstates with each energy 
number_of_microstates = np.zeros(9)
# Your code to do the loop over all the microstates and to count how many times each 
# of the energy values appear goes here
for i in range(2**8) :
    vv, spins = i, np.zeros(8)
    for j in range(8) :
        ppp = 2**(7-j)
        spins[j] = np.floor( vv / ppp )
        vv = vv - spins[j]*ppp
        if spins[j]==0 : spins[j] = -1
    eng = hamiltonian( spins, 1 )
    number_of_microstates[ int((eng + 8)/2) ] = number_of_microstates[ int((eng + 8)/2) ] + 1

entropy = np.log( number_of_microstates )
# This will plot the possible values for the energy against the number of microstates with 
# that particular energy.
plt.bar( energies, entropy, width=0.1 )
plt.xlabel("energy")
plt.ylabel("Entropy")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 13
def hamiltonian( spins, H ) : 
  energy = -H*sum(spins)
  return energy
def ensemble_average( N, H, T ) :
  numerator, Z = 0, 0
  # Your code to calculate the ensemble average goes here
  for i in range(2**N) :
      v, spins = i, np.zeros(N)
      for j in range(N) :
          ppp = 2**(N-1-j)
          spins[j] = np.floor( v / ppp )
          v = v - ppp*spins[j]
          if spins[j]==0 : spins[j] = -1
      e = hamiltonian( spins, H )
      bwe = np.exp( -e/T )
      numerator = numerator + e*bwe
      Z = Z + bwe
  return numerator / Z
# Calculate the ensemble average of the energy for a system of 5 spins 
# with an external field of 1 at a temperature of 0.1
print( ensemble_average(5,0,1.1) )
# Calculate the ensemble average for a system of 6 spins 
# with a magnetic field strength of 1 at a temperature of 0.5
print( ensemble_average(6,1,0.5) )

# Exercise 14
def hamiltonian( spins, H ) :
  energy = -H*sum(spins)
  return energy
def ensemble_average( N, H, T ) :
  numerator, Z = 0, 0
  # Your code to calculate the partition function goes here
  for i in range(2**N) :
      v, spins = i, np.zeros(N)
      for j in range(N) :
          ppp = 2**(N-1-j)
          spins[j] = np.floor( v / ppp )
          v = v - ppp*spins[j]
          if spins[j]==0 : spins[j] = -1
      e = hamiltonian( spins, H )
      bwe = np.exp( -e/T )
      numerator = numerator + e*bwe
      Z = Z + bwe
  return numerator / Z
energies, k = np.zeros(15), 0
temperatures = np.linspace(0.1,3.1,15)
for temp in temperatures :
    energies[k] = ensemble_average(8, 1., temp)
    k = k + 1
plt.plot( temperatures, energies, 'k-' )
plt.xlabel("temperature / arbitrary units")
plt.ylabel("average energy / arbitrary units")
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

# Exercise 15
# Define symbols that we will use to represent:
# N = number of particles
# B = 1/T where T is temperature
N, B = sy.symbols("N B")
# One particle partition function
Z1 = 1 + sy.exp(-B) + sy.exp(-3*B )
# N particle partition function
ZN = Z1**N
# Now ensemble average of the energy 
# sy.diff calculates the derivative with respect to B
E = -sy.diff( sy.log(ZN), B )
print("The ensemble average for the energy can be calculated using", E )
# Lets now draw a graph of this result using matplotlib and NumPy
# We are setting H=1 and N=8 here
temperatures = np.linspace(0.1,3,100)
energies = -8*( -np.exp(-1/temperatures ) - 3*np.exp(-3/temperatures) )/ (1  + np.exp(-1/temperatures) + np.exp(-3/temperatures) )
plt.plot( temperatures, energies, 'k-' )
plt.xlabel('temperature')
plt.ylabel('average energy')
plt.show()
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()
