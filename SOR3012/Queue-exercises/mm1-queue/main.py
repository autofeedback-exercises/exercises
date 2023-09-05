import matplotlib.pyplot as plt
import numpy as np

def exponential_random_variable(lam):
  # Your code to generate an exponential random variable goes here

def my_queue( N, lam, expr ) :
  # Your code to generate the times that the N customers spend queuing and being served goes here
  my_queue_times = np.zeros(N)



# This is the code to generate the graph showing the values of 100 of your
# random variables.  You should not need to edit anything beyond here
indices, times = np.linspace( 1, 100, 100 ), my_queue( 100, 0.5, 1 )   
plt.plot( indices, times, 'ko' )
plt.xlabel("index")
plt.ylabel("time spent queueing and being served")
plt.savefig("queue.png")
