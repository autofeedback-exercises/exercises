import matplotlib.pyplot as plt
import numpy as np 

xvals = np.zeros(100)
fibonacci = np.zeros(100)
# Insert your code for the fibonacci series here



plt.plot( xvals, fibonacci, 'ko' )
plt.xlabel("Index")
plt.ylabel("Fibonacci series")
plt.savefig("fibonacci.png" )
