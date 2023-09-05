import matplotlib.pyplot as plt
import numpy as np 

def sample_mean(m) : 
  # Your code to calculate a  sample mean from m 
  # uniform random variables between 0 and 1 goes here
  v = 0
  for i in range(m) : v = v + np.random.uniform(0,1)
  return v/m  
  
def variance(n,m) : 
  # Your code to estimate the variance for a set of n 
  # sample means, which are each computed from m 
  # uniform random variables between 0 and 1 goes here.
  s, s2 = 0, 0 
  for i in range(n) :
      vv = sample_mean(m) 
      s = s + vv 
      s2 = s2 + vv*vv 
  s = s / n
  return ( n/(n-1) )*( s2 / n - s*s )  

xvals, yvals = np.zeros(50), np.zeros(50) 
for i in range(50) : 
  # Your code to set xvals and yvals as described in the panel
  # on the right goes here
  xvals[i] = i+1
  yvals[i] = variance(10,i+1)

plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Number of variables used to calculate mean")
plt.ylabel("Variance")
plt.savefig("variance_change.png")
  

