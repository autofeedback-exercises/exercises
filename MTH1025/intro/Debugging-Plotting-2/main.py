import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-4, 4, 10) 
y=np.sin(x)

x=np.linspace(-4, 4, 500)
z=np.sin(x)

plt.xlabel(x)
plt.ylabel(y)
plt.legend()
plt.savefig("sinx.png" )