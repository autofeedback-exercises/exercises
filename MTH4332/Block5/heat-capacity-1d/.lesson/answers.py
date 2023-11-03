import matplotlib.pyplot as plt
import numpy as np

frequency = 1.0 
T = np.linspace( 0.1, 10, 200 )
b = np.exp(-frequency/T)
nb = 1-b
CV = (frequency*frequency)/(T*T)*( b /nb + b*b/(nb*nb) )

plt.plot( T, CV, 'k-')
plt.xlabel("Temperature / natural units")
plt.ylabel("Heat capacity / natural units")
plt.savefig("heat-capacity-1dof.png")

