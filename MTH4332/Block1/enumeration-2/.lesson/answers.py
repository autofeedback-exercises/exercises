import numpy as np

def convertToBase( N, base ) :
  # Your code goes here
  state, v = np.zeros(7), N 
  for i in range(7) :
      vv = base**(6-i)
      state[i] = np.floor( v / vv )
      v = v - state[i]*vv
  return state
 

# This will print some output that will allow you to test your function
for b in range(2,10) :
  for n in range(10) :
    print("The number", n, "in base", b, "is", convertToBase(n,b) )
