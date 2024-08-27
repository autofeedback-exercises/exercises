import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
# This loads the data that we are going to investigate
x = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Expectation/data.dat')
# Your code will go here
N = len(x)
L=min(x)
U=max(x)

# This loads the data that we are going to investigate
x = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Expectation/data.dat')
# Your code will go here
y = np.linspace( 1, len(x), len(x) ) / len(x)
x.sort()
plt.plot( x, y, 'k-' )
plt.xlabel('x')
plt.ylabel('cumulative distribution')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

plt.figure()
# This loads the data that we are going to investigate
x = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Expectation/data.dat')
# Your code will go here
dmin  = min(x)
lowq  = np.percentile(x, 25)
median= np.percentile(x, 50)
highq = np.percentile(x, 75)
dmax  = max(x)
# This will produce a box plot for you automatically
plt.boxplot(x)
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

plt.figure()
ssum, indices, average = 0, np.zeros(200), np.zeros(200)
for i in range(200) :
  # Add code to setup the numpy arrays called indices and average to generate the desired
  # plot here.
  ssum = ssum + np.random.uniform(0,1)
  indices[i] = i+1
  average[i] = ssum / (i+1)
# This will plot the graph for the data.  You should not need to adjust this.
plt.plot( indices, average, 'ro' )
plt.plot( [0,200], [0.5,0.5], 'k--' )
plt.xlabel('Number of random variables')
plt.ylabel('Sample mean')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def bernoulli(p) :
  # Insert code for calculating and returning the expectation of a Bernoulli random variable here
  return p
def binomial(n, p) :
  # Insert code for calculating and returning the expectation of a binomial random variable here
  return n*p
def geometric(p) :
  # Insert code for calculating and returning the expectation of a geometric random variable here
  return 1/p
def negative_binomial(r, p) :
  # Insert code for calculating and returning the expectation of a negative binomial random variable here
  return r/p
def uniform_continuous(a, b) :
  # Insert code for calculating and returning the expectation of a uniform continuous random variable here
  return (a+b)/2
def uniform_discrete(a,b) :
  # Insert code for calculating and returning the expectation of a uniform discrete random variable here
  return (a+b)/2
def exponential(lam) :
  # Insert code for calculating and returning the expectation of a exponential random variable here
  return 1/lam
def normal(mu, sigma) :
  # Insert code for calculating and returning the expectation of a Normal random variable here
  return mu
print('The expectation for a Bernoulli random variable with p=0.5 is', bernoulli(0.5) )
print('The expectation for a binomial random variable with n=5, p=0.5 is', binomial(5,0.5) )
print('The expectation for a geometric random variable with p=0.5 is', geometric(0.5) )
print('The expectation for a negative binomial random variable with r=3 and p=0.5 is', negative_binomial(3,0.5) )
print('The expectation for a uniform continusou random variable with a=0 and b=1 is', uniform_continuous(0,1) )
print('The expectation for a uniform discrete random variable with a=1 and b=8 is', uniform_discrete(1,8) )
print('The expectation for a exponential random variable with lambda=2 is', exponential(2) )
print('The expectation for a normal random variable with mu=4 and sigma=2 is', normal(4,2) )

def average(n) :
  # Your code to compute the average for a set of n uniform random variables goes here.
  mean = 0
  for i in range(n) : mean = mean + np.random.uniform(0,1)
  return mean/n
# You should not need to adjust the code from here onwards
plt.figure()
xv, yv1, yv2 = np.linspace(1,100,100), np.zeros(100), np.zeros(100)
for i in range(100) :
    yv1[i] = np.random.uniform(0,1)
    yv2[i] = average(100)
plt.plot( xv, yv1, 'ro' )
plt.plot( xv, yv2, 'ko' )
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def sample_mean(n) :
  # Code for generating the sample mean goes here
  mean = 0
  for i in range(n) : mean = mean + np.random.uniform(0,1)
  return mean/n
def sample(m,n) :
  # Code for generating the sample goes here
  mydata = np.zeros(m)
  for i in range(m) : mydata[i] = sample_mean(n)
  return mydata

def limit(m, n) :
    # Your code to calculate the m sample means goes here.
    # Each of these sample means should be computed from
    # n uniform random variables between 0 and 1 goes
    # here.
    mydata = sample(m, n)
    # When completed this function should return
    # lower = the 5th percentile of the distribution for the sample mean
    # median = your estimate for the median
    # upper = the 95th percentile of the distribution for the sample mean
    lower = np.percentile(mydata, 5)
    median = np.percentile(mydata, 50)
    upper = np.percentile(mydata, 95)
    return lower, median, upper
print( limit(10,100) )
print( limit(10,100) )
print( limit(10,100) )
print( limit(10,100) )

def variance(n) :
  # Your function to calculate the variance for a set of n uniform random variables goes here
  S, S2 = 0, 0
  for i in range(n) :
    myvar = np.random.uniform(0,1)
    S = S + myvar
    S2 = S2 + myvar*myvar
  mean = S/n
  return (n/(n-1))*(S2/n-mean*mean)

plt.figure()
myvar = np.random.uniform(0,1)
ssum, ssum2 = myvar, myvar*myvar
indices, S2 = np.zeros(200), np.zeros(200)
for i in range(200) :
  # Add code to setup the numpy arrays called indices and average to generate the desired plot here.
  myvar = np.random.uniform(0,1)
  ssum = ssum + myvar
  ssum2 = ssum2 + myvar*myvar
  indices[i] = i+2
  mean = ssum/(i+2)
  S2[i] = (i+2)/(i+1)*(ssum2/(i+2)-mean*mean)
plt.plot( indices, S2, 'ro' )
plt.xlabel('Number of random variables')
plt.ylabel('Sample variance')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def variance(m,n):
    # Your code to calculate a  sample mean from m
    # uniform random variables between 0 and 1 goes here
    s, s2 = 0, 0
    for i in range(n) :
      vv = sample_mean(m)
      s = s + vv
      s2 = s2 + vv*vv
    s = s / n
    return ( n/(n-1) )*( s2 / n - s*s )
xvals, yvals = np.zeros(50), np.zeros(50)
plt.figure()
for i in range(50) :
  # Your code to set xvals and yvals as described in the panel
  # on the right goes here
  xvals[i] = i+1
  yvals[i] = variance(i+1,10)
plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Number of variables used to calculate mean")
plt.ylabel("Variance")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def mean_with_errors(n) :
  # Your code to calculate the sample mean and sample variance
  # for a set of n uniform random variables between 0 and 1 goes
  # here.
  mean, S2 = 0, 0
  for i in range(n) :
    myvar = np.random.uniform(0,1)
    mean = mean + myvar
    S2 = S2 + myvar*myvar
  mean = mean/n
  var = (n/(n-1))*(S2/n-mean*mean)
  # Your code to calculate lower and upper goes here.
  ppp = scipy.stats.norm.ppf(0.95)
  lower = mean - ppp*np.sqrt(var/n)
  upper = mean + ppp*np.sqrt(var/n)
  # When complete this function should return
  # lower = the 5th percentile of the distribution that was sampled
  # mean = your estimate for the sample mean
  # upper = the 95th percentile of the distribution that was sampled
  # N.B. To compute lower and upper you should be using the central
  # limit theorem as discussed in the explanatory text.
  return lower, mean, upper
print( mean_with_errors(100) )
print( mean_with_errors(100) )
print( mean_with_errors(100) )
print( mean_with_errors(100) )
