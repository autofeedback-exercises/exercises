# Calculating the hitting time

When we use the 1D random walk to model how a gambler plays a game such as roulette in a casino we can use simulation to determine the likelihood the gambler has of loosing all their money.  We can also use simulation to determine how many spins of the wheel the gambler will play before leaving the casino, however.  In this exercise we are thus going to learn how write a program to calculate the number of games the gambler plays before leaving the casino.

Remember the gambler usually only has a finite amount of money to gamble with. If he looses a large number of games he is therefore forced to stop playing. Similarly, the gambler may also have some target for how much money he would like to win. In other words, he should have some figure N pounds, which is more than the amouont of money he entered the casino with. He will stop gambling once he has N pounds in his pocket.

To calculate the number of spins of the wheel the gambler will bet on we thus need to calculate the number of steps the random walk takes before arriving in state 0 or state n.  __Your task in this exericse is to write a function called `nplays` that simulates the changes in the amount of money the gambler has and that returns the number of spins of the wheel that take place.__  Your function should take three arguments:

1. `start` the amount of money the gambler starts with. This should be a positive number
2. `n` the target amount of money that the gambler wants to win. The gambler should stop playing once he has n pounds or when he runs out of money and has zero pounds.
3. `p` the probability of winning each individual game the gambler plays. If the gambler wins a game the amount of money he has increases by one pound. If he looses the amount of money he has decreases by one pound. 

Within the function the random 1D walk should be simulated until the walker arrives in state 0 or in state N.  The number of steps the walker takes should be accumulated and it is this number of steps that should be returned at the end of the function.
