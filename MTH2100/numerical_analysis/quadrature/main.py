import numpy as np
import matplotlib.pyplot as plt
trap_error, simp_error = [], []
h_vals = []
N_vals = np.arange(10, 40, 2)
for n in N_vals:
    trap_error.append(exact - trapezoidal(f_demo, 0, 2, n))
    simp_error.append(exact - simpsons(f_demo, 0, 2, n))
    h_vals.append(2/n)
plt.semilogy(h_vals, trap_error, 'ro', label='Trapezium')
plt.semilogy(h_vals, simp_error, 'bo', label="Simpson's")
plt.xlabel('interval size, h')
plt.ylabel('Abs(Error)')
plt.legend()
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def simpson_func(f, a, b, N):
    from scipy.integrate import simpson
    x = np.linspace(a, b, N+1)
    y = f(x)
    return simpson(y, x)

from scipy.integrate import fixed_quad
def fsin(x):
    return np.sin(np.pi*x*x)
I_exact,_  = fixed_quad(fsin, 0, 1, n=1001)
for N in range(3, 21, 2):
    IG, _ = fixed_quad(fsin, 0, 1, n=N)
    IS = simpson_func(fsin, 0, 1, N=N-1)
    plt.semilogy(N, abs(I_exact-IG), 'ro')
    plt.semilogy(N, abs(I_exact-IS), 'bo')
    plt.xlabel('Number of nodes')
    plt.ylabel('Abs(Error)')
    plt.legend(['GL quadrature', 'Simpsons rule'])