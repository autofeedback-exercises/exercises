def double(x):
# function to multiply a value by 2
    d=2*x
    return(d)
def triple(x):
# function to multiply a value by 3
    y=3*x
    return (y)
def fivetimes(x):
# function to multiply a value by 5. Makes use of double and triple functions above
    z= double(x)+triple(x)
    return (z)
# TESTS
print (double(4))
