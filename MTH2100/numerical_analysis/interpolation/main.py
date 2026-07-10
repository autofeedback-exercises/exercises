import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator
x_fine = np.linspace(-20, 20, 550)
def runge(x):
    return 1 / (25 + x**2)
x5 = np.linspace(-20, 20, 5)
x11 = np.linspace(-20, 20, 11)
y5 = runge(x5)
y11 = runge(x11)
poly5 = BarycentricInterpolator(x5, y5)
poly11 = BarycentricInterpolator(x11, y11) 
plt.plot(x_fine, poly5(x_fine), label='poly5')
plt.plot(x_fine, poly11(x_fine), label='poly11')
plt.plot(x_fine, runge(x_fine), label='Runge')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

# your code goes here
def oscillator(x):
    return np.sin(20*x)
x20 = np.linspace(0, 2*np.pi, 20)
x21 = np.linspace(0, 2*np.pi, 21)
plt.plot(x20, oscillator(x20),'ro')
plt.plot(x21, oscillator(x21),'bo')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

from scipy.interpolate import UnivariateSpline
x_noisy, y_noisy = np.loadtxt('noisy_data.txt')
plt.plot(x_noisy, y_noisy, 'ro')
x_fine = np.linspace(0, 2*np.pi, 100)
# Calculate the three different splines and plot them using x_fine as the x values
s0 = UnivariateSpline(x_noisy, y_noisy, s=0)(x_fine)
s1 = UnivariateSpline(x_noisy, y_noisy, s=1)(x_fine)
s01 = UnivariateSpline(x_noisy, y_noisy, s=0.1)(x_fine)
plt.plot(x_fine,s0, label='no smoothing')
plt.plot(x_fine,s1, label='over smoothed')
plt.plot(x_fine,s01, label='just right')
plt.legend()
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()