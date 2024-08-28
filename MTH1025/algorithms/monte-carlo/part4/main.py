import numpy as np
def estimate_pi(N):
    counter = 0
    for _ in range(N):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x*x + y*y < 1.0:
            counter += 1
    return(4*counter/N)
