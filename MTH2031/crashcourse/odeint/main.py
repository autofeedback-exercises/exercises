from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
def dydt(y, t):
    return y/t
t = np.linspace(-5, 5, 100)
y0 = -10
y = odeint(dydt, y0, t)
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
fighand=plt.gca()

plt.figure()
def pend(y, t):
    b = 0.25
    c = 5.0
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt
p0 = [np.pi/2, 0.0]
t = np.linspace(0, 10, 100)
res = odeint(pend, p0, t)
theta = res[:, 0]
omega = res[:, 1]
plt.plot(t, theta)
plt.xlabel('t')
plt.ylabel('theta')
fighand=plt.gca()
