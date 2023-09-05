import numpy as np

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

