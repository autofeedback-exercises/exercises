# Simulating the number of steps until absorption

Consder the Markov chain that is illustrated in the transition graph shown below:

![](chain.png)

States 2, 3 and 4 in this chain are transient and states 1 and 5 are absorbing.  If the chain is run for long enough the system is guaranteed to end up in state 1 or state 5.  If we told that a phenomenon can be modelled using this Markov chain we might choose to investigate the random variable that measures how many transitions occur before the system ends up in state 1 or 5.  Your task in this exercise is thus to write a function to generate samples of this random variable.

I would recommend that you start by noting that the transition matrix that corresponds to the chain above is:

![](matrix.png)

You can thus set a variable `A` equal to this matrix by using the `np.array` command that was introduced in previous exercises.

To sample the chain you should write a function called `markov_move` that is similar to the function that you wrote for generating the next state in a Markov chain.  Just as in the previous exercises this function takes two arguments.  The first of these arguments, `trans`, should be the 1-step transition matrix for the Markov chain that is being simulated.  The second argument, `start`, is the state that the system is currently within.  Your function should generate the next state in the chain.

The last function you should write should be called `nsteps_to_absorption`.  This function should take two arguments.  The first of these arguments, `trans`, should be the 1-step transition matrix for the Markov chain that is being simulated.  The second argument `start` is then state that the system starts within. Within your `time_to_absorption` function you should use a while loop to call `markov_move` until you have arrived in one of the absorbing states.  Once you arrive in one of he absorbing states the function should return the number of times that `nsteps_to_absorption` has been called.

To complete the exercise you will need to generate 20 samples of the number of steps the chain takes starting from state 2 until it is absorbed in either state 1 or state 5.  These samples should be plotted on the y-axis of a graph.  The x-coordinates of the points should be the integers from 1 to 100.  The x-axis label should be "Index" and the y-axis label shold be "Number of steps till absorption". 
