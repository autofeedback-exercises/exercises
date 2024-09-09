import numpy as np
import matplotlib.pyplot as plt
N = 100
m = np.ones(N)
x = np.random.normal(0, 1, N)
y = np.random.normal(0, 2, N)
z = np.random.normal(0, 3, N)

M = np.sum(m)
Xc = np.sum(m*x)/M
Yc = np.sum(m*y)/M
Zc = np.sum(m*z)/M
x1 = x - Xc
y1 = y - Yc
z1 = z - Zc

I = np.zeros((3,3))
I[0,0] = np.sum( m * (y1**2 + z1**2))
I[1,1] = np.sum( m * (x1**2 + z1**2))
I[2,2] = np.sum( m * (x1**2 + y1**2))
I[0,1] = -np.sum( m * x1 * y1)
I[0,2] = -np.sum( m * x1 * z1)
I[1,2] = -np.sum( m * y1 * z1)
I[1,0] = I[0,1]
I[2,0] = I[0,2]
I[2,1] = I[1,2]
