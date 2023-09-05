import matplotlib.pyplot as plt
import numpy as np

Q = np.array([[1/3,1/3,0],[0.5,0,0.5],[0.5,0,0]])

inv = np.linalg.inv( np.identity(3) - Q ) 
times = np.dot( inv, np.array([1,1,1]) )

plt.bar( [2,3,4], times, width=0.1 ) 
plt.xlabel("Initial state")
plt.ylabel("Expected number of steps till absorbtion")
plt.savefig("hitting_probs.png")
