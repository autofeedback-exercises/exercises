import matplotlib.pyplot as plt
import numpy as np 

xvals = np.zeros(100)
triangularNumbers = np.zeros(100)
# Insert your code to compute the triangular numbers here



plt.plot( xvals, triangularNumbers, 'ko' )
plt.xlabel("Index")
plt.ylabel("Triangular Numbers")
plt.savefig("triangular.png" )
