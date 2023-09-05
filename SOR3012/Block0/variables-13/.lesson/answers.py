import matplotlib.pyplot as plt
import numpy as np

xvals = np.linspace(0,19,20)
yvals = 0.5**xvals 

plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Index")
plt.ylabel("Geometric series")
plt.savefig("geometric.png")
