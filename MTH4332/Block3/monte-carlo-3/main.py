import matplotlib.pyplot as plt
import numpy as np

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

    # Do the main Monte Carlo loop
    neweng, energies = 0, np.zeros( int( np.floor(N / stride) ) )
    for i in range(equil + N) : 
        # Generate the trial move
        move = np.floor( (L*L+1)*np.random.uniform(0,1) )
        if move==L*L : 
           # Your code to calculate the energy when all the spins are flipped goes here
           neweng = eng
        else :
           # This is going to be flipping a single spin
           j, k = int( np.floor( move / L ) ), move%L
           # Your code to calculate the energy when a single spin flips goes here
           neweng = eng

        # Now decide whether or not to accept the move
        # YOU NEED TO determine the two arguments to the min function in the if
        # statement in the line below.
        if np.random.uniform(0,1)<min( , ) :
           # Set the energy to its new value
           eng = neweng
           # Update the spins array
           if move==L*L : 
               # YOU NEED TO ADD CODE HERE
           else : 
               # YOU NEED TO ADD CODE HERE
       

        step = i-equil
        if step>=0 and step%stride==0 : 
           energies[int(step/stride)] = eng

    return energies


# This is the part of the code that allows you to visualise the series of 
# energies your Monte Carlo function generates.  You do not need to modify
# anything from here onwards.  You can modify this code though.
energies = monte_carlo( 1000, 0, 10, 20, 0, 1.0, 319 )
plt.plot( energies, 'ko' )
plt.xlabel("index")
plt.ylabel("energy")
plt.savefig("energies.png")
