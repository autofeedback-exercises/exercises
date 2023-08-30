import numpy as np

def potential(x) :
  energy = 0
  force = 0
  # Your code goes here
  
  return energy, force
  

# This calculates and force and prints the energy of the configuration in the input file.
pot, force = potential(-1)
print( "The potential at x=-1 is", pot, "and the force is", force )
pot, force = potential(0)
print( "The potential at x=0 is", pot, "and the force is", force ) 
pot, force = potential(1)
print( "The potential at x=1 is", pot, "and the force is", force ) 
