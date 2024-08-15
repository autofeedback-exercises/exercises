import numpy as np 

# remember that arange goes up to but not including the upper limit 
# hence to make sure the last element of x is '3' we make the upper limit > 3
x=np.arange(1,4)
print (x) # make sure your input array is defined properly in each case

y=2*x

print(y[:2]) # you can a few elements of each array after it's defined to check the answer if you wish

x=np.arange(0,6.1,0.5) # produces from 0 up to (but not including) 6.1 in steps of 0.5

print (x[-1]) # check that the last element of x is in fact 6

y1 = 4*x*x + 6*x + 3

y2 = -x*x -1 

u = np.linspace(-np.pi,np.pi,1000) 

x1= u*np.cos(u)

x2 = u/(u+3)

n=np.arange(100) # this produces the values from 0 up to 99 in the default step size of 1

a=n*(n+1)

print (a[:3], ) # check the first few values are (0*1) (1*2) (2*3)
