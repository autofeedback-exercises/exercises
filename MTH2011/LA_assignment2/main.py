import sympy as sp

#Q1
q1_A=sp.Matrix([[1,-2,0],[2,-3,1],[1,1,5]])
q1_L,q1_U,rs= q1_A.LUdecomposition() 
q1_inv = q1_A.inv()
q1_det = q1_A.det()
sp.pprint(q1_A.det())

#Q2
a,b,c=sp.symbols('a,b,c')
q2_B=sp.Matrix([[a-b-c,2*a,2*a],[2*b,b-c-a,2*b],[2*c,2*c,c-a-b]])
q2_det=q2_B.det()

#Q3
q3_C=sp.Matrix([[2,5,7],[1,4,-6],[0,0,6]])
r=sp.symbols('r')
q3_cpoly=q3_C.charpoly(r)

