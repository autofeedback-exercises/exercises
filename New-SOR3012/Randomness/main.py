import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
def multiply(a, b) :
  return a*b

def modulo( a ) :
  if a<0 : return a*-1
  return a

xvals = np.linspace(1,100,100)
yvals = np.zeros(100)
for i in range(100) :
  yvals[i] = np.random.uniform(0,1)
plt.plot( xvals, yvals, 'ro' )
plt.xlabel('Index')
plt.ylabel('random variable')
fighand = plt.gca()

def uniform( a, b ) :
  # Your code to generate a random variable that is distributed uniformly
  # between a and b goes here.
  return (b-a)*np.random.uniform(0,1) + a
# You should not need to adjust any of the code from here onwards
xv, yv1, yv2, yv3, yv4 = np.linspace(1,100,100), np.zeros(100), np.zeros(100), np.zeros(100), np.zeros(100)
for i in range(100) :
  yv1[i] = uniform(1,5)
  yv2[i] = uniform(-5,-1)
  yv3[i] = uniform( 2.5, 3.5 )
  yv4[i] = uniform( -3.5, -2.5 )
plt.plot( xv, yv1, 'ro' )
plt.plot( xv, yv2, 'bo' )
plt.plot( xv, yv3, 'go' )
plt.plot( xv, yv4, 'ko' )
plt.xlabel('index')
plt.ylabel('random variable')
fighand = plt.gca()

def bernoulli(p):
   # Your code goes here
  if np.random.uniform(0,1) < p : return 1
  return 0
print( bernoulli(0.5), bernoulli(0.5), bernoulli(0.5)  )

# Your code for generating the list of Bernoulli random variables goes here
prob=0.5
xvals, yvals = np.linspace(1,100,100), np.zeros(100)
for i in range(100) : yvals[i] = bernoulli(prob)
plt.plot( xvals, yvals, 'ro' )
plt.xlabel('Index')
plt.ylabel('random variable')
fighand = plt.gca()

def binomial(n,p) :
  # Your code to generate the binomial random variable goes here.
  binom = 0
  for i in range(n) : binom = binom + bernoulli(p)
  return binom
print( binomial(5,0.5), binomial(5,0.5), binomial(5,0.5) )

# Your code for generating the scatter plot of binomial random variables goes here
num, prob = 5, 0.5
xvals, yvals = np.linspace(1,100,100), np.zeros(100)
for i in range(100) : yvals[i] = binomial( num, prob )
plt.plot( xvals, yvals, 'ro' )
plt.xlabel('Index')
plt.ylabel('random variable')
fighand = plt.gca()

def geometric(p):
  # Your code to generate a geometric random variable goes here
  geom=1
  while bernoulli(p)==0 : geom = geom + 1
  return geom
print( geometric(0.5), geometric(0.5), geometric(0.5), geometric(0.5) )

# Your code for generating the list of geometric random variables goes here
prob = 0.5
xvals, yvals = np.linspace(1,100,100), np.zeros(100)
for i in range(100) : yvals[i] = geometric( prob )
plt.plot( xvals, yvals, 'ro' )
plt.xlabel('Index')
plt.ylabel('random variable')
fighand = plt.gca()

def uniform_discrete(a,b) :
  # Your code goes here
  return np.floor( a + (b-a+1)*np.random.uniform(0,1) )
print( uniform_discrete(1,6), uniform_discrete(1,6), uniform_discrete(1,6), uniform_discrete(1,6) )

# Your code for generating the scatter plot of dice rolls variables goes here
xvals, yvals = np.linspace(1,100,100), np.zeros(100)
for i in range(100) : yvals[i] = uniform_discrete( 1, 6 )
plt.plot( xvals, yvals, 'ro' )
plt.xlabel('Index')
plt.ylabel('dice roll')
fighand = plt.gca()
