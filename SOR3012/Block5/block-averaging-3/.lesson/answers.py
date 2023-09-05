import matplotlib.pyplot as plt
import numpy as np

# Read in the energies from a file
eng = np.loadtxt("energies")[:,1]
# Create a list with 10 elements that you will use to hold the variances
eng2 = eng*eng
variances = np.zeros(10)
# Your code goes here
for i in range(10) :
    mean = sum( eng[100*i:100*(i+1)] ) / 100 
    mean2 = sum( eng2[100*i:100*(i+1)] ) / 100 
    variances[i] = (100/99)*( mean2 - mean*mean )

mean = sum( eng ) / len(eng)
mean2 = sum( eng2 ) / len(eng)
total_var = (len(eng)/(len(eng)-1))*( mean2 - mean*mean )
# This will draw a graph of your variances
x = np.linspace( 1, 10, 10 )
plt.plot( x, variances, 'ko')
plt.plot( [1,10], [total_var,total_var], 'r-' )
plt.xlabel("Index")
plt.ylabel("Variance / energy^2")
plt.savefig( "block_variances.png")
