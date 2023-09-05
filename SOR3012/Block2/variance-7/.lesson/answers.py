import matplotlib.pyplot as plt
import numpy as np

myvar = np.random.uniform(0,1)
ssum, ssum2 = myvar, myvar*myvar 
indices, S2 = np.zeros(200), np.zeros(200)
for i in range(200) : 
  # Add code to setup the numpy arrays called indices and average to generate the desired plot here.
  indices[i] = i+2
  myvar = np.random.uniform(0,1)
  ssum, ssum2 = ssum + myvar, ssum2 + myvar*myvar 
  mean = ssum / indices[i] 
  S2[i] = (indices[i] / (indices[i]-1))*( ssum2 / indices[i] - mean*mean )

plt.plot( indices, S2, 'ro' )
plt.xlabel("Number of random variables")
plt.ylabel("Sample variance")
plt.savefig("variance.png") 
