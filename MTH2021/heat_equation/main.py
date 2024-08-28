import numpy as np
def fourierSum(Bn, x, l, t, K):
    S = 0
    for n in range(len(Bn)):
        S += Bn[n] * np.sin((n+1)*np.pi*x/l) * np.exp(
            -(((n+1)*np.pi/l)**2)*K*t
        )
    return S
