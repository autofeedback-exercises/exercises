# Confidence limit on mean

As discussed previously any sample mean that we calculate is a random variable.  In order to make our result reproducible we must provide some information about the distribution whenever we quote a sample mean.  In previous exercises we have seen how we can provide this information on the distribution by proposing a confidence limit.  The process that we used to do this in those previous exercises involved:

1. Generating multiple random variables.

2. Using the `np.percentile` function to find a range that 90% of these random samples falls within. 

We could thus make our result by reprocible by noting that if our colleague was sampling the same distribution as us he should obtain a result that falls between the 5th and 95th percentile of our distribution of results with a probablity of 90%.

To complete this exercise I want you to apply this idea for quoting confidence limits on a sample mean.  To complete the exericse you will need to complete the following functions in `main.py`:

1. `sample_mean` should take in a single number `n`.  This function should return a sample mean that is calculated by adding `n` uniform random variables that lie between 0 and 1 together.

2. `limit` should take in two numbers `n` and `m`.  This funciton should generate `m` sample means and store them in a NumPy array.  Each of these sample means should be calculated by adding together `n` uniform random variables that lie between 0 and 1.  This function should then return three numbers.  The first of these numbers `lower` should be the 5th percentile of the distribution of sample means that were generated.   The second of these numbers `median` should be the median of the sample means that was generated.  The final number `upper` should be the 95th percentile of the distribution of sample means.
