# EXERCISE 1
def sample_mean_and_var( sample ) :
    mean, var = 0, 0
    # Your code goes here
    mean, mean2 = sum(sample) / len( sample ), sum(sample*sample) / len(sample)
    var = (len(sample) / (len(sample) - 1)) * (mean2 - mean * mean)
    return mean, var
# You do not need to modify any of the code from here onwards
mysample = np.loadtxt( "https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/Hypothesis/Basics/sample_data.dat" )
mymean, myvar = sample_mean_and_var( mysample )
print( "The mean for the data in mysample is", mymean, "and the variance is", myvar )

# EXERCISE 2
def teststat( sample, mu0 ) : 
    xbar, S2 = sample_mean_and_var( sample )
    # Your code goes here
    return (xbar - mu0) / np.sqrt(S2 / len(sample))
# You do not need to modify any of the code from here onwards
mysample = np.loadtxt( "https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/Hypothesis/Basics/sample_data.dat" )
print("The test statistic for a test to determine whether mu=0 for the data in sample_data.dat is", teststat( mysample, 0) )

# EXERCISE 3
def pval_lower( sample, mu0 ) : 
    t = teststat( sample, mu0 )
    # Your code goes here
    return scipy.stats.t.cdf(t, len(sample)-1)
def pval_not( sample, mu0 ) : 
    t = teststat( sample, mu0 )
    # Your code goes here
    return 2*(1 - scipy.stats.t.cdf(np.abs(t), len(sample)-1))
def pval_higher( sample, mu0 ) : 
    t = teststat( sample, mu0 )
    # Your code goes here
    return 1 - scipy.stats.t.cdf(t, len(sample)-1)
# You do not need to modify any of the code from here onwards
# Notice that I don't really need to load the data here again
# as I read the file sample_data.dat earlier in the notebook
# and set mysample equal to its contents. I am only reading this file here as I have no way of 
# knowing whether you changed the value of the variable mysample
# between the earlier cell where I read it and here.
mysample = np.loadtxt( "https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/Hypothesis/Basics/sample_data.dat" )
print( "The p-value for a test of H_0: mu=0 against H_1 mu<0", pval_lower( mysample, 0 ) )
print( "The p-value for a test of H_0: mu=0 against H_1 mu \ne 0", pval_not( mysample, 0 ) )
print( "The p-value for a test of H_0: mu=0 against H_1 mu>0", pval_higher( mysample, 0 ) )
