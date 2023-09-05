import numpy as np

# This loads the data that we are going to investigate
x = np.loadtxt("data.dat")

# Your code will go here
N = len(x)
L = min(x)
U = max(x)
