import matplotlib.pyplot as plt
import numpy as np

frequencies = np.array([1,1,2,2,2,3,4,5,9]) 
T = np.linspace( 0.1, 30, 200 )
CV = np.zeros(200)
for i, temp in enumerate(T) : 
    b = np.exp(-frequencies/temp)
    nb = 1-b
    CVall = (frequencies*frequencies)/(temp*temp)*( b /nb + b*b/(nb*nb) )
    CV[i] = sum(CVall)/3

plt.plot( T, CV, 'k-')
plt.xlabel("Temperature / natural units")
plt.ylabel("Heat capacity per atom / natural units")
plt.savefig("heat-capacity-9dof.png")

