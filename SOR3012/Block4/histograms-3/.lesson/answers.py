import numpy as np

def myvariable( probs ) : 
  myvar = np.random.uniform(0,1) 
  if myvar < probs[0] : return 0
  if myvar < probs[0] + probs[1] : return 1
  if myvar < probs[0] + probs[1] + probs[2] : return 2 
  if myvar < probs[0] + probs[1] + probs[2] + probs[3] : return 3
  return 4 
  
probs = np.array([0.5, 0.1, 0.2, 0.05, 0.15 ])  # You need to fill in the rest of this vector
print( myvariable( probs ), myvariable( probs ), myvariable( probs ) )
