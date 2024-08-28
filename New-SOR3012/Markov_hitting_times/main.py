import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
def myvariable( probs ) :
    myvar = np.random.uniform(0,1)
    if myvar < probs[0] : return 0
    if myvar < probs[0] + probs[1] : return 1
    # You will need to write the rest of this function here
    if myvar < probs[0] + probs[1] + probs[2] : return 2
    if myvar < probs[0] + probs[1] + probs[2] + probs[3] : return 3
    if myvar < probs[0] + probs[1] + probs[2] + probs[3] + probs[4] : return 4
probs = np.array([0.5, 0.1, 0.2, 0.05, 0.15 ])  # You need to fill in the rest of this vector
print( myvariable( probs ), myvariable( probs ), myvariable( probs ) )

def myvariable( probs ) :
    myrand = np.random.uniform(0,1)
    myvar, accum = 0, probs[0]
    while myvar>accum:
        # You will need to write contents of the while loop here and the
        # condition for leaving the loop on the previous line.  Notice that
        # I have defined three quantities and written a return statement below
        # to give you a clue as to how to proceed.
        myvar += 1
        accum += probs[myvar]
    return myvar
probs = np.array([0.5, 0.1, 0.2, 0.05, 0.15 ])
print( myvariable( probs ), myvariable( probs ), myvariable( probs ) )

def markov_move( trans, start ) :
    myrand, myvar, accum  = np.random.uniform(0,1), 0, trans[start,0]
    while myrand>accum :
          myvar = myvar + 1
          accum = accum + trans[start,myvar]
    return myvar
# Setup the transition matrix
A = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
# Now generate a random move if we start in state 0
print( markov_move( A, 0 ), markov_move( A, 0 ), markov_move( A, 0 ) )
# Now generate a random move if we start in state 1
print( markov_move( A, 1 ), markov_move( A, 1 ), markov_move( A, 1 ) )
# Now generate a random move if we start in state 2
print( markov_move( A, 2 ), markov_move( A, 2 ), markov_move( A, 2 ) )

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
plt.plot(xv,yv)
plt.xlabel('Index')
plt.ylabel('Number of steps till absorption')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def endstate( trans, start ) :
    while start!=0 and start!=4 :
       start = markov_move( trans, start )
    if start==0 : return 0
    return 1
def sample_mean( trans, start, nsamples ) :
    m = 0
    for i in range(nsamples) : m = m + endstate( trans, start )
    mean = m / nsamples
    var = mean*(1-mean)
    conf = np.sqrt( var / nsamples )*scipy.stats.norm.ppf(0.95)
    return mean, conf
# Setup the transition matrix here
A = np.array([[1,0,0,0,0],[1/3,1/3,1/3,0,0],[0,0.5,0,0.5,0],[0,0.5,0,0,0.5],[0,0,0,0,1]])
# Now estimate some hitting probablities if we start from state 2
prob, conf = sample_mean( A, 1, 100 )
print('There is a 90% probablity that the conditional probablity of finishing in state 5 given you start in state 2 is within', conf, 'of', prob )
prob, conf = sample_mean( A, 2, 100 )
print('There is a 90% probablity that the conditional probablity of finishing in state 5 given you start in state 3 is within', conf, 'of', prob )
prob, conf = sample_mean( A, 3, 100 )
print('There is a 90% probablity that the conditional probablity of finishing in state 5 given you start in state 4 is within', conf, 'of', prob )

Q = np.array( [[1/3,1/3,0],[1/2,0,1/2],[1/2,0,0]] )
R = np.array( [[1/3,0],[0,0],[0,1/2]] )
mat = np.identity(3) - Q
inv = np.linalg.inv( mat )
probs = np.dot( inv, R )
plt.bar( [2,3,4], probs[:,1], width=0.1 )
plt.xlabel("Initial state")
plt.ylabel("Probability of absorption in state 5")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

Q = np.array([[1/3,1/3,0],[0.5,0,0.5],[0.5,0,0]])
inv = np.linalg.inv( np.identity(3) - Q )
times = np.dot( inv, np.array([1,1,1]) )
plt.bar( [2,3,4], times, width=0.1 )
plt.xlabel("Initial state")
plt.ylabel("Expected number of steps till absorbtion")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()
