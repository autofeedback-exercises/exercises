import numpy as np

xvals = np.loadtxt("values.dat")
yvals = xvals
for i,xv in enumerate(yvals) : 
    if xv<0 : yvals[i]=-xv
