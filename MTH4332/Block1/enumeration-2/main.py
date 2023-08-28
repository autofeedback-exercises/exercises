import numpy as np

def convertToBase( N, base ) :
  # Your code goes here
  

# This will print some output that will allow you to test your function
for b in range(2,10) :
  for n in range(10) :
    print("The number", n, "in base", b, "is", convertToBase(n,b) )
