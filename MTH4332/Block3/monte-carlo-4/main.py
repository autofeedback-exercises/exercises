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
    # YOUR CODE TO CALCULATE THE INITIAL ENERGY AND THE INITIAL MAGNETISATION OF THE CONFIGURATION GOES HERE

    # Do the main Monte Carlo loop
    neweng, M, M2, ns = 0, 0, 0, 0
    for i in range(equil + N) : 
        # Generate the trial move
        move = np.floor( (L*L+1)*np.random.uniform(0,1) )
        if move==L*L : 
           # Your code to calculate the energy when all the spins are flipped goes here
           neweng = eng  
        else :
           # This is going to be flipping a single spin
           j, k = int( np.floor( move / L ) ), int( move%L )
           # Your code to calculate the energy when a single spin flips goes here
           neweng = eng 

        # Now decide whether or not to accept the move
        if np.random.uniform(0,1)<min( , )  :
           # Set the energy to its new value
           eng = neweng
           # Update the spins array
           if move==L*L : 
               # YOU NEED TO ADD CODE HERE TO UPDATE THE SPINS AND THE MAGNETISATION
           else : 
               # YOU NEED TO ADD CODE HERE TO UPDATE THE SPINS AND THE MAGNETISATION

        # YOU NEED TO ADD CODE HERE TO ACCUMULATE YOUR ENSEMBLE AVERAGES

    # YOU SHOULD CALCULATE THE SUSCETIBILITY FROM THE ENSEMBLE AVERAGES HERE
    S = 0
    return S 

# Lets look at the time series of energies from our Monte Carlo simulation 
print("The suceptibility at T=2 and H=0 is", monte_carlo( 10000, 1000, 10, 20, 0, 2, 319 ) )
print("The suceptibility at T=5 and H=0 is", monte_carlo( 10000, 1000, 10, 20, 0, 5, 450 ) ) 
