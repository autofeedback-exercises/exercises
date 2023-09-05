import numpy as np
import matplotlib.pyplot as plt

def bernoulli(p) : 
  # Your code for generating a Bernoulli random variable goes here
  if np.random.uniform(0,1)< p : return 1
  return 0 
 
# Your code for generating the list of Bernoulli random variables goes here
prob=0.5
indices, random_variables = np.zeros(100), np.zeros(100)
for i in range(100) : 
    indices[i], random_variables[i] = i+1, bernoulli(prob) 
 
# This will plot a graph showing your Bernoulli random variables.
plt.plot( indices, random_variables, ".") 
plt.xlabel("Index")
plt.ylabel("random variable")
plt.savefig("bernoulli_rvs.png")
