# Heat capacity for N quantum harmonic oscillators

It is straightforward to adapt what you have learned about calculating the heat capacity for a single quantum harmonic oscillator to calculating the heat capacity 
for the solid system that we studied in the previous but one exercise.  

At the end of that exercise about calculating the frequencies from the Hessian matrix we had
calculated a vector with 3N elements, where N is the number of atoms.  This vector contained the frequencies of the 3N vibrational modes for the system of N atoms.
Each of these modes is independent so we can thus calculate a partition function for each vibrational mode by substituing the frequency of that mode into the expression
for the partition function of a 1D quantum harmonic oscillator.  The partition function for the N particle system is then the product of these 3N 1D partition functions.  

The average energy for a system of 3N harmonic oscillators is thus the sum of the average energies for each of the 3N harmonic oscillator.  The heat capacity is 
similarly a sum of the heat capacities of the 3N 1D oscillators.

Given all the above your task is to plot a graph showing the heat capacity per atom as a function of temperature for the three atom system with the 9 frequencies that are 
given in the NumPy array called `frequencies`.  You will need to use the expression for the heat capacity of a quantum Harmonic oscillator that you used in the previous exercise
to calculate the heat capacities for each of the frequencies separately.  You will then need to sum all those individual heat capacities in order to (almost) arrive at the final result (remember
I want the heat capacity per atom and there are three atoms).

Please ensure that you have a variable called `T` in your final `main.py` code.  This variable should be set equal to a NumPy array that contains the temperatures
at which you evaluated the heat capacity when you generated in the plots.  I use this variable when testing your code.  Please also set the x-axis and y-axis labels 
on your graph equal to "Temperature / natural units" and "Heat capacity per atom / natural units" respectively.
