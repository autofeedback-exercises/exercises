import matplotlib.pyplot as plt
import numpy as np 

xvals = np.zeros(100)
xvals[0], xvals[1] = 1, 2
fibonacci = np.ones(100)
# Insert your code for the fibonacci series here
for i in range(2,100) :
  xvals[i]=i+1
  fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

plt.plot( xvals, fibonacci, 'ko' )
plt.xlabel("Index")
plt.ylabel("Fibonacci series")
plt.savefig("fibonacci.png" )
