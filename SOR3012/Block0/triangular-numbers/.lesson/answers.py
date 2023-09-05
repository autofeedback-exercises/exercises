import matplotlib.pyplot as plt
import numpy as np 

xvals = np.zeros(100)
triangularNumbers = np.zeros(100)
# Insert your code to compute the triangular numbers here
for i in range(1,100) : 
    xvals[i]=i
    triangularNumbers[i] = triangularNumbers[i-1] + i


plt.plot( xvals, triangularNumbers, 'ko' )
plt.xlabel("Index")
plt.ylabel("Triangular Numbers")
plt.savefig("triangular.png" )
