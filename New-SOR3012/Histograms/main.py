import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
def bernoulli(p) :
  # Your code to generate a bernoulli random variable goes here
  if np.random.uniform(0,1)<p : return 1
  return 0
def repeated_trials(n,p) :
  nsuccess, nfail = 0, 0
  # Your code to generate n bernoulli trials and to count the number of
  # successes and failures goes here.
  for i in range(n) :
    if bernoulli(p) == 1 : nsuccess = nsuccess + 1
    else : nfail = nfail + 1
  return nsuccess, nfail
print( repeated_trials(10,0.2) )
print( repeated_trials(10,0.2) )
print( repeated_trials(10,0.2) )
print( repeated_trials(10,0.2) )

prob, counts = 0.3, np.zeros(2)
# Your code to generate n bernoulli trials and to count the number of
# successes and failures goes here.
for i in range(100) :
  myvar = bernoulli(prob)
  counts[int(myvar)] = counts[int(myvar)] + 1
# Your code to ensure that the sum of the two heights is equal to one
# and that the bar chart plotted is thus an estimate for the probablity
# mass function goes here.
for i in range(2) : counts[i] = counts[i] / 100
# This will draw a bar chart showing the fraction of successes and
# the fraction of failures.
plt.bar( [0,1], counts, width=0.1 )
plt.xlabel('Outcome')
plt.ylabel('Probability')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def binomial(n, p) :
  # Your code to generate a binomial random variable goes here
  b = 0
  for i in range(n) : b = b + bernoulli(p)
  return b
# This variable is the number of random variables we are going to generate
nsamples=200
nparam, prob = 8, 0.3
noutcomes = 9
counts = np.zeros(noutcomes)
for i in range(nsamples) :
  # Your code to generate multiple binomial variables using the function
  # called binomial above and to count how often each outcome comes
  # up goes here.
  myvar = binomial(nparam, prob)
  counts[int(myvar)] = counts[int(myvar)] + 1
sample_space = np.zeros(noutcomes)
for i in range(noutcomes) :
  # Your function to convert the count of the number of times each
  # value for the random variable comes up to the fraction of times
  # each outcome comes up goes here.  You should also set the elements
  # of the list sample_space to the various values in the sample space for this particular random variable so that the plot appears correctly.
  counts[i] = counts[i] / nsamples
  sample_space[i] = i
plt.bar( sample_space, counts, width=0.1 )
plt.xlabel('Random variable value')
plt.ylabel('Fraction of occurances')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

# This sets the x-coordinates for your bar charts
xvals = np.linspace(0,6,7)
# Your code for setting the values in uniform_pmf and binom_pmf goes here
uniform_pmf = np.ones(7)*(1/6)
uniform_pmf[0] = 0
binom_pmf = np.zeros(7)
for i in range(7) :
  binom_pmf[i] = scipy.stats.binom.pmf(i,6,0.5)
# This is the part for plotting the probablity mass functions
# side by side.  Notice that the x-coordinates
# define the position of the centers of the bars.  You
# thus get the center of the two side by side bars to appear at
# the coordinates in xvals by shifting one set of bars left
# by half the width of the bar and the other set of bars
# right by half the width of the bar.
plt.bar( xvals-0.05, uniform_pmf, width=0.1, color='blue' )
plt.bar( xvals+0.05, binom_pmf, width=0.1, color='red' )
plt.xlabel('x')
plt.ylabel('P(X=x)')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def dice_roll() :
  # Insert code so that this function return  the outcome of a roll of a fair six sided dice here.
  return np.floor(np.random.uniform(1,7))
def histo_estimate(n) :
    histo = np.zeros(6)
    # Insert code to compute a histogram if you roll the dice n times here.
    for i in range(n) :
      val = dice_roll()
      histo[int(val-1)] = histo[int(val-1)] + 1
    return histo / n
# This tells us that 50 (nsamples) random variables should be used in the generation of each histogram
# This procedure of generating 50 random variables and calculating the histogram should then
# be repeated 500 (nresamples) times.
nsamples, nresamples = 50, 500
# This loop resamples your histogram
histo_samples = np.zeros([nresamples,6])
for i in range(nresamples) : histo_samples[i] = histo_estimate(nsamples)
# This computes percentiles from your histogram
lower, upper, median = np.zeros(6), np.zeros(6), np.zeros(6)
for i in range(6) :
    # We find the median
    median[i] = np.median( histo_samples[:,i] )
    # Generally we quote the error by saying that the the value is between
    # median - lower and median + upper.  When we compute percentiles we are
    # getting values for median - lower and median + upper so we have to
    # do some sums to get the values of lower and upper that we want.
    lower[i] = median[i] - np.percentile( histo_samples[:,i], 5 )
    upper[i] = np.percentile( histo_samples[:,i], 95 ) - median[i]
plt.bar( [1,2,3,4,5,6], median, width=0.1 )
# This plots the small bar around each of the values.
plt.errorbar( [1,2,3,4,5,6], median, yerr=[lower,upper], fmt='ko' )
plt.xlabel("Outcome")
plt.ylabel("Fraction of occurances")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

nsamples = 500
histo = np.zeros(6)
# Insert code to compute a histogram by generating nsamples binomial random variables with
# n=5 and p=0.5 here.
for i in range(nsamples) :
  myvar = binomial(5,0.5)
  histo[int(myvar)] = histo[int(myvar)] + 1
histo = histo / nsamples
# Don't forget to normalise your histogram.
# Include the code to compute the error bars at the 90% confidence limit here.  The list
# called error should contain the difference between the 95th percentile for the distribution of the
# mean and the mean
error = np.sqrt( histo*(1-histo) / nsamples )*scipy.stats.norm.ppf(0.95)
# This will plot the histogram and the error bars
plt.bar( [0,1,2,3,4,5], histo, width=0.1 )
# This plots the small bar around each of the values.
plt.errorbar( [0,1,2,3,4,5], histo, yerr=error, fmt='ko' )
plt.xlabel('Outcome')
plt.ylabel('Fraction of occurances')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

nsamples, counts = 1000, np.zeros(2)
for i in range(nsamples) :
    if np.random.uniform(0,1)<0.3 : counts[0] = counts[0] + 1
    else : counts[1] = counts[1] + 1
counts = counts / nsamples
errors = np.sqrt( counts / nsamples )
xvals, true_pmf = np.array([0,1]), np.array([0.3,0.7])
plt.errorbar( xvals, counts, yerr=errors, fmt='ko' )
plt.bar( xvals, true_pmf, width=0.1 )
plt.xlabel("Random variable value")
plt.xticks([0,1])
plt.ylabel("Probability of occurance")
plt.show()
