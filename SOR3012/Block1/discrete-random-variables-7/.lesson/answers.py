import numpy as np

def bernoulli(p) :
  # Your code to generate a bernoulli random variable goes here.
  if np.random.uniform(0,1)<p : return 1
  return 0

def geometric(p): 
  # Your code to generate a geometric random variable goes here
  nt = 1
  while bernoulli(p)==0 : nt = nt + 1
  return nt  

print( geometric(0.5), geometric(0.5), geometric(0.5), geometric(0.5) )
