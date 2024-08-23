import numpy as np
import matplotlib.pyplot as plt
# this is the code from part 1
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x,y,'r')
xsq = [-1, 1, 1, -1, -1]
ysq = [-1, -1, 1, 1, -1]
plt.plot(xsq, ysq, 'b')
plt.axis('equal')
# your code goes here
xlist, ylist = [], []
for _ in range(1000):
    xlist.append(np.random.uniform(-1,1))
    ylist.append(np.random.uniform(-1.0,1.0))
plt.plot(xlist, ylist, 'k.')
# This line is needed for the automated feedback, don't remove it!
fighand = plt.gca()
