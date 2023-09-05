import numpy as np

def myvariable( probs ) : 
  myvar = np.random.uniform(0,1) 
  if myvar < probs[0] : return 0
  if myvar < probs[0] + probs[1] : return 1
  # You will need to write the rest of this function here
  
probs = np.array([0.5, 0.1, ])  # You need to fill in the rest of this vector
print( myvariable( probs ), myvariable( probs ), myvariable( probs ) )
