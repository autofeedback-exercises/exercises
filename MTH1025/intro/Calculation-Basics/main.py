import numpy as np 
q0 = np.sin(np.pi/4)
print(q0) # you can print the value of each variable after it's defined to check the answer if you wish
q1 = (3**4 + 7**5) / (36**2 - 1)
# you have to be careful defining r. 
# r=3**(1/5) is fine
# r=3**1/5 is not- python interprets this as (3**1)/5
# safest option is:
r=3**0.2
q2 = (4/3) * np.pi * r**3
q3 = np.sin(5*np.pi/6)
# note that sin^2 (x) is how we write it mathematically, but really we are doing (sin(x))^2:
q4=np.sin(np.pi/5)**2 + np.cos(np.pi/5)**2
# two ways to do this: 
# q5= np.e**5, or
q5=np.exp(5)
# the default np.log is the natural logarithm, the base 10 log is:
q6=np.log10(10**3)
