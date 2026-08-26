# EXERCISE 1
def add_element( a, n ) : 
    # Your code goes here
    for e in a :
      if n==e : return a
    a.append(n)
    return a
a, b = [1,2,3,4], {1,2,3,4}
b.add(4)
b.add(5)
add_element(a, 4)
add_element(a, 5)
# You can see from the output that add_element is currently 
# implemented wrongly.  If it were operating correclty the elements 
# in a and b would be identical.
print('This is the set', b, 'this is the list', a )

# EXERCISE 2
def tuple_to_set( A ) : 
    # Your code goes here
    C = []
    for e in A :
      add_element(C,e)
    return set(C)
# And here is some code to test your function
B = (1,2,2,3,4,2)
print("The set of elements in the tuple B is ", tuple_to_set(B) )

# EXERCISE 3
def set_union(A, B) :
    # Your code goes here
    C = []
    for e in A : 
      add_element( C, e )
    for e in B : 
      add_element( C, e )
    return set(C)
# You don't need to modify from here.  This code is just testing your function
A = (1,2,3,4)
B = (3,4,5,6,7)
print( "The union of the two sets is", set_union(A, B) )

# EXERCISE 4
def set_intersection(A, B) : 
    # Your code goes here
    C = []
    for e in A :
      if e in B : add_element(C,e)
    return set(C)
# You don't need to modify from here.  This code is just testing your function
A = (1,2,3,4)
B = (3,4,5,6,7)
print( "The intersection of the two sets is", set_intersection(A, B) )

# EXERCISE 5
def set_difference(A, B) : 
    # Your code goes here
    C = [] 
    for e in A : 
      if e not in B : add_element(C,e)
    return set(C)
# You don't need to modify from here.  This code is just testing your function
A = (1,2,3,4)
B = (3,4,5,6,7)
print( "The difference between set A and set B is", set_difference(A, B) )
print( "The difference between set B and set A is", set_difference(B, A) )

# EXERCISE 6
def check_equality_of_sets(A, B ) :
    # Your code goes here
    for e in A :
      if e not in B : return False
    for e in B :
      if e not in A : return False
    return True
# This tests your function and should not need modifying
a, b = (1,2,3), (3,2,1)
# Both print statements should return true when you have fixed the function
print("True or false: the sets a and b are equal", check_equality_of_sets(A, B ) )
a, b = {1,2,3}, {3,2,1}
print("True or false: these sets a and b are equal", a==b )

# EXERCISE 7
def cartesian_product_2(A, B) :
    # Create an empty set to add elements to using C.add()
    C = set()
    # Your code goes here
    for e in A : 
      for f in B : 
        C.add((e,f))
    return C
def cartesian_product_3(A, B, C ) :
    # Create an empty set to add elements to using D.add()
    D = set()
    # Your code goes here
    for e in A : 
      for f in B :
        for g in C : 
          D.add((e,f,g))    
    return D
# Here is some code to test your functions - notice that we are allowed to 
# calculate the cartesian product of a set with itself.  However, the 
# result of taking the cartesian product of a set with itself is NOT the power set!
A = {1,2,3}
print("A x A is", cartesian_product_2(A,A) )
print("A x A x A is", cartesian_product_3(A,A,A) )

# EXERCISE 8
def vector_addition( v1, v2 ) :
    # Your will need to fix the code from here onwards 
    v3 = v1.copy()
    for i in range(len(v1)) : 
      v3[i] = v1[i] + v2[i]
    return v3
# This code is to test the function you write.
# Nothing from here needs modifying
v1, v2 = [1,2,1], [2,5,7]
# This is what we get when we do the calculation using the function for 
# vector addition.  What I have written is wrong and needs to be fixed by you
print("Adding the vectors v1 and v2 gives", vector_addition( v1, v2 ) )
# You can get the correct result from adding the two vectors together by using NumPy arrays as shown below
v1, v2 = np.array([1,2,1]), np.array([2,5,7])
print("Adding the vectors v1 and v2 gives", v1+v2)
# Once your code is working correctly the two print statements should give the same output

# EXERCISE 9
def vector_times_scalar( v, a ) :
    # Your code goes in here and will change the quantity being returned
    b = v.copy()
    for i in range(len(v)) : 
      b[i] = v[i]*a
    return b
# This is code for testing your function.  It does not need to be modified.
v, a = [1,2,3], 2
# This tests your function.  It is currently returning the wrong quantity as 
# I have impelemented the function incorrectly
print("The product of the vector v and the scalar a is", vector_times_scalar( v, a ) )
# Once you have fixed the function it should give the same result as you get 
# when you do the calculation with NumPy arrays
v = np.array([1,2,3])
print("The product of the vector v and the scalar a is", a*v )

# EXERCISE 10
def array_product( a, b ) : 
    # You need to fix the code in this function - which currently will return an error
    c = a.copy()
    for i in range(len(a)) : c[i] = a[i]*b[i]
    return c
