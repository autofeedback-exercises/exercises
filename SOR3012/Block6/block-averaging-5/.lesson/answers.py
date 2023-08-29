import matplotlib.pyplot as plt
import numpy as np

def block_average( M, data ) :
  # Your code goes here
  nblocks = int( np.floor(len(data) / M) ) 
  blocks = nblocks*[0]

  k=0
  for i in range( len(eng) ) :
    blocks[k] = blocks[k] + eng[i] 
    if (i+1)%M==0 and i>0 : 
      blocks[k] = blocks[k] / M
      k = k + 1
  
  mean, sq = 0, 0  
  for bb in blocks : mean, sq = mean + bb, sq + bb*bb
  average, sq = mean / len(blocks), sq / len(blocks)
  var = ( len(blocks) / ( len(blocks) - 1 ) ) * ( sq - average*average )
  error = np.sqrt( var / len(blocks) ) 
  return error

# Read in the energies from a file
eng = np.loadtxt("energies")[:,1]

i, errors, block_sizes = 0, 10*[0], [10,20,30,40,60,100,120,200,300,400]
for bb in block_sizes :
  errors[i] = block_average( bb, eng )
  i = i + 1
  
# And plot a graph
plt.plot( block_sizes, errors, 'k.-' )
plt.xlabel("Size of blocks")
plt.ylabel("Error")
plt.savefig("myplot.png")
