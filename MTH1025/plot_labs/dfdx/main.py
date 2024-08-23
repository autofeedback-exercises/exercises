import numpy as np
import matplotlib.pyplot as plt
delx=0.1
x=np.arange(-10,10.1,0.1)
f=np.exp(-x**2)
exact_derivative=f*(-2*x)
plt.plot(x,exact_derivative,'k-',label='Exact Derivative')
plt.legend()
plt.xlabel('x')
plt.ylabel('df/dx')
fighand = plt.gca()

# your code goes here
df99=(f[100]-f[99])/delx
err99=np.absolute(exact_derivative[99]-df99)

def numerical_derivative(f,delx):
  N=len(f)
  dfdx=np.zeros(N)
  for ii in range(N-1):
    dfdx[ii]=(f[ii+1]-f[ii])/delx
    dfdx[-1]=dfdx[-2]
  return dfdx

plt.figure()
delx=0.1
x=np.arange(-10,10.1,0.1)
f=np.exp(-x**2)
exact_derivative=f*(-2*x)
plt.plot(x,exact_derivative,'k-',label='Exact Derivative')
plt.legend()
plt.xlabel('x')
plt.ylabel('df/dx')
dfdx=numerical_derivative(f,delx)
plt.plot(x,dfdx,'r',label='Numerical Derivative, delx=0.1')
x2=np.arange(-10,10.5,0.5)
f2=np.exp(-x2**2)
dfdx=numerical_derivative(f2,0.5)
plt.plot(x2,dfdx,'b',label='Numerical Derivative, delx=0.5')
plt.legend()
fighand = plt.gca()