# This code calculates the product of the two NumPy arrays a and b so you can see what this command does
a, b = np.array([1,2,3]), np.array([4,5,6])
print("The product of the two NumPy arrays is", a*b )
# These next two lines will return an error when you first execute this cell.
# Your task is to modify the function array_product so that it outputs a list whose elements
# are the same as the elements in the NumPy array that results from doing a*b
a, b = [1,2,3], [4,5,6]
print("With a modified version of array_product we can get the same result from two lists", array_product(a,b) )

# EXERCISE 11
def complex_number_add( a, b ) :
    # You need to add code here
    return a+b
def complex_number_multiply( a, b ) :
    # You need to add code here 
    return np.array([a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]])
def complex_conjugate( a ) : 
    # You need to add code here
    return np.array([a[0],-a[1]])
def modulus( a ) :
    # You need to add code here    
    return np.sqrt(a[0]*a[0] + a[1]*a[1])
def complex_division( a, b ) : 
    # You need to add code here  
    return complex_number_multiply(a,complex_conjugate(b))/modulus(b)**2
# You do not need to modify from here
# Lets use a NumPy array to store the real and imaginay parts of two complex numbers a and b
a, b = np.array([1,1]), np.array([0,1])
print("a+b is", complex_number_add( a, b ) )
print("a*b is", complex_number_multiply( a, b ) )
print("The complex conjugage of a is", complex_conjugate( a ) )
print("The modulus of a is", modulus( a ) )
print("a/b is", complex_division( a, b ) )

# EXERCISE 12
def solve_basic_poly( n, a ):
    # Your code goes here
    z = sympy.symbols("z")
    eq = sympy.Eq(z**n-a,0)
    sol = sympy.solve(eq,z)
    return sol
# You don't need to modify any of the code from here.
for n in range(1,5) : 
    print("The solution of x^n-1=0 when n=" + str(n) + " is ", solve_basic_poly(n,1) )

# EXERCISE 13 -- CURRENTLY BROKEN
sol = solve_basic_poly( 8, 1 )
realp, imagp = sol.copy(), sol.copy()
for i in range(len(sol)) : 
  realp[i] = sympy.re(sol[i])
  imagp[i] = sympy.im(sol[i])
plt.plot( realp, imagp, 'ro' )
plt.xlabel("real part")
plt.ylabel("imaginary part")
plt.savefig("argand.png")

# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

# EXERCISE 14  -- CURRENTLY BROKEN
def set_of_solutions( N ) :
    solutions = set()
    # Your code goes here
    for n in range(1,N+1) : 
      sol = solve_basic_poly(n,1)
      solutions = solutions.union(set(sol))
    return solutions

# EXERCISE 15
def dictionary_of_solutions( N ) :
    # Create an empty dictionary
    solution_dictionary = {}
    # Your code goes here
    for n in range(1,N+1) : 
      sol = solve_basic_poly(n,1)
      for s in sol : 
        if s in solution_dictionary.keys() : 
          solution_dictionary[s] = solution_dictionary[s] + 1
        else : 
          solution_dictionary[s] = 1
    return solution_dictionary
# You don't need to modify from here onwards.
# This code just uses your function to recreate figure 2 from the example report.
# Get the dictionary of solutions
mysolutions = dictionary_of_solutions(12)
# And plot a bar chart with the number of times each solution appears
f = plt.figure()
f.set_figwidth(10)
xvals = np.linspace(1,len(mysolutions),len(mysolutions))
plt.bar( xvals, mysolutions.values(), width=0.2 )
plt.xticks( xvals, labels=mysolutions.keys(), rotation=90 )
plt.xlabel("Solution")
plt.ylabel("Number of appearances")
plt.show()

# EXERCISE 16
def get_array_of_shared_roots( N ) : 
    mymatrix = np.zeros([N,N])
    # Your code goes here
    for i in range(1,N+1) :
      iroots = set( solve_basic_poly(i,1) )
      for j in range(1,N+1) :
        jroots = set( solve_basic_poly(j,1) )
        mymatrix[i-1,j-1] = len(iroots.intersection(jroots))
    return mymatrix
# You don't need to modify from here onwards.
# This code just uses your function to recreate figure 3 from the example report.
# Get the array that contains the number of shared solutions
shared_solutions = dictionary_of_solutions(12)
# And plot the heat map that shows the |S_n \cap S_m| values
maxn=12
bihisto = get_array_of_shared_roots(maxn)
plt.imshow( bihisto, cmap='hot')
plt.colorbar(label="Number of shared roots")
plt.xticks( np.arange(maxn), labels=range(1,maxn+1))
plt.yticks( np.arange(maxn), labels=range(1,maxn+1))
plt.xlabel("n")
plt.ylabel("m")
plt.show()
