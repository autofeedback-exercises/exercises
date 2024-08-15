import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,0.5,1])

g0=np.array([1,1,1])
g1=np.cos(x)
g2=np.sin(x)

A=np.array([g0,g1,g2])
A=A.transpose()
print(np.linalg.solve(A,[0,0,0]))
