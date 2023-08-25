import numpy as np

def getBinary( N ) : 
  # Your code goes here
  bina = np.zeros(6)
  for i in range(6) :
     pp = 2**(5-i)
     bina[i] = np.floor( N / pp )
     N = N - bina[i]*pp
  return bina 

for i in range(16) : 
  print("The binary representation of", i, "is", getBinary(i) )
