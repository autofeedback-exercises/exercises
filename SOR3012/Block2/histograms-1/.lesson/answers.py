import numpy as np

def bernoulli(p) : 
  # Your code to generate a bernoulli random variable goes here
  if np.random.uniform(0,1)<p : return 1
  return 0 
 
def repeated_trials(n,p) :
  nsuccess, nfail = 0, 0
  # Your code to generate n bernoulli trials and to count the number of 
  # successes and failures goes here.
  for i in range(n) : 
      nsuccess = nsuccess + bernoulli(p)
  nfail = n - nsuccess 
  return nsuccess, nfail
  
print( repeated_trials(10,0.2) )
print( repeated_trials(10,0.2) )
print( repeated_trials(10,0.2) )
print( repeated_trials(10,0.2) )
