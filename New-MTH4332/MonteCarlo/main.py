# First exercise
def incircle(x,y) :
  # Your code goes here
  if (x*x+y*y)<1 : return 1
  return 0

npoints = 100
gridspacing = 1.0/npoints
npoints_in_circle = 0
for i in range(npoints) :
  x = (i+0.5)*gridspacing
  for j in range(npoints) :
    y = (j+0.5)*gridspacing
    npoints_in_circle = npoints_in_circle + incircle(x,y)

final_integral = npoints_in_circle / (npoints*npoints)
print( final_integral )

# Second exercise
def circle_estimate(N) : 
  # Your code goes here
  estimate = 0
  for i in range(100) :
      x = np.random.uniform(0,1)
      y = np.random.uniform(0,1)
      estimate = estimate + incircle(x,y)
  return estimate / N

# Three estimates for the area of the circle based on a random grid
# of 1000 points are printed here
print( circle_estimate(1000), circle_estimate(1000), circle_estimate(1000) )

# Third exercise
print( circle_estimate(1000), circle_estimate(1000), circle_estimate(1000) )

def myerrors(N,M) :
  # Your code goes here.
  l, m, u = 0, 0, 0
  samples = np.zeros(M)
  for i in range(M) : samples[i] = circle_estimate(N)
  l = np.percentile( samples, 5 )
  m = np.median( samples )
  u = np.percentile( samples, 95 )
  return l, m, u


print( myerrors(1000, 100) )

# Fourth exercise
def circle_estimate(N) :
  nin = 0
  for i in range(N) :
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    if x*x + y*y < 1 : nin = nin + 1
  mean = nin / N
  var = (N/(N-1))*( mean - mean*mean )
  sig = np.sqrt( var / N )
  return mean + sig*scipy.stats.norm.ppf(0.05), mean, mean + sig*scipy.stats.norm.ppf(0.95)

print( area(1000) )
