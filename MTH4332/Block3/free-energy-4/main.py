import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

# Read in the list of magnetisation values
mags = np.loadtxt("magnetisations")

# This is the number of bins
nbins = 50
# This is the minimum and maximum for the grid
minx, maxx = -1.1, 1.1
# This is the list of block sizes you should investigate
blocksizes = np.array([10, 20, 25, 100, 200, 250, 500])


# Your code to draw the graph described in the instructions goes here.
# I would recommend writing a function to calculate the histogram with 
# different block sizes
