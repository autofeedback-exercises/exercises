import matplotlib.pyplot as plt
import queueing_tool as qt
import numpy as np
from mm1 import *

def rate(t) :
    tp = t - np.floor(t/600)*600 
    if tp<60 : return 0.5
    if tp<180 : return 1/6 
    if tp<240 : return 0.5 
    if tp<360 : return 1/6
    if tp<420 : return 0.5
    if tp<540 : return 1/6
    return 0.5

def arr_f(t):
    return qt.poisson_random_measure(t, rate, 0.5 )

def ser_f(t):
    return t +  np.random.exponential(2.0) 

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
