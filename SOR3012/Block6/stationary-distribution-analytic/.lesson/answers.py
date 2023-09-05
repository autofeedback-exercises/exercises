import matplotlib.pyplot as plt
import numpy as np

A = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
w, lv = np.linalg.eig( A.T )

stat = lv[:,0] / sum(lv[:,0])

plt.bar( [1,2,3], stat, width=0.1 )
plt.xlabel("State")
plt.ylabel("Probability")
plt.savefig("distribution.png")
