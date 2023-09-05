# Changing the number of servers

In the next few exercises you are going to learn a bit more about how queuing tool works.  I have thus deleted the following lines of code from the file called `mm1.py`.

```python
def rate(t) : 
    '''rate of arrivals'''
    return 0.25

def arr_f(t):
    '''arrival times'''
    return qt.poisson_random_measure(t, rate, 0.25 )

def ser_f(t):
    '''time to get order'''
    return t + np.random.exponential(1.0)
    
q_args = {
    1: {
        'num_servers': 1,
        'arrival_f': arr_f,
        'serivce_f': ser_f
    },
}
```

You will need to  copy this code into `main.py` in order to get back to being able to simulate the M/M/1 queue.  Once you have added these commands you can then use the `qt.QueueNetwork`, `qt.initialize`, `qt.start_collecting_data`, `qt.simulate` and `qt.get_agent_data` commands that you learned about in the previous exercise to run simulations of the M/M/1 queue and to collect data on the agents who pass through the queue.  __Try to see if you can reproduce what you did in the previous exercise by copying and pasting the code above and the code that you used to complete the last exercise now__.
You don't need to make the graph you made at the end of that exercise but you do need to at least call `qt.QueueNetwork` to pass the test.

Now that you have got the code working again lets consider what the code in the above snippet does.  Hopefully you recognise that there are three function definitions at the start of this block of code.  The first of these functions, `rate`, just returns a number.  The second function - `arr_f`, meanwhile, takes the arrival time of the nth agent and input and returns the arrival time for the (n+1)th agent.  We are using the `qt.poisson_random_measure` function here, which is part of queuing tool, to simulate a poisson process. However, we could also write that function as:

```python
def arr_f(t):
    return t + np.random.exponential(0.25)
```

which is very similar to the way you learned to simulate a poisson process in the exercises on the M/M/1 queue.

The final function `ser_f` takes the time the agent enters service as input and returns the time they leave service.  As we are simulating an M/M/1 queue we can find the leave service time by just adding an exponential random variable to the enter service time for an agent.

Now that we understand what the functions are doing lets look at the final part of the code above:

```python
q_args = {
    1: {
        'num_servers': 1,
        'arrival_f': arr_f,
        'serivce_f': ser_f
    },
}
```

This code sets the variable called `q_args` equal to a dictionary of dictionaries.  The outer dictionary has only one key:value pair.  The key for this key value pair is 1 and the value is the dictionary that is enclosed in the curly braces that follow the 1: in the command above.  You can see that this inner dictionary has three key value pairs with keys `num_servers`, `arrival_f` and `service_f`.  The values for the `arrival_f` and `service_f` keys are the functions that we wrote in the first part of the code.

Notice how the `q_args` variable is used in the command that sets up the queue:

```python
qn = qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )
```

Notice, furthrmore, that to pass this exercise the queue network object that is created by the `qt.QueueNetwork` command must be called `qn` as this object is used within the tests.

In queuing tool objects called `QueueServers` manage queues. When you use the command above you are thus setting up one `QueueServer` to manage the M/M/1 queue.  The `q_args` variable that you set up above tells queuing tool how this `QueueServer` object should be set up.  What queuing tool needs to know about each `QueueServer` is what you would expect; namely:

1. What governs the times that agents arrive at the queue -- For an M/M/1 queue this is a Poisson process.
2. How long agents spend being served -- For an M/M/1 queue this is an exponential random variable.

To pass this information to the `QueueServer` object we pass the functions called `arr_f` and `ser_f` that we defined earlier by setting the appropriate  values of the appropriate key:value pairs in the `q_args` dictionary.

__Given what you have learend about queuing tool can you write modify the code I have given you for simulating the M/M/1 queue so that it simulates an M/M/3 queue instead.__  In other words, can you increase the number of servers in the queue from one to three.   
