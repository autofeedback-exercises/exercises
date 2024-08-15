import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

a,b,c,d=sp.symbols("a,b,c,d")
alpha,beta,gamma=sp.symbols("alpha,beta,gamma")
w,x,y,z=sp.symbols("w,x,y,z")


#Q1 worked
f2=1
f1=1+x
f0=(1+x)**2

px=a*x**2+b*x+c

Eq1 =  sp.Eq(alpha*f0+beta*f1+gamma*f2,px)
q1=sp.solve(Eq1,[alpha,beta,gamma])
sp.pprint(q1)
