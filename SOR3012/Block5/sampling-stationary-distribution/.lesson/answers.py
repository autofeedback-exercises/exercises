import matplotlib.pyplot as plt
import numpy as np

def markov_move( trans, start ) : 
    # Your code for generating the moves of the Markov chain goes here
    myrand, myvar, accum  = np.random.uniform(0,1), 0, trans[start,0]
    while myrand>accum :
          myvar = myvar + 1
          accum = accum + trans[start,myvar]
    return myvar
 
A = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])     # Set this variable equal to the transition matrix that you are given in the readme

# This is the number of steps to run with the Markov chain
nsteps = 1000
# Add code to accumulate and plot your estimate of the transition probablity matrix here
state, histo = 0, np.zeros(3)
for i in range(nsteps) : 
    state = markov_move( A, state )
    histo[state] = histo[state] + 1

histo = histo / nsteps
plt.bar( [1,2,3], histo, width=0.1 )
plt.xlabel("state")
plt.ylabel("probability")
plt.savefig("stationary_distribution.png")
