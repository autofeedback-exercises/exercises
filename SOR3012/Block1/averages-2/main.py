import matplotlib.pyplot as plt
import numpy as np

def uniform( a, b ) : 
  # Your code to generate a random variable that is distributed uniformly
  # between a and b goes here.
  

# You should not need to adjust any of the code from here onwards
xv, yv1, yv2, yv3, yv4 = np.linspace(1,100,100), np.zeros(100), np.zeros(100), np.zeros(100), np.zeros(100)
for i in range(100) : 
  yv1[i] = uniform(1,5) 
  yv2[i] = uniform(-5,-1)
  yv3[i] = uniform( 2.5, 3.5 )
  yv4[i] = uniform( -3.5, -2.5 )
  
plt.plot( xv, yv1, 'ro' )
plt.plot( xv, yv2, 'bo' )
plt.plot( xv, yv3, 'go' )
plt.plot( xv, yv4, 'ko' )
plt.xlabel("index")
plt.ylabel("random variable")
plt.savefig("uniform_rv.png")
