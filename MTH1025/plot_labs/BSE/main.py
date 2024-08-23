import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi,np.pi,100)
y= np.sign(x)
plt.plot(x,y,'k',label='Target Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
fighand = plt.gca()

def fourier_coefficient(n):
  if n % 2 == 0:
    return 0
  else:
    return (4/(n*np.pi))

def fourier_expand(N,x):
  F=0*x
  for n in range(1,N+1,2):
    a=fourier_coefficient(n)
    b= np.sin(n*x)
    F = F + a*b
  return F

plt.figure()
x = np.linspace(-np.pi,np.pi,100)
y= np.sign(x)
F10= fourier_expand(10,x)
F20= fourier_expand(20,x)
F50=fourier_expand(50,x)
plt.plot(x,y,'k',label='Target Function')
plt.plot(x,F10,'r',label="F10")
plt.plot(x,F20,'b',label="F20")
plt.plot(x,F50,'g',label="F50")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
fighand = plt.gca()
