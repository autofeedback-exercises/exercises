import numpy as np
import matplotlib.pyplot as plt
def logistic_map(x, r):
    # your code goes here
    return r * x * (1 - x)
def iterate_map(x0, r, n_iter=100):
    # your code goes 
    x = x0
    xs = [x0]
    for _ in range(n_iter):
        x = logistic_map(x, r)
        xs.append(x)
    return xs
# ── Orbit diagram: show what long-term behaviour looks like ─────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
r_examples = [2.5, 3.2, 3.5, 3.56, 3.8, 3.999]
descriptions = [
    'r=2.5 : stable fixed point',
    'r=3.2 : period-2 cycle',
    'r=3.5 : period-4 cycle',
    'r=3.56: period-8 (near chaos)',
    'r=3.8 : chaos (some order)',
    'r=3.99: fully chaotic'
]
for ax, r_val, desc in zip(axes.flat, r_examples, descriptions):
    xs = iterate_map(x0=0.5, r=r_val, n_iter=100)
    n  = len(xs)
    ax.plot(range(n), xs, 'b-o', ms=3, lw=1.0, alpha=0.8)
    ax.set_title(desc, fontsize=10)
    ax.set_xlabel('Iteration $n$')
    ax.set_ylabel('$x_n$')
    ax.set_ylim(-0.05, 1.05); ax.grid(alpha=0.3)
plt.suptitle("Logistic map orbits for different values of $r$", fontsize=13)
plt.tight_layout()
plt.show()

logistic_a = iterate_map(x0=0.5, r=3.9)
logistic_b = iterate_map(x0=0.5000001, r=3.9)
plt.plot(logistic_a, label='x0=0.5')
plt.plot(logistic_b, label='x0=0.5000001')
plt.xlabel('iterations')
plt.ylabel('logistic map value')
plt.legend()
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()


def double_pendulum(t, state, l1=1.0, l2=1.0, m1=1.0, m2=1.0, g=9.81):
    theta1, omega1, theta2, omega2 = state
    delta = theta2 - theta1
    denom1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta)**2
    denom2 = (l2 / l1) * denom1
    dtheta1_dt = omega1
    dtheta2_dt = omega2
    # Full nonlinear equations of motion
    domega1_dt = (
        m2 * l1 * omega1**2 * np.sin(delta) * np.cos(delta)
        + m2 * g * np.sin(theta2) * np.cos(delta)
        + m2 * l2 * omega2**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta1)
    ) / denom1
    domega2_dt = (
        -m2 * l2 * omega2**2 * np.sin(delta) * np.cos(delta)
        + (m1 + m2) * g * np.sin(theta1) * np.cos(delta)
        - (m1 + m2) * l1 * omega1**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta2)
    ) / denom2
    return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]