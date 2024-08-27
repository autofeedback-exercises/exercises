import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
def markov_move( trans, start ) :
    myrand, myvar, accum  = np.random.uniform(0,1), 0, trans[start,0]
    while myrand>accum :
          myvar = myvar + 1
          accum = accum + trans[start,myvar]
    return myvar
def is_transition( trans, start, nsteps, target ) :
    for i in range(nsteps) :
        start = markov_move( trans, start )
    if start == target : return 1
    return 0
def sample_mean( trans, start, nsteps, target, nsamples ) :
    mean = 0
    for i in range(nsamples) : mean = mean + is_transition( trans, start, nsteps, target )
    mean = mean / nsamples
    var = mean*(1-mean)
    conf = np.sqrt( var / nsamples )*scipy.stats.norm.ppf(0.95)
    return mean, conf
# Setup the transition matrix here
A = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
# Now estimate some hitting probablities if we start from state 2
for i in range(3) :
    for j in range(3) :
        prob, conf = sample_mean( A, i, 10, j, 100 )
        print('There is a 90% probablity that element', i+1, j+1, 'of the 10-step transition probablity matrix is within', conf, 'of', prob )

A2 = np.linalg.matrix_power( A, 2)
A10 = np.linalg.matrix_power( A2, 5 )
A50 = np.linalg.matrix_power( A10, 5 )
A100 = np.linalg.matrix_power( A50, 2 )

# This is the number of steps to run with the Markov chain
nsteps = 1000
# Add code to accumulate and plot your estimate of the transition probablity matrix here
state, histo = 0, np.zeros(3)
for i in range(nsteps) :
    state = markov_move( A, state )
    histo[state] = histo[state] + 1
histo = histo / nsteps
plt.bar( [1,2,3], histo, width=0.1 )
plt.xlabel("state")
plt.ylabel("probability")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

A = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
w, lv = np.linalg.eig( A.T )
stat = lv[:,0] / sum(lv[:,0])
plt.bar( [1,2,3], stat, width=0.1 )
plt.xlabel("State")
plt.ylabel("Probability")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

# Read in the data from a file
data = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Markov_stationary_distribution/energies")[:,1]
# Your code goes here
average = sum(data) / len(data)

# Read in the data from a file
eng = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Markov_stationary_distribution/energies")[:,1]
# Create a list with 10 elements that you will use to hold the average eneriges
av_eng = np.zeros(10)
# Your code goes here
bsize = int( len(eng) / 10 )
for i in range(10) :
    av_eng[i] = sum( eng[bsize*i:bsize*(i+1)] ) / bsize
x = np.linspace(1,10,10)
plt.plot( x, av_eng, "ko")
plt.xlabel("Index")
plt.ylabel("Average energy / natural units")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

# Read in the energies from a file
data = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Markov_stationary_distribution/energies")[:,1]
# Create a list with 10 elements that you will use to hold the variances
variances = np.zeros(10)
data2 = data*data
# Your code goes here
for i in range(10) :
    mean = sum( data[100*i:100*(i+1)] ) / 100
    mean2 = sum( data2[100*i:100*(i+1)] ) / 100
    variances[i] = (100/99)*( mean2 - mean*mean )
mean = sum( data ) / len(data)
mean2 = sum( data2 ) / len(data)
total_var = (len(data)/(len(data)-1))*( mean2 - mean*mean )
# This will draw a graph of your variances
x = np.linspace( 1, 10, 10 )
plt.plot( x, variances, 'ko')
plt.plot( [1,10], [total_var,total_var], 'r-' )
plt.xlabel("Index")
plt.ylabel("Variance / energy^2")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

# Read in the energies from a file
data = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Markov_stationary_distribution/energies")[:,1]
# Create a list to hold the block averages
blocks = np.zeros(10)
# Your code goes here
k=0
for i in range( len(data) ) :
  blocks[k] = blocks[k] + data[i]
  if (i+1)%100==0 and i>0 :
    blocks[k] = blocks[k] / 100
    k = k + 1
mean, sq = 0, 0
for bb in blocks : mean, sq = mean + bb, sq + bb*bb
average, sq = mean / len(blocks), sq / len(blocks)
var = ( len(blocks) / ( len(blocks) - 1 ) ) * ( sq - average*average )
error = np.sqrt( var / len(blocks) )
print( average, error )

def block_average( M, data ) :
  # Your code goes here
  nblocks = int( np.floor(len(data) / M) )
  blocks = np.zeros( nblocks )
  k=0
  for i in range( len(data) ) :
    if k>=nblocks : break
    blocks[k] = blocks[k] + data[i]
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
data = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Markov_stationary_distribution/energies")[:,1]
i, errors, block_sizes = 0, 10*[0], [10,20,30,40,60,100,120,200,300,400]
for bb in block_sizes :
  errors[i] = block_average( bb, data )
  i = i + 1
# And plot a graph
plt.plot( block_sizes, errors, 'k.-' )
plt.xlabel("Size of blocks")
plt.ylabel("Error")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()
