import sympy as sy
import numpy as np
mat = [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0],
       [0, 0, 0, 4]]
A_sym = sy.Matrix(mat)
A_num = np.array(mat)
epairs_sym = A_sym.eigenvects()
evals_num, evects_num = np.linalg.eig(A_num)

sy.pprint(epairs_sym)
