import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-7,7,1000)
f = np.sin(4*x)
g = np.sin(5*x)

xf = np.linspace(-2*np.pi,2*np.pi,17)
xg = np.linspace(-2*np.pi,2*np.pi,21)
zf=np.zeros(17)
zg=np.zeros(21)

plt.plot(x,f,'b-')
plt.plot(x,g,'r--')
plt.plot(xf,zf,'bo')
plt.plot(xg,zg,'rD')
plt.legend(['sin(4x)','sin(5x)'])
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-2*np.pi,2*np.pi,-1.5,1.5])
fighand = plt.gca()
