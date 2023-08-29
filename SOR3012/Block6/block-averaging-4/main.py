import matplotlib.pyplot as plt
import numpy as np

# Read in the energies from a file
eng = np.loadtxt("energies")[:,1]

# Create a list to hold the block averages
blocks = np.zeros(10)

# Your code goes here
