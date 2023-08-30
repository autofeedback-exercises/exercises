import numpy as np

def circle_estimate(N) : 
  # Your code goes here
  estimate = 0 
  for i in range(100) : 
      x = np.random.uniform(0,1)
      y = np.random.uniform(0,1)
      if x*x+y*y<1 : estimate = estimate + 1
  return estimate / N
  
# Three estimates for the area of the circle based on a random grid
# of 1000 points are printed here
print( circle_estimate(1000), circle_estimate(1000), circle_estimate(1000) )
