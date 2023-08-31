# Heat capacities by finite differences

Now that you can compute these ensemble averages you know how to run all the molecular dynamics simulations that you will need to compute the heat capacities for your report.  In these final four exercises, I am thus going to give you the ensemble averages and error bars that I computed by running constant temperature MD simulations at a number of different temperatures.  You are then going to use this data to compute the heat capacity as a function of temperature.  We are going to use two different methods to compute the heat capacity.  The first of these is based on the definition of the heat capacity that you learned from classical thermodynamics.  In that part of this course, you learned that the heat capacity was the partial derivative of the internal energy with respect to temperature at constant volume.  Given this it makes sense to calculate the heat capacity at a temperature midway between T_1 and T_2 using:

![](eq.png)

In other words, we run simulations at two temperatures T_2 and T_1 and compute the ensemble average for the total energy in these two simulations.  We then insert these two approximate ensemble averages into the finite-difference formula above as <E>(T_2) and <E>(T_1) to get an approximate value for the derivative at the midpoint between the two temperatures.

The exercise in the code cell on the left will allow you to test whether or not you have understood this idea.  Ensemble averages and errors from the MD simulations that I have run from you have been imported from the input file called `md_results.txt`.  Five lists have been created from this data that are named as follows:

1. `temperatures` - the temperatures at which the simulations were run
2. `energies` - the ensemble average for the total energies at each temperature
3. `errror_energies` - the error bars for each of the average energies computed at each temperature.
4. `energies2` - the ensemble average for the square of the total energy at each temperature.
5. `error_energies2` - the error bars for each of the average squared energies computed at each temperature.

Your task is to use these 10 data points to calculate the heat capacity at nine different temperatures using the formula above.  The values of the temperature at which you have computed the heat capacity should be stored in the list called `cv_temperatures` and the final values for the heat capacity should be stored in the list called `cv`.  If you complete the exercise correctly a graph showing the value of the heat capacity as a function of temperature will be generated. 
