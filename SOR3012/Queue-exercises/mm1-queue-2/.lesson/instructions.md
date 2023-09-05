# Stationary distribution for M/M/1 queue

In a previous exercise you learned to simulate an M/M/1 queue and how to extract random variables that measure the total amount of time that each customer spends queuing and being served.  This quantity is not the only variable we might be interested in extracting from a simulation of a queue.  We might for instance be interested in obtaining information about the average length of the queue or the amount of time the queue spends with each of the possible lengths.  In this exercise, we are thus going to learn how to extract information about the amount of time that the queue has each of the different lengths.  If we can extract the distribution then we can work out the average length of the queue.

To complete this exercise you will need to reproduce the code that you wrote in the previous exercise that simulated the queue.  This time, however, you do not need to write this within a function.  Additionally, you need to keep track of the times at which the length of the queue changed by using a list of lists called `events` and the two commands shown below:

```python
# Use this command to record times at which the number of customers in the queuing system increased by one
events.append([time,+1])
# Use this command to record times at which the number of customers in the queuing system decreased by one
events.append([time,-1])
```

Once you have written this code you will need to sort the list called `events` by using the command

```python
events.sort()
```

You should then be able to write a loop like this:

```python
qlen = 1 
for time, change in events : 
    qlen = qlen + change
```

The variable `qlen` here keeps track of the length of the queue.  You can creaate another list of pairs of objects, `qlen`, that records the time at which the queue starts to have a particular length and the length that it starts to have at that time by creating a second list variable in the code above and by adding suitable append commands within the loop.  Once you have this `qlen` variable you can then determine the amount of time the queue spends with each of the different lengths by using the code below:

```python
distribution = np.zeros(maxl) 
for i in range(1,len(qstats)) : 
    # The first of each pair in qstats measures the time at which the queue changes length
    time_with_len = qstats[i][0] - qstats[i-1][0]
    # The second of each pair in qstats measures the number of people in the queue.  This comamnd
    # is thus doing something akin to what we do when we accumulate a histogram.  As time is a random
    # variable, however, we add a random variable when we update the distribution.
    distribution[ qstats[i-1][1] ] = distribution[ qstats[i-1][1] ] + time_with_len
```

Your task is to use the ideas that have been introduced above to draw a histogram that shows the probability that a queue with an arrival rate of `lam` and a service time that has an exponential distribution with parameter `expr` will have lengths of 0, 1, 2, 3, 4, 5, 6, 7 and 8.  You should draw a bar centred on each of these numbers of individuals in the queue.  The heights of the bars should then be equal to the fraction of time that the queue had that particular length.  The x-axis label for your graph should be "number of people in queue" and the y-axis label should be "probability".
