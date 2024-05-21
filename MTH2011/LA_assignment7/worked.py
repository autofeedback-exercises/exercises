import sympy as sp

M = [sp.Matrix([-1, 1, 1, 1]), sp.Matrix([-1, -1, 1, 1]), sp.Matrix([-1, 1, -1, 1])]
out = sp.GramSchmidt(M,orthonormal=True)
print (out)
v0=out[0]
v1=out[1]
v2=out[2]
sp.pprint(out)
#sp.pprint(v0.dot(v1))
#sp.pprint(v0.dot(v2))
#sp.pprint(v2.dot(v1))
#sp.pprint(v0.norm())

a,b,c = sp.symbols("a,b,c")
for ii in range(3):
    res=sp.solve(M[ii]-a*v0-b*v1-c*v2,[a,b,c])
    sp.pprint(res)
    sp.pprint(res[a]*v0+res[b]*v1+res[c]*v2)
    sp.pprint(M[ii])
