import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
def delta_f(f, delta_x):
    return np.cos(f) * delta_x
f_array = [0] 
x_array = [0]
delta_x = 0.01 
N_steps = int(10/delta_x)
for _ in range(N_steps):
    f_array.append(f_array[-1] + delta_f(f_array[-1], delta_x))
    x_array.append(x_array[-1] + delta_x)
plt.plot(x_array, f_array, 'r,')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def euler(f, t0, y0, t_end, h):
    '''
    Integrate dy/dt = f(t, y) from t0 to t_end using Euler
    '''
    y0 = np.atleast_1d(np.array(y0, dtype=float))
    t  = np.arange(t0, t_end + h/2, h)
    y  = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(len(t) - 1):
        ti, yi = t[i], y[i]
        # calculate [dx/dt, dv/dt]
        delta = f(ti, yi)
        # [x', v'] = [x, v]  + [dx, dv]
        y[i+1] = yi + h * np.asarray(delta)
    return t, y.T
def update_inhomo(x, state):
    y, v = state
    return [v, 3*x+2+v+6*y]
x, s = euler(update_inhomo, 0, [0.3, 0], 1, 0.01)
plt.plot(x, s[0], label='position')
plt.xlabel('x')
plt.ylabel('y')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

g = 9.8
L = 1
def pendulum(t, state):
    theta, phi = state
    return [phi, -(g/L)*np.sin(theta)]
def simple(t, state):
    theta, phi = state
    return [phi, -(g/L)*theta]
y0 = [0, 1.5]
sol_exact = solve_ivp(fun=pendulum, t_span=(0,10), y0=y0, method='RK45', rtol=1e-8, atol=1e-10)
sol_simpl = solve_ivp(fun=simple, t_span=(0,10), y0=y0, method='RK45', rtol=1e-8, atol=1e-10)
plt.plot(sol_exact.t, sol_exact.y[1])
plt.plot(sol_simpl.t, sol_simpl.y[1])
plt.show()

def rk4(f, t0, y0, t_end, h):
    '''
    Integrate dy/dt = f(t, y) from t0 to t_end using classical RK4.
    '''
    y0 = np.atleast_1d(np.array(y0, dtype=float))
    t  = np.arange(t0, t_end + h/2, h)
    y  = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(len(t) - 1):
        ti, yi = t[i], y[i]
        # Four slope evaluations
        k1 = np.asarray(f(ti,         yi))
        k2 = np.asarray(f(ti + h/2,   yi + h/2 * k1))
        k3 = np.asarray(f(ti + h/2,   yi + h/2 * k2))
        k4 = np.asarray(f(ti + h,     yi + h   * k3))
        # Weighted average: k1 and k4 get weight 1; k2 and k3 get weight 2
        y[i+1] = yi + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
    return t, y.T
def stiff(t, state):
    y = state[0]
    return [-1000*y + 3000 - 2000*np.exp(-t)]
y0 = [1]
for h in [0.2, 0.02, 0.002]:
    t, sol = rk4(f=stiff, t0=0, y0=y0, t_end=50, h=h)
    plt.plot(t, sol[0])
plt.figure()
sol_rk4= solve_ivp(fun=stiff, t_span=(0,50), y0=y0, method='RK45', rtol=1e-8, atol=1e-10)
print(sol_rk4.nfev)
sol_rad = solve_ivp(fun=stiff, t_span=(0,50), y0=y0, method='Radau', rtol=1e-8, atol=1e-10)
print(sol_rad.nfev)
plt.plot(sol_rk4.t, sol_rk4.y[0], 'r')
plt.plot(sol_rad.t, sol_rad.y[0], 'b')
plt.plot(t, sol[0],'k,')
plt.show()

omega = 10
rho = 28
beta = 8/3
def butterfly(t, state):
    x, y, z = state
    return [omega * (y-x), x*(rho-z)-y, x*y-beta*z]
y0 = [1, 1, 1]
sol1 = solve_ivp(fun=butterfly, t_span=(0,40), y0=y0, method='RK45', rtol=1e-8, atol=1e-10)
ax = plt.figure().add_subplot(projection='3d')
ax.plot(*sol1.y)  # sol.y is (3, n_steps), so *sol.y unpacks to x, y, z arrays
ax.plot(*y0, 'ro')
y0 = [1.000001, 1, 1]
sol = solve_ivp(fun=butterfly, t_span=(0,40), y0=y0, method='RK45', rtol=1e-8, atol=1e-10)
ax.plot(*sol.y)  # sol.y is (3, n_steps), so *sol.y unpacks to x, y, z arrays
ax.plot(*y0, 'go')
plt.figure()
plt.plot(sol1.t, sol1.y[0])
plt.plot(sol.t, sol.y[0])
plt.show()