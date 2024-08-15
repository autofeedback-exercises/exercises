import numpy as np

s3 = np.sqrt(3)
s6 = np.sqrt(6)
basis =  np.array([[-0.5, 0.5, 0.5, 0.5],[-s3/6, -s3/2, s3/6, s3/6],[-s6/6,0,-s6/3, s6/6]])

def project(vecin):
    c=[0,0,0]
    for ii in range(3):
        c[ii] = np.dot(basis[ii],vecin)
    return(c)

def expand(coeff):
    exp = 0
    for ii in range(3):
        exp += basis[ii] * c[ii]
    return(exp)

v=np.array([-1,1,1,1])

c = project(v)
print (expand(c))
print (v)
