import numpy as np


def sample_mean(n) :
  # Code for generating the sample mean goes here
  mm = 0
  for i in range(n) : mm = mm + np.random.uniform(0,1)
  return mm / n


def sample(m,n) :
  # Code for generating the sample goes here
  sample = np.zeros(m)
  for i in range(m) : sample[i] = sample_mean(n)
  return sample
