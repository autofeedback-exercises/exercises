import matplotlib.pyplot as plt
import queueing_tool as qt
import numpy as np
from mm1 import *

def rate(t) :
    return 0.25

def arr_f(t):
    return qt.poisson_random_measure(t, rate, 0.25 )

def ser_f(t):
    return t + np.random.normal(2.0,2.0)

q_args = {
    1: {
        'num_servers': 1,
        'arrival_f': arr_f,
        'serivce_f': ser_f
    },
}

# Setup a queuing network object
qn = qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )
# Indicate which queues allow arrivals from outside the network by initializing them
qn.initialize( edge_type=1 )
# And now simulate the queue for 100 time units
qn.simulate( t=100 )


# Please do not modify the code from here onwards.  This code allows me to check the functions you have written
st_func = qn.edge2queue[0].service_f
