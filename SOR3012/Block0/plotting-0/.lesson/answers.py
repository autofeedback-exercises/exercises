import matplotlib.pyplot as plt
import numpy as np

xvals, yvals = np.zeros(11), np.zeros(11)
for i in range(11) : 
    xvals[i] = i 
    yvals[i] = 7*i 

plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Index")
plt.ylabel("Seven times table")
plt.savefig("seven-times-table.png")
