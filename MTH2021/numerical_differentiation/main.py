import numpy as np
N = 101
x = np.linspace(-5, 5, N)
h = x[1] - x[0]
f = np.exp(-x**2)
D = np.eye(N)
for ii in range(1,N-1):
    D[ii, ii-1] = 1
    D[ii, ii] = -2
    D[ii, ii+1] = 1
D[0,0] = 0
D[N-1,N-1] = 0
D = (1/(h*h)) * D
f2p = np.dot(D, f)
