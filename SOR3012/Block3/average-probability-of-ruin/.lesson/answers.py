import numpy as np
import scipy.stats

def random_walker(start, n, p) :
  # Your code for simulating the behaviour of the random walker 
  # goes here.  Remember your function should return 1 if the walker
  # finishes in state 0 and 0 if the walker finishes in state n
  while (start>0 and start<n ) :
     if np.random.uniform(0,1)<p : start=start+1
     else : start=start-1
  if start==0 : return 1
  else : return 0

def sample_mean(start,n,p,m) :
  # Your code to calculate the the sample mean for m random variables that are generated by calling random_walker goes here
  S, S2 = 0, 0
  for i in range(m) :
      myvar = random_walker( start, n, p )
      S, S2 = S + myvar, S + myvar*myvar 
  mean = S / m
  var = (m/(m-1))*( S2/m - mean*mean )
  lower = mean + np.sqrt( var / m )*scipy.stats.norm.ppf(0.05)
  upper = mean + np.sqrt( var / m )*scipy.stats.norm.ppf(0.95)

  # When completed this function should return
  # lower = the 5th percentile of the distribution for the sample mean
  # mean = your sample mean
  # upper = the 95th percentile of the distribution for the sample mean
  return lower, mean, upper


l, m, u = sample_mean( 5, 10, 0.3, 200 )
print("200 random walks were generated for a chain with length 10 and a probablity of winning of 0.3")
print("These random walks all started from state 5")
print("A fraction",m,"of these walks finishes in state 0")
print("Our simulations show that there is a 90% chance that the probablity of ruin lies between",l,"and",u)
