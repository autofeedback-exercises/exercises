import numpy as np
import matplotlib.pyplot as plt
# your code goes here
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x,y,'r')
xsq = [-1, 1, 1, -1, -1]
ysq = [-1, -1, 1, 1, -1]
plt.plot(xsq, ysq, 'b')
plt.axis('equal')
# This line is needed for the automated feedback, don't remove it!
fighand = plt.gca()
