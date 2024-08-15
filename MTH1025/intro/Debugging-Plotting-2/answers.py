import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-4,4,10)
y=np.sin(x)
plt.plot(x,y,'r',label='coarse')

x=np.linspace(-4,4,500)
z=np.sin(x)
plt.plot(x,z,'b',label='smooth')

plt.xlabel('x')
plt.ylabel('y')


plt.legend()

