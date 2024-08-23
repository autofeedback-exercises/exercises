import numpy as np
import sympy as sy
x,y,z,t = sy.symbols('x,y,z,t')
#Q1a
Eq1_1 = sy.Eq(2*x+3*y,3)
Eq1_2 = sy.Eq(x-2*y,5)
Eq1_3 = sy.Eq(3*x+2*y,7)
q1 = sy.solve([Eq1_1,Eq1_2,Eq1_3],(x,y))
print(q1)

#Q2
Eq2_1 = sy.Eq(x+2*y-3*z+2*t,2)
Eq2_2 = sy.Eq(2*x+5*y-8*z+6*t,5)
Eq2_3 = sy.Eq(3*x+4*y-5*z+2*t,4)
q2 = sy.solve([Eq2_1,Eq2_2,Eq2_3],(x,y,z,t))
print(q2)

#Q3
Eq3_1 = sy.Eq(x**3*y**2*z**6,1)
Eq3_2 = sy.Eq(x**4*y**5*z**12,2)
Eq3_3 = sy.Eq(x**2*y**2*z**5,3)
q3 = sy.solve([Eq3_1,Eq3_2,Eq3_3],(x,y,z))
sy.pprint(q3)
