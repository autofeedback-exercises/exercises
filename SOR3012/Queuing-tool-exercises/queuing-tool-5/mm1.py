import queueing_tool as qt

q_classes = { 1: qt.QueueServer }
adja_list, edge_list = { 0: [1] }, {0: {1: 1}}
g = qt.adjacency2graph(adjacency=adja_list, edge_type=edge_list)
