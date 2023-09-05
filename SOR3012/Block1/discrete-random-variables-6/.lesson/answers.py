import matplotlib.pyplot as plt
import numpy as np

# You may wish to write some code here

def binomial(n, p) :
  # Your code for generating a binomial random variable goes here
  num = 0
  for i in range(n) : 
      if np.random.uniform(0,1)<p : num = num + 1 
  return num 
 
# Your code for generating the scatter plot of binomial random variables goes here
num, prob = 5, 0.5
xvals, yvals = np.zeros(100), np.zeros(100)
for i in range(100) :
    xvals[i] = i+1
    yvals[i] = binomial(num, prob )

plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Index")
plt.ylabel("random variable")
plt.savefig("binomial.png")
