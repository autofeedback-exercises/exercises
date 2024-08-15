import sympy as sy

def project(vecin):
    a,b,c = sy.symbols("a,b,c")
    basis= [sy.Matrix([ [-1/2], [ 1/2], [ 1/2], [ 1/2]]), sy.Matrix([ [-sy.sqrt(3)/6], [-sy.sqrt(3)/2], [ sy.sqrt(3)/6], [ sy.sqrt(3)/6]]), sy.Matrix([ [-sy.sqrt(6)/6], [         0], [-sy.sqrt(6)/3], [ sy.sqrt(6)/6]])]
    res = res=sy.solve(vecin-a*basis[0]-b*basis[1]-c*basis[2],[a,b,c])
    return res

def expand(coeff):
    a,b,c = sy.symbols("a,b,c")
    basis= [sy.Matrix([ [-1/2], [ 1/2], [ 1/2], [ 1/2]]), sy.Matrix([ [-sy.sqrt(3)/6], [-sy.sqrt(3)/2], [ sy.sqrt(3)/6], [ sy.sqrt(3)/6]]), sy.Matrix([ [-sy.sqrt(6)/6], [         0], [-sy.sqrt(6)/3], [ sy.sqrt(6)/6]])]
    vout = basis[0] * coeff[a] + basis[1] * coeff[b] + basis[2] * coeff[c]
    return vout

v = sy.Matrix([-1,1,1,1])
c = project(v)
v2 = expand(c)
sy.pprint(v)
sy.pprint(v2)
