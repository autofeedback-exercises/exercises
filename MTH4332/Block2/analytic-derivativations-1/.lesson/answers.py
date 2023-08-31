import sympy as sy

# Lets first define some symbols
# x = position of particle
# p = momentum of particle
# T = temperature 
x, p, T  = sy.Symbol("x"), sy.Symbol("p"), sy.Symbol("T", real=True, positive=True )

# Now calculate the partition function 
# First the hamiltonian
H = x**4 + p*p / 2
# And the boltzmann weight
f = sy.exp( - H / T )

# Now integrate along p
pint = sy.integrate( f, (p,-sy.oo,sy.oo) )
# and integrate the result from the last step along x to get Z
Z = sy.integrate( pint, (x,-sy.oo,sy.oo) )
print("The partition function is", Z )

# Now get the ensemble average for the energy by differentiating log(Z) with respect to beta
E = (T**2)*sy.diff( sy.log(Z), T )
print("The ensemble average of the energy is", E )

# And finally get the heat capcity
# N.B I test that the variable with this value has the correct value when I test your code
CV = sy.diff( E, T )
print("The heat capacity is", CV )
