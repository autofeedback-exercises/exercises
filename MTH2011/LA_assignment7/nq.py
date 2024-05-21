import sympy as sp

M = [sp.Matrix([1, 2, 1]), sp.Matrix([1, 1, 1])]
out = sp.GramSchmidt(M,orthonormal=True)
print(out)
v0=out[0]
v1=out[1]

a,b=sp.symbols("a,b")

res=sp.solve(sp.Matrix([2,2,2])-a*v0-b*v1,[a,b])
print(res)
