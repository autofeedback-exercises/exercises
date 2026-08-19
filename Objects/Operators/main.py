# ANSWER TO EXERCISE 1
def dot_product_1(a, b) :
    # Your code goes here
    dp = 0 
    for i in range(a.shape[0]) : dp = dp + a[i]*b[i]
    return dp

# ANSWER TO EXERCISE 2
def dot_product_2(a, b) :
    # Your code goes here
    return sum(a*b)

# ANSWER TO EXERCISE 3
def dot_product_3(a, b) :
    # Your code goes here
    return np.dot(a,b)

# ANSWER TO EXERCISE 4
def outer_product_1( a, b ) : 
    # Your code goes in here
    c = np.zeros([a.shape[0],b.shape[0]])
    for i in range(a.shape[0]) : 
      for j in range(b.shape[0]) : c[i,j]=a[i]*b[j]
    return c

# ANSWER TO EXERCISE 5
def distance_matrix(X) : 
    # Your code goes in here
    return np.abs( np.subtract.outer( X, X ) )

# ANSWER TO EXERCISE 6
def matvec_mult( A, b ) : 
    # Your code goes here
    c = np.zeros(A.shape[0])
    for i in range(A.shape[0]) : 
      for j in range(A.shape[1]) : c[i] = c[i] + A[i,j]*b[j]
    return c

# ANSWER TO EXERCISE 7
def cumdist_estimate( X, r ) : 
    # Calculate the matrix of distances between the random points using the function that 
    # was written in the last but one exercise
    D = distance_matrix(X)
    # Your code goes here
    C = np.where( D<=r, 1, 0)
    v = np.matmul( C, np.ones(C.shape[1]) ) / C.shape[1]
    return np.mean(v)

# ANSWER TO EXERCISE 8
def matrix_multiplication( A, B ) : 
    # Your code goes here
    c = np.zeros([A.shape[0],B.shape[1]])
    for i in range(A.shape[0]) : 
      for j in range(B.shape[1]) : 
        for k in range(A.shape[1]) : c[i,j] = c[i,j] + A[i,k]*B[k,j]
    return c

# ANSWER TO EXERCISE 9
def all_dot_products( X ) :
    # Your code goes here
    return np.matmul( X.T, X )

# ANSWER TO EXERCISE 10
def all_angles( X ) : 
    # Your code goes here
    m = np.sqrt( np.matmul( X.T*X.T, np.ones(X.shape[0]) ) )
    angmat = np.acos( np.matmul( X.T, X ) / np.outer( m, m ) )
    return angmat[np.triu_indices_from(angmat, 1) ]

# ANSWER TO EXERCISE 11
def distance_matrix_nd( X ) : 
    # Your code goes here
    mag = np.matmul( X.T*X.T, np.ones( X.shape[0]) )
    return np.add.outer(mag,mag) - 2*np.matmul( X.T, X )

# ANSWER TO EXERCISE 12
def bounded_power_set_2( S ) : 
    # You need to write a suitable double loop here
    power_set = set()
    for i in range(1,len(S)) : 
      for j in range(i) : power_set.add( (S[j],S[i]) )
    return power_set
def bounded_power_set_3( S ) : 
    # You need to write a suitable triple loop here
    power_set = set()
    for i in range(2,len(S)) : 
      for j in range(1,i) : 
        for k in range(j) : power_set.add( (S[k],S[j],S[i]) )
    return power_set
def bounded_power_set_4( S ) : 
    # You need to write a suitable quadruple loop here
    power_set = set() 
    for i in range(3,len(S)) : 
      for j in range(2,i) : 
        for k in range(1,j) : 
          for l in range(k) : power_set.add( (S[l],S[k],S[j],S[i]) )
    return power_set

# ANSWER TO EXERCISE 13
def get_all_sets_of_three_vectors( X ) :
    # Your code goes here
    corners = np.array( list( itertools.combinations( X.T, 3 ) ) )
    return corners

# ANSWER TO EXERCISE 14
def get_all_areas(X) : 
    # Get the corners of all the random triangles we can make from X
    triangles = get_all_sets_of_three_vectors( X )
    # Your code goes here
    edges_f = np.array( [triangles[:,1,:] - triangles[:,0,:], triangles[:,2,:] - triangles[:,0,:]] )
    edges = np.transpose( edges_f, axes=(1,0,2) )
    return 0.5*np.abs( np.linalg.det(edges) )
