import numpy as np
import matplotlib.pyplot as plt
theta=np.linspace(0,2*np.pi,1000)
x=np.cos(theta)
y=np.sin(theta)
plt.plot(x,y,'k')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
fighand=plt.gca()
