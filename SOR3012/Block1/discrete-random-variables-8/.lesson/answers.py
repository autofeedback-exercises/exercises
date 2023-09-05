import matplotlib.pyplot as plt
import numpy as np

# You may wish to write some code here

def geometric(p) :
  # Your code for generating a geometric random variable goes here
  nt = 1
  while np.random.uniform(0,1)>p : nt = nt + 1
  return nt 
 
# Your code for generating the list of geometric random variables goes here
prob = 0.5
xvals, yvals = np.zeros(100), np.zeros(100)
for i in range(100) : 
    xvals[i] = i+1 
    yvals[i] = geometric(prob)

plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Index")
plt.ylabel("random variable")
plt.savefig("geometric.png")
  
