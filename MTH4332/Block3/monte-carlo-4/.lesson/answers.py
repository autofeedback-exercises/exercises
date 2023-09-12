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
