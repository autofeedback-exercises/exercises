import matplotlib.pyplot as plt
import numpy as np

# This loads the data that we are going to investigate
x = np.loadtxt("data.dat")

# Your code will go here
x.sort()
y = np.zeros( len(x) )
for i in range(len(x)) : y[i] = (i+1)/len(x)

# This will produce the final graph
plt.plot( x, y, 'k-' )
plt.xlabel("x")
plt.ylabel("cumulative distribution")
plt.savefig("cumulative-pdf.png")
