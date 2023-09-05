import numpy as np

def bernoulli(p):
  # Your code to generate the bernoulli random variable goes here
  if np.random.uniform(0,1)<p : return 1
  return 0

def binomial(n,p) :
  # Your code to generate the binomial random variable goes here.
  var = 0
  for i in range(n) : var = var + bernoulli(p)
  return var

print( binomial(5,0.5), binomial(5,0.5), binomial(5,0.5) )
