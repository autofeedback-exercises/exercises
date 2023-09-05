import matplotlib.pyplot as plt
import queueing_tool as qt
import numpy as np
from mm1 import *

# Setup a queuing network object
qn = qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )
# Collect the data
qn.start_collecting_data()
# Indicate which queues allow arrivals from outside the network by initializing them
qn.initialize( edge_type=1 )
# And now simulate the queue for 100 time units
qn.simulate( t=100 )

times, data_out = [], qn.get_agent_data()
for k in data_out.keys() : 
    if data_out[k][0,2]>data_out[k][0,0] : times.append( data_out[k][0,2] - data_out[k][0,0] )

ind = np.linspace( 1, len(times), len(times) )
plt.plot( ind, times, 'ko' )
plt.xlabel("Agent")
plt.ylabel("Time spent in system")
plt.savefig("times.png")
