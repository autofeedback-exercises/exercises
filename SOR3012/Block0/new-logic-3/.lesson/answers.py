import numpy as np

# This loads the data from values.dat into the NumPy array called xvals
xvals = np.loadtxt("mydata.dat")
yvals = np.zeros(len(xvals))
for i,xv in enumerate(xvals) :
    if xv==5 : yvals[i] = 1
