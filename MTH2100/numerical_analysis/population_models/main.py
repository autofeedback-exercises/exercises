import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
r = 0.5   # intrinsic growth rate (per time unit)
K = 200   # carrying capacity
def logistic(t, N):
    # Logistic ODE: dN/dt = rN(1 - N/K)
    return r * N * (1 - N / K)
def log_exact(t, r, K, N):
    return K/(1+((K-N)/N)*np.exp(-r*t))
fig, ax = plt.subplots(1, 1, figsize=(5, 5))
for N0 in [5, 20, 50, 150, 250]:
    sol = solve_ivp(logistic, t_span=(0, 50), y0=[N0],
                method='RK45')#, rtol=1e-8, atol=1e-10) 
    ax.plot(sol.t, sol.y[0], lw=2, label=f'$N_0={N0}$')
ax.set_xlabel('Time $t$')
ax.set_ylabel('Population $N(t)$')
ax.set_title('Logistic growth from various initial conditions', fontsize=12)
ax.legend(fontsize=9)
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

params = {'r':1.0, 'K':100, 'alpha':1.0, 'beta':0.1, 'delta':0.075, 'gamma':1.5}
def lotka_volterra(t, state, params):
    '''
    Lotka-Volterra predator-prey equations.
    state = [x, y]  (x = prey population, y = predator population)
    Returns [dx/dt, dy/dt]
    '''
    x, y = state
    dxdt = params['alpha'] * x - params['beta']  * x * y    # prey: born, eaten by predators
    dydt = params['delta'] * x * y - params['gamma'] * y    # predators: born from prey, die naturally
    return [dxdt, dydt]
def logprey(t, state, params):
    '''
    Lotka-Volterra predator-prey equations.
    state = [x, y]  (x = prey population, y = predator population)
    Returns [dx/dt, dy/dt]
    '''
    x, y = state
    dxdt =  params['r']*x*(1-x/params['K']) - params['beta']  * x * y    # prey: born, eaten by predators
    dydt = params['delta'] * x * y - params['gamma'] * y    # predators: born from prey, die naturally
    return [dxdt, dydt]
y0 = [90, 10]
sol_log = solve_ivp(logprey, t_span=(0, 30), y0=y0, 
                    method='RK45', rtol=1e-8, atol=1e-10, args=(params,))
plt.plot(sol_log.t, sol_log.y[0], label='prey')
plt.plot(sol_log.t, sol_log.y[1], label='predator')
plt.legend()
plt.show()
plt.figure()
sol_lot = solve_ivp(lotka_volterra, t_span=(0, 30), y0=y0, 
                    method='RK45', rtol=1e-8, atol=1e-10, args=(params,))
plt.plot(sol_lot.t, sol_lot.y[0], label='prey')
plt.plot(sol_lot.t, sol_lot.y[1], label='predator')
plt.legend()
plt.show()
plt.figure()
plt.plot(sol_log.y[0], sol_log.y[1], label='logistic')
plt.plot(sol_lot.y[0], sol_lot.y[1], label='lotka')
plt.legend()
plt.show()

params = {'r': 1.0, 'K': 60, 'beta': 0.1, 'delta': 0.075, 'gamma': 1.5, 'H': 0}
def LV_harvest(t, state, params):
    x, y = state
    dxdt = params['r'] * x * (1 - x/params['K']) - params['beta'] * x * y - params['H']
    dydt = params['delta'] * x * y - params['gamma'] * y
    return [dxdt, dydt]
def extinct(t, s, p):
    return min(s[0], s[1])    # stop when either population hits zero
extinct.terminal  = True
y0 = [22.0, 5.5]    # small perturbation from the H=0 equilibrium (20, 6.67)
H_values = [0, 2, 4, 6, 8, 10, 12, 14]
colors = plt.cm.plasma(np.linspace(0.1, 0.9, len(H_values)))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
for H, col in zip(H_values, colors):
    params['H'] = H
    sol = solve_ivp(LV_harvest, (0, 200), y0,
                    method='RK45', rtol=1e-8, atol=1e-10,
                    args=(params,), events=extinct)
    ax1.plot(sol.t, sol.y[0], color=col, lw=1.5, label=f'H={H}')
    ax1.plot(sol.t, sol.y[1], linestyle='--', color=col, lw=1.5)
    ax2.plot(sol.y[0], sol.y[1], color=col, lw=1.2)
ax1.set_xlabel('Time $t$')
ax1.set_ylabel('Prey (-)/predator (--) population $x$')
ax1.legend()
ax2.set_xlabel('Prey $x$')
ax2.set_ylabel('Predator $y$')
ax2.grid(alpha=0.3)
plt.tight_layout()
plt.show()