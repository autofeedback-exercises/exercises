import numpy as np

def better_sqrt(x):
  if x>=0:
    return np.sqrt(x)
  else:
    return (1j*np.sqrt(-x))


