def newton_raphson(f, df, x0, tol=1e-10, max_iter=50):
    x = x0
    history = [x]
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:        # close enough to zero: stop
            break
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero — Newton-Raphson fails here.")
        x = x - fx / dfx        # Newton-Raphson update
        history.append(x)
    return x, history
H_val = 10
r = 1
K = 100
def harvest_model(N, H=H_val):
    return r * N * (1 - N / K) - H 
def df_harvest(x):
    """given a function (f), a value (x) and a grid spacing (h), compute the forward difference formula for f'(x)"""
    h = 0.01
    return (harvest_model(x+h) - harvest_model(x))/h
eq_NR1, _ = newton_raphson(harvest_model, df_harvest, x0=1)
eq_NR2, _ = newton_raphson(harvest_model, df_harvest, x0=K)

def double_root(x):
    return (x-2)*(x-2)*(x+1)
def df_double_root(x):
    return (double_root(x+0.001)-double_root(x))/0.001
r1, hist_r1 = newton_raphson(double_root, df_double_root, -1.1)
r2, hist_r2 = newton_raphson(double_root, df_double_root, 10, max_iter=10000)
error_r1 = abs(1 + np.array(hist_r1))
error_r2 = abs(2 - np.array(hist_r2))
plt.semilogy(error_r1, label='error_r1')
plt.semilogy(error_r2, label='error_r2')
plt.xlabel('Number of iterations')
plt.ylabel('Error')
plt.legend()
fighand = plt.gca()
