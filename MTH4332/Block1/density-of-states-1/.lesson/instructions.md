# Plotting the energies of all the microstates

Over the course of these next two exercises you are going to learn to compute the density of states.  The density of states is a graph that shows how many microstates have each value of the energy.  Before learning to calculate the density of states properly we will first review what we have learned in previous exercises and draw a graph that shows the energies of all the microstates that the system can adopt.  In this exercise, we are going to use the same Hamiltonian we used in the previous exercise about the partition function:

![](eq2.png)

Each of our individual particles can thus be in one of two states, where they have coordinates of 1 or -1 respectively.  Furthermore, for the sake of simplicity we will set the magnetic field, H, equal to one.

I have written a loop that will run over all the microstates within the code for you.  Within this loop you will need to implement the usual algorithm that converts each of the integers between 0 and 2^(8-1) to a set of microscopic coordinates for a system of 8 spins.  You will then need to calculate the energies of each of these states. 

You will notice that I have created a list called `indices` and a list called `energies` that will ultimately hold each of the numerical indices for the microstates and the energies of each of the microstates respectively.  I have then written code to plot these `indices` against the `energies`.  The final result of your calculation will thus be a graph that contains one point for each microstate that indicates its energy.

You must write a separate function called `hamiltonian` that returns the energy of a set of `N` particles in a magnetic field with strength `H` using the Hamiltonian above.  This function should work for systems with an arbtrary number of spins and an artbitrary field strength.  I know you don't need all that to complete all the exercise but it is good to get in the habit of always writing things in the same way.  You will need the more general version of this function in other exercises. 
