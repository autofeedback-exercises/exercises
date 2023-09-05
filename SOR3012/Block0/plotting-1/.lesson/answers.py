import matplotlib.pyplot as plt
import numpy as np

xvals = np.linspace(0,29,30)
yvals = xvals*xvals 

plt.plot( xvals, yvals, 'ko'  )
plt.xlabel("Index")
plt.ylabel('Square')
plt.savefig("squares.png")
