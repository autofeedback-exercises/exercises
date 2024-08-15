import sympy as sp

#Q1
A=sp.Matrix([[1,2,-4],[-1,-1,5],[2,7,-3]])

"""
The LUdecomposition returns three values: L and U (the lower and upper
triangular matrices) and rs: the row swaps. In this example, you can see that
the row swaps array is empty because all of the pivots are non-zero
"""
q1_L,q1_U,rs= A.LUdecomposition() 

print(rs) #There have been no row-swaps: hence this list is empty

"""
To check if the LU decomposition works, we should have L*U == A
"""
print (A)
print (q1_L*q1_U) 

"""
sympy provides methods for computing the inverse and determinant directly:
"""
A_inv= A.inv()
A_det = A.det()

"""
and we can check that the inverse is indeed the inverse with A*A_inv == I:
"""
print(A*A_inv)


#Q2
a,b,c=sp.symbols('a,b,c')
B=sp.Matrix([[a-b-c,2*a,2*a],[2*b,b-c-a,2*b],[2*c,2*c,c-a-b]])
sp.pprint(sp.factor(B.det()))

#Q3
A=sp.Matrix([[2,5,7],[1,4,-6],[0,0,6]])
r=sp.symbols('r')
cp=A.charpoly(r)

sp.pprint(18*A.inv())
