import matplotlib.pyplot as plt
import numpy as np

def gen_vel(temp) :
  #Your code goes here
  
  vel = 0
  return vel
  
  
# To test your code I have written the following code, which will generate multiple
# random initial velocities and illustrate the distribution of values for these 
# velocities
velocities = np.zeros(1000)
for i in range(1000) : velocities[i] = gen_vel(1.0)
plt.hist( velocities )
plt.savefig("velocity_dist.png")
