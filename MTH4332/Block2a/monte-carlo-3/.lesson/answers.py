import numpy as np

def area(N) : 
  nin = 0 
  for i in range(N) : 
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    if x*x + y*y < 1 : nin = nin + 1
  return nin / N
  
print( area(1000), area(1000), area(1000) )

def myerrors(N,M) : 
  # Your code goes here.
  l, m, u = 0, 0, 0
  samples = np.zeros(M) 
  for i in range(M) : samples[i] = area(N)
  l = np.percentile( samples, 5 )
  m = np.median( samples )
  u = np.percentile( samples, 95 ) 
  return l, m, u
  

print( myerrors(1000, 100) )
