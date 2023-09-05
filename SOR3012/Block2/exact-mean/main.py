import numpy as np

def bernoulli(p) : 
  # Insert code for calculating and returning the expectation of a Bernoulli random variable here

def binomial(n, p) : 
  # Insert code for calculating and returning the expectation of a binomial random variable here 

def geometric(p) : 
  # Insert code for calculating and returning the expectation of a geometric random variable here

def negative_binomial(r, p) : 
  # Insert code for calculating and returning the expectation of a negative binomial random variable here

def uniform_continuous(a, b) : 
  # Insert code for calculating and returning the expectation of a uniform continuous random variable here  

def uniform_discrete(a,b) : 
  # Insert code for calculating and returning the expectation of a uniform discrete random variable here

def exponential(lam) : 
  # Insert code for calculating and returning the expectation of a exponential random variable here

def normal(mu, sigma) : 
  # Insert code for calculating and returning the expectation of a Normal random variable here


print("The expectation for a Bernoulli random variable with p=0.5 is", bernoulli(0.5) )
print("The expectation for a binomial random variable with n=5, p=0.5 is", binomial(5,0.5) )
print("The expectation for a geometric random variable with p=0.5 is", geometric(0.5) )
print("The expectation for a negative binomial random variable with r=3 and p=0.5 is", negative_binomial(3,0.5) )
print("The expectation for a uniform continusou random variable with a=0 and b=1 is", uniform_continuous(0,1) )
print("The expectation for a uniform discrete random variable with a=1 and b=8 is", uniform_discrete(1,8) )
print("The expectation for a exponential random variable with lambda=2 is", exponential(2) )
print("The expectation for a normal random variable with mu=4 and sigma=2 is", normal(4,2) )
