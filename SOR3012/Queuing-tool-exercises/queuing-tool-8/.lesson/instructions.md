# Modelling the coffee shop II

I have now shown you most of what I used to produce my report on the coffee shop using queueing tool.  The one final thing that you need to know is how to setup the transition rates so that 30% of agents go to the tea queue and 70% of agents go to the coffee queue.  Setting up these transition probabilities is easy.  You just need to use the commands below as follows:

```python
# Setup the queue network using the variables that you have set earlier in the code
qn = qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )
# Setup the transition matrix -- this is how you ensure the the ratio of agents getting coffee to agents getting tea is 7:3
qn.set_transitions( transitions )
# Tell queuing tool that only edges of type 1 get arrivals from outside the network
qn.initialize(edge_type=1)
# Tell queuing tool that you want to collect data
qn.start_collecting_data()
# Simulate the queue
qn.simulate(t=oneday)
```

The key command here is `qn.set_transitions`.  To understand how this command works, suppose that you have setup your adjacency graph as follows:

```python
adj_graph = { 0: [2], 1: [2,3], 2: [0,1,2,4], 3: [1], 4: [2], }
```

You can then set the variable called `transitions` that is passed to `qn.set_transitions` as follows:

```python
transitions = {
  0: {2: 1.0},
  1: {2: 0.3, 3: 0.7},
  2: {0: 0.20, 1: 0.3, 2: 0.25, 4: 0.25},
  3: {1: 1.0},
  4: {2: 1.0}
}
```

The probablity that an agent transitions from node 1 to node 2 is then 0.3.  Similarly the probablity that an agent transitions from node 2 to node 0 is 0.2.

You now know everything that you need to know in order to simulate the complicated network of queues that I simulated in my report and that is illustrated below:

![](coffee-shop.png)

__Your task is thus to use everything that you have learned by completing these exercises to simulate this system of queues and to draw a graph showing how long each agent waits within the queue.__  
The x-coordinates of the points in your graph should be numerical indices that distinguish each agent.  The x-coordinate of the first point will thus be 1, the x-coordinate of the second point will be 2, the third will be 3 and so on.  The y-coordinates should then tell you how long that particular agent spent in the queue.  In other words, the nth y-coordinate will tell you the amount of time that passed between the arrival of the nth agent into the queuing system and their departure time from it.  Notice that if the leave service time for an agent is earlier than their arrival time that means they are still in the queue or waiting to receive service at the end of the simulation.

The x-axis of your plot should have the label "Agent" and the y-axis of your plot should have the label "Time spent in system".

The test only checks that you have extracted the times each agent spends in the queue from the simulation correctly.  You can thus pass the test by simulating any queue even if it not the queue 
that is given in the description of the problem.  If you want to double check that you have setup the queues for the coffee shop properly you can always ask me to take a look at your code.
