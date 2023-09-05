import matplotlib.pyplot as plt
import numpy as np

Q = np.array( [[1/3,1/3,0],[1/2,0,1/2],[1/2,0,0]] )
R = np.array( [[1/3,0],[0,0],[0,1/2]] )

mat = np.identity(3) - Q 
inv = np.linalg.inv( mat )
probs = np.dot( inv, R )

plt.bar( [2,3,4], probs[:,1], width=0.1 )
plt.xlabel("Initial state")
plt.ylabel("Probability of absorption in state 5")
plt.savefig("hitting-probs.png")
