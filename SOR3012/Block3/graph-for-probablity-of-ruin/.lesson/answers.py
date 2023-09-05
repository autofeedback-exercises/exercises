import matplotlib.pyplot as plt
import numpy as np

def random_walker(start, n, p) :
  while (start>0 and start<n ) :
     if np.random.uniform(0,1)<p : start=start+1
     else : start=start-1
  if start==0 : return 1
  else : return 0

def sample_mean(start,n,p,m) :
  S = 0
  for i in range(m) :
      S = S + random_walker( start, n, p )
  return S / m

x, y = np.linspace(1,9,9), np.zeros(9)
for i in range(1,10) : y[i-1] = sample_mean(i,10,0.4,200)

print( y )
plt.plot( x, y, 'ko' )
plt.xlabel("start point")
plt.ylabel("probability of ruin")
plt.savefig("graph.png")
    
