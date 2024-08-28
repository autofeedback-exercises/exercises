import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
a,b,c,d=sp.symbols("a,b,c,d")
alpha,beta,gamma=sp.symbols("alpha,beta,gamma")
w,x,y,z=sp.symbols("w,x,y,z")
#Q1
m0=sp.Matrix([[1,0],[0,1]])
m1=sp.Matrix([[1,0],[0,-1]])
m2=sp.Matrix([[0,1],[1,0]])
m3=sp.Matrix([[0,1],[-1,0]])
LHS=sp.Matrix([[a,b],[c,d]])
q1=sp.solve(w*m0+x*m1+y*m2+z*m3-LHS,[w,x,y,z])

#Q2
import sympy as sp
v0=sp.Matrix([1,2,0,0])
v1=sp.Matrix([0,-1,1,1])
v2=sp.Matrix([2,0,1,-1])
expr=a*v0+b*v1+c*v2
eq=sp.Eq(expr,sp.Matrix([0,0,0,0]))
q2=sp.solve(eq,[a,b,c])
sp.pprint(q2)

