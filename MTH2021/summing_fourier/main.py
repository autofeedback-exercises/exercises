import numpy as np
def fourierSum(Bn, x, l):
    S = 0
    for n in range(len(Bn)):
        S += Bn[n] * np.sin((n+1)*np.pi*x/l)
    return S
