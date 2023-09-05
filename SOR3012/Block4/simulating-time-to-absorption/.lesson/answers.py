import matplotlib.pyplot as plt
import numpy as np


def markov_move( trans, start ) :
    myrand, myvar, accum  = np.random.uniform(0,1), 0, trans[start,0]
    while myrand>accum : 
          myvar = myvar + 1
          accum = accum + trans[start,myvar]
    return myvar


def nsteps_to_absorption( trans, start ) :
   nsteps = 0
   while start!=0 and start!=4 :
       start = markov_move( trans, start )
       nsteps = nsteps + 1
   return nsteps

# Setup the transition matrix here
A = np.array([[1,0,0,0,0],[1/3,1/3,1/3,0,0],[0,0.5,0,0.5,0],[0,0.5,0,0,0.5],[0,0,0,0,1]])

xv, yv = np.zeros(20), np.zeros(20) 
for i in range(20) :
    xv[i], yv[i] = i+1, nsteps_to_absorption( A, 1 )

plt.plot( xv, yv, 'ko' )
plt.xlabel("Index")
plt.ylabel("Number of steps till absorption")
plt.savefig("samples.png")
