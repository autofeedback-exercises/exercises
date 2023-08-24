# Generating microstates I

In these exercises we are going to be studying one systems of non-interacting particles.  Each particle in these non-interacting systems can be in a series of distinct states.  For example where might have a system of nuclear spins that can either point up (+1) or down (-1).  Each of the spins can thus occupy one of two possible states +1 or -1.  Consequently, if there are N spins in total then there are 2^N possible microstates.

We can store the coordinates that the N spins take when the system is in one particular micostate in a python list containing N elements.  The elements in this list are equal to +1 if the corresponding spin is in the up state and -1 if the corresponding spin is in the down state. 

I would like you to generate three of the possible micro states for the system of spins described above in the programming exercises.  You will notice that I have created three lists for you `allup`, `alldown` and `alternating`.  I would like you to:

1. Set the elements of the list `allup` so that the list gives the coordinates for microstate in which all the spins are in the spin up state.
2. Set the elements of the list `alldown` so that the list gives the coordinates for microstate in which all the spins are in the spin down state.
3. Set the elements of the list `alternating` so that the list gives the coordinates for the microstate in which all the odd numbered spins are spin up and all the even numbered spins are spin down.

__You will need to use for loops when setting the spin coordinates in each of these microstates.__

Also notice that I can use modulo arithmetic as shown below to determine whether a number is even or odd.

````
if number%2==0 : print("number is even")
else : print("number is odd")
````
