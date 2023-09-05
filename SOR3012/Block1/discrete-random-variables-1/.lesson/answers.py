import matplotlib.pyplot as plt
import numpy as np

# Your code goes here
xvals, random_variables = np.zeros(100), np.zeros(100)
for i in range(100) : 
    xvals[i] = i+1
    random_variables[i] = np.random.uniform(0,1)

plt.plot( xvals, random_variables, 'ko' )
plt.xlabel("Index")
plt.ylabel("random variable")
plt.savefig("random.png")
