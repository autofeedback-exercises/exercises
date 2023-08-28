import numpy as np
import matplotlib.pyplot as plt

theta=np.linspace(0,np.pi,1000)
x=np.cos(theta)
y=np.sin(theta)

plt.plot(x,theta)
plt.axis('equal')

plt.savefig('circle.png')