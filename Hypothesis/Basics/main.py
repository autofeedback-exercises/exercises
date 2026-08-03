import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

# EXERCISE 1
def sample_mean( sample ) :
    # Your code for computing the sample mean from the data in sample 
    # goes here
    return sum( sample ) / len( sample )
# You do not need to modify any of the code from here onwards
mysample = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/Hypothesis/Basics/sample_data.dat" )
print( sample_mean( mysample ) )

# EXERCISE 2
# This generates the 16 standard normal random variabels
samples = np.random.uniform( 0, 1, size=16 )
# Now calculate the sample mean 
xbar = sum(samples) / len(samples)
# Here are the x-values at which I want you to evaluate the probability density
# function for the variable above
xvals = np.linspace( -1, 1, 100 )
# You need to adapt the line below so that the yvals values are the values of the 
# probability density function for the distribution that mu is sampled from.  
# To answer this question you need to remember what the central limit theorem
# tells us about the distribution of a sample mean that is calculated by 
# summing multiple random variables together.
yvals = scipy.stats.norm.pdf( xvals, 0, 1/np.sqrt(200) )
# This will generate the graph for you
plt.plot( xvals, yvals, 'k-')
plt.xlabel("Sample mean")
plt.ylabel("Probability density")
plt.savefig("clt_distribution.png")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

# EXERCISE 3
def teststat( sample, mu, sig2 ) : 
    xbar = sample_mean( sample )
    # Your code goes here.
    return (xbar - mu) / np.sqrt( sig2 / len(sample) )
# You do not need to modify any of the code from here onwards
# Notice that I don't really need to load the data here again
# as I read the file sample_data.dat earlier in the notebook
# and set mysample equal to its contents. I am only reading this file here as I have no way of 
# knowing whether you changed the value of the variable mysample
# between the earlier cell where I read it and here.
mysample = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/Hypothesis/Basics/sample_data.dat" )
print( teststat( mysample, 0, 1 ) )

# EXERCISE 4
def critregH1a( siglev ) : 
    # You need to add code here
    return scipy.stats.norm.ppf(siglev)
def critregH1b( siglev ) :
    # You need to add code here
    return scipy.stats.norm.ppf(siglev/2), scipy.stats.norm.ppf(1-siglev/2)
def critregH1c( siglev ) : 
    # You need to add code here
    return scipy.stats.norm.ppf(1-siglev)

# EXERCISE 5
def pval_lower( sample, mu0, sig2 ) : 
    t = teststat( sample, mu0, sig2 )
    # Your code goes here
    return scipy.stats.norm.cdf(t)
def pval_not( sample, mu0, sig2 ) : 
    t = teststat( sample, mu0, sig2 )
    # Your code goes here
    return 2*(1-scipy.stats.norm.cdf(np.fabs(t)))
def pval_higher( sample, mu0, sig2 ) : 
    t = teststat( sample, mu0, sig2 )
    # Your code goes here
    return 1-scipy.stats.norm.cdf(t)
# You do not need to modify any of the code from here onwards
# Notice that I don't really need to load the data here again
# as I read the file sample_data.dat earlier in the notebook
# and set mysample equal to its contents. I am only reading this file here as I have no way of 
# knowing whether you changed the value of the variable mysample
# between the earlier cell where I read it and here.
mysample = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/Hypothesis/Basics/sample_data.dat" )
print( "The p-value for a test of H_0: mu=0 against H_1 mu<0", pval_lower( mysample, 0, 1) )
print( "The p-value for a test of H_0: mu=0 against H_1 mu \ne 0", pval_not( mysample, 0, 1) )
print( "The p-value for a test of H_0: mu=0 against H_1 mu>0", pval_higher( mysample, 0, 1) )

# EXERCISE 6

