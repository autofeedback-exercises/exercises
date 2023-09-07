import matplotlib.pyplot as plt
import queueing_tool as qt
import numpy as np

# Create the adjacency list of the graph for this network
adj_list = {0: [1], 1: [2, 3]}
# Now say what type of queue is on each edge
edge_list = {0: {1: 1}, 1: {2: 2, 3: 2}}
# And create the graph object
g = qt.adjacency2graph(adjacency=adj_list, edge_type=edge_list)

# And now create the queue server objects
def rate(t) : 
    return 0.25

def arr_f(t):
    return qt.poisson_random_measure(t, rate, 0.25 )

def ser_order(t):
    return t + np.random.exponential(1.0)
    
def ser_tea(t):
    return t + np.random.exponential(2.0)

def ser_coffee(t):
    return t + np.random.exponential(4.0)

q_classes = { 1: qt.QueueServer, 2: qt.QueueServer, 3: qt.QueueServer }
q_args = {
    1: {
        'num_servers': 1,
        'arrival_f': arr_f,
        'serivce_f': ser_order
    },
    2: {
        'num_servers': 1,
        'serivce_f': ser_tea
    },
    3: {
        'num_servers': 1,
        'serivce_f': ser_coffee
    },
}


# Setup a queuing network object
qn = qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )
# Collect the data
qn.start_collecting_data()
# Indicate which queues allow arrivals from outside the network by initializing them
qn.initialize( edge_type=1 )
# And now simulate the queue for 100 time units
qn.simulate( t=100 )
