# Implementing an M/M/1 queue with queuing tool

In every exercise that you have done thus far you have written your own simulation code. Although we have used libraries such as NumPy at Matplotlib for linear algebra and plotting graphs you have written code for doing the simulations yourself. In many areas of mathematics this is not a sensible way to proceed. When the simulations are complicated you really need to use programs that others have written as otherwise, when problems are complex, you will achieve little in the limited time that you have available to tackle any given problem if you start from scratch. In this series of exercises we are thus going to learn to perform simulations of networks of queues using a package called [queuing tool](https://queueing-tool.readthedocs.io/en/latest/).

To start this process we are going to learn how we can reproduce what your codes from last week did using queuing tool.  In this exercise we will focus on analysing the output from queuing tool.  We will then move to understanding how to setup queuing tool simulations yourself over the next few exercises.  For now though, I have written all the code to setup an M/M/1 queue for you in the file called `mm1.py`, which I have imported at the top of the file you will edit - `main.py`.  

Into `main.py` you need to add the commands below:

```python
# Setup a queuing network object
qn = qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )
# Indicate which queues allow arrivals from outside the network by initializing them
qn.initialize( edge_type=1 )
# And now simulate the queue for 100 time units 
qn.simulate( t=100 )
```

These commands tell queuing tool to run a simulation of an M/M/1 queue for 100 time units.  When you run the commands above, however, nothing from the simulations is recorded.  To record data on the queues you need to add the command:

```python
qn.start_collecting_data()
```

before you call the `qn.simulate` method.  If the command above is present you can then collect information on what occured during your simulation using:

```python
data_out = qn.get_agent_data()
```

This `data_out` object that is created by the command above is a type of python object that you haven't seen - a dictionary.  A dictionary is a bit like a list or array.  Unlike lists or arrays, however, the elements in python dictionaries:

1. Are not simply numbers.  You can use dictionaries to hold any kind of obect.
2. Are not referred to using numbers.  Each element in the dictionary consists of key:value pair.  You get the value from the dictionary by referencing it using the key it is paired with.

For now it is sufficient to know that we can iterate through and print out each of the values in a dictionary by using a for loop that looks something like this:

```python 
for k in data_out.keys() : print( data_out[k] )
```

If you run this command on the `data_out` dictionary that was output when `qn.get_agent_data` was called you should find that each value in the dictionary is a two by six matrix.  These two by six matrices provide information on the times that each of the individual people who used the queue (the queuing tool documentation calls the folks who use the queues agents) did various things.  In particular the six numbers in the first row of the array are:

1. The arrival time of the agent.
2. The enter service time for the agent.
3. The leave service time for the agent.
4. The length of the queue when the agent arrived.
5. The total number of agents in the queue.
6. The edge index of the queue.

You should notice that the first number in the second row is equal to the third number in the first row.  This is because the second row provides you with information about the "queue" that the agent enters after they have finished with the first queue.  This second "queue" is used to describe what happens when the agents are released from queue system.  The arrival time for this new "queue" is thus equal to the time at which the agent finishes service.   

That should be enough information to complete the exercise.  __Your task is to plot how long each agent spends in the queue system.__  The x-coordinates of the points in your graph should be numerical indices that distinguish each agent.  The x-coordinate of the first point will thus be 1, the x-coordinate of the second point will be 2, the third will be 3 and so on.  The y-coordinates should then tell you how long that particular agent spent in the queue.  In other words, the nth y-coordinate will tell you the amount of time that passed between the arrival of the nth agent into the queuing system and their departure time from it.  Notice that if the leave service time for an agent is earlier than their arrival time that means they are still in the queue or waiting to receive service at the end of the simulation.

The x-axis of your plot should have the label "Agent" and the y-axis of your plot should have the label "Time spent in system". 

To write this program you will need to use the information about queuing tool that I have provided in the instructions above.  In particular, you will need to call `qn.simulate` as described above.  Lastly, note that __you must call the object that is created by the command `qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )` `qn` as the testing routines use calls to this object to test your code__.


