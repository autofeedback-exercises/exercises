import queueing_tool as qt

def rate(t) : 
    '''this function just returns a constant as we are simulating an M/M/1 queue'''
    return 0.5

def arr_f(t):
    '''this function generates a poisson process'''
    return qt.poisson_random_measure(t, rate, 0.5 )

def ser_f(t):
    '''this determines how long it takes for someone to get served
    as we are dealing with an M/M/1 queue it just adds an exponential
    random variable'''
    return t + np.random.exponential(1.0)

q_classes = { 1: qt.QueueServer }
q_args = {
    1: {
        'num_servers': 1,
        'arrival_f': arr_f,
        'serivce_f': ser_f
    }
}

adja_list, edge_list = { 0: [1] }, {0: {1: 1}}
g = qt.adjacency2graph(adjacency=adja_list, edge_type=edge_list)
