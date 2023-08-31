# Heat capacity from fluctuations

Now you know how to compute a heat capacity you can run a simulation and produce a result that can be compared with the results from an experiment or with the result that we would expect given the body of theory that we have learned during this course on statistical mechanics.  

In these final two exercises, we are going to consider an alternative method that we can use to calculate the heat capacity from a constant temperature MD simulation.  For this method, we will use the fact that the heat capacity is related to the average fluctuations in the internal energy by this formula:

![](eq1.png)

We learned about this formula when we studied the canonical ensemble.  Furthermore, at some point during your degree (or before), you will have learned that the variance can be computed using either the part of the expression shown in angle brackets above or by computing:

![](eq2.png)

Given that we are given the average for the square of the energy, it is clear that you are going to use this second formula in your codes.

With all that in mind, your task here is to compute the heat capacity using the formulas above.  In doing so, you should use the data from the file `md_results.txt` .  As always you have been given the following data:

* `temperatures` - the temperatures at which the simulations were run
* `energies` - the ensemble average for the total energies at each temperature
* `errror_energies` - the error bars for each of the average energies computed at each temperature.
* `energies2` - the ensemble average for the square of the total energy at each temperature.
* `error_energies2` - the error bars for each of the average squared energies computed at each temperature. 

You should be able to use this data and the formulas above to compute the heat capacity at ten different temperatures.  The values of the temperature at which you have calculated the heat capacity should be stored in the list called `cv_temperatures`, and the final values for the heat capacity should be stored in the list called `cv`.   

If you complete the exercise correctly, a graph showing the value of the heat capacity as a function of temperature will be generated.    
