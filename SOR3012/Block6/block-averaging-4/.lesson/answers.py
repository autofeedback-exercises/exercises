import matplotlib.pyplot as plt
import numpy as np

# Read in the energies from a file
eng = np.loadtxt("energies")[:,1]

# Create a list to hold the block averages
blocks = np.zeros(10)

# Your code goes here
k=0
for i in range( len(eng) ) :
  blocks[k] = blocks[k] + eng[i] 
  if (i+1)%100==0 and i>0 : 
    blocks[k] = blocks[k] / 100
    k = k + 1
  
mean, sq = 0, 0  
for bb in blocks : mean, sq = mean + bb, sq + bb*bb
average, sq = mean / len(blocks), sq / len(blocks)
var = ( len(blocks) / ( len(blocks) - 1 ) ) * ( sq - average*average )
error = np.sqrt( var / len(blocks) )
print( average, error )
