import numpy as np

A = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]]) 

A2 = np.linalg.matrix_power( A, 2 )
A10 = np.linalg.matrix_power( A2, 5 )
A50 = np.linalg.matrix_power( A10, 5 ) 
A100 = np.linalg.matrix_power( A50,2 )

