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
# you're going to edit this code as per the instructions above
xin, xout, yin, yout = [], [], [], []
for _ in range(1000):
    xpt = np.random.uniform(-1,1)
    ypt = np.random.uniform(-1.0,1.0)
    if (xpt*xpt + ypt*ypt) < 1:
        xin.append(xpt)
        yin.append(ypt)
    else:
        xout.append(xpt)
        yout.append(ypt)
plt.plot(xin, yin, 'r.')
plt.plot(xout, yout, 'b.')
# This line is needed for the automated feedback, don't remove it!
fighand = plt.gca()
