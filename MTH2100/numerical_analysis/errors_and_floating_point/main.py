import numpy as np
import matplotlib.pyplot as plt
def forward_diff(f, x, h):
    """given a function (f), a value (x) and a grid spacing (h), compute the forward difference formula for f'(x)"""
    return (f(x+h) - f(x))/h
def backward_diff(f, x, h):
    return (f(x)-f(x-h))/h
def central_diff(f, x, h):
    return (f(x+h)-f(x-h))/(2*h)

h_values = [0.1**n for n in range(1,16)]
err_fwd = np.array([abs(forward_diff(np.sin, 1.0, h) - np.cos(1.0)) for h in h_values])
err_bwd = np.array([abs(backward_diff(np.sin, 1.0, h) - np.cos(1.0)) for h in h_values])
err_cen = np.array([abs(central_diff(np.sin,  1.0, h) - np.cos(1.0)) for h in h_values])
plt.loglog(h_values, err_fwd, 'b-', label='Forward') 
plt.loglog(h_values, err_bwd, 'g--', label='Backward')
plt.loglog(h_values, err_cen, 'r-', label='Central')
plt.xlabel('Step size')
plt.ylabel('Absolute error')
plt.legend()
# don't delete this line: it's needed for the Automated Feedback
fighand = plt.gca()

def second_diff(f, x, h):
    return (f(x+h)+f(x-h)-2*f(x))/(h**2)
err_2nd = np.array([abs(second_diff(np.exp, 1.0, h) - np.e) for h in h_values])
plt.loglog(h_values, err_2nd, 'b-', label='Central') 
plt.xlabel('Step size')
plt.ylabel('Absolute error')
plt.legend()
# don't delete this line: it's needed for the Automated Feedback
fighand = plt.gca()