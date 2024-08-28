import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
#Q1 
q1_M = sy.Matrix([[5,3,4,1], [1,2,2,6],[4,0,1,4]])
q1_rref=q1_M.rref()
q1_rank=q1_M.rank()
q2_A = sy.Matrix([[0,0,1,1,0],[1,2,0,0,3],[1,1,0,1,0],[0,1,-1,1,0]])
q2_rref=q2_A.rref()
q2_rank=q2_A.rank()
print(q2_rank)

#Q2
x,y,z,alpha = sy.symbols("x,y,z,alpha")
q3_E0=x+y+z-2
q3_E1=x+alpha*y+2*alpha*z-1
q3_E2=x+y+alpha*alpha*z-alpha-3
print(q3_E0)
print(q3_E1)
print(q3_E2)

#Q3
q3_1 =sy.solve([q3_E0,q3_E1.subs(alpha,1),q3_E2.subs(alpha,1)],[x,y,z])
q3_m1 =sy.solve([q3_E0,q3_E1.subs(alpha,-1),q3_E2.subs(alpha,-1)],[x,y,z])
q3_2 =sy.solve([q3_E0,q3_E1.subs(alpha,2),q3_E2.subs(alpha,2)],[x,y,z])
print(q3_m1)
print(q3_2)
