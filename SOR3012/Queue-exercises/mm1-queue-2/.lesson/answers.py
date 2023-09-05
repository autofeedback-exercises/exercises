import matplotlib.pyplot as plt
import numpy as np

# These are the parameters of the queue that you should use.  If you change the values
# of these parameters you will fail the test as I have set up the test this way.  In 
# writing your project you can change them but you should always ensure that lam<expr
lam, expr = 0.5, 1.0
# This is the number of people who you should model entering your queue
# Once again you adjust this value in your project.  You must set this value to 100000 to pass
# the test, however
N = 100000

# Use this to hold the times when the queue changes length as is discussed in the text
def exp_rv( lamd ) :
    return -np.log( np.random.uniform(0,1) ) / lamd

# Add code here to simulate the queue and to determine the distribution of lengths
events = []
time, tqt, lst = 0, np.zeros(N), exp_rv( expr )
events.append([lst,-1])
for i in range(1,N) :
    time = time + exp_rv( lam )
    events.append([time,+1])
    if lst<time : est = time  
    else : est = lst 
    lst = est + exp_rv( expr )
    events.append([lst,-1])

events.sort() 
qlen, qstats = 1, []
qstats.append([0,1])
for time, change in events : 
    qlen = qlen + change
    qstats.append( [time, qlen] )

distribution = np.zeros(9) 
for i in range(1,len(qstats)) :
    if qstats[i-1][1]>8 : continue 
    time_with_len = qstats[i][0] - qstats[i-1][0]
    distribution[ qstats[i-1][1] ] = distribution[ qstats[i-1][1] ] + time_with_len

distribution = distribution / lst 

xv = np.linspace(0,8,9)
plt.bar( xv, distribution, width=0.1 )
plt.xlabel("number of people in queue")
plt.ylabel("probability")
plt.savefig("mydist.png")
