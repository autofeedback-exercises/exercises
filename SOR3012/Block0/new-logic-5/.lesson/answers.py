import numpy as np

# This loads the data from values.dat into the NumPy array called xvals
xvals = np.loadtxt("mydata.dat")

# Add code so that these variables are set equal to the number of elements in 
# xvals that are less than or equal to five and that are more than five respectively
nlefive=0
nmefive=0
for xv in xvals :
    if xv<=5 : nlefive = nlefive + 1
    if xv>=5 : nmefive = nmefive + 1
