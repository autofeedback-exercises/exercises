# Calculating block averages

In this exercise we are going to calculate block averages.  

The input file `energies` that I provided you with contains 1000 values for the energy.  For this exercise I want you to calculate:

* The average over the first 100 energies in this file
* The average over the second 100 energies in this file
* The average over the third 100 energies in the file 
* and so on.  

The final result should thus be a list containing 10 values for the average energy.  I have setup a list with 10 elements that you can use to hold these averages.  The list is called `av_eng`.

Once you have calculated the elements of `av_eng` I would like you to draw a graph of the results.  The x-coordinates for the 10 points in your graph should be the integers from 1 to 10.  The y-coordinates
should be the values of the 10 block averages that you have obtained.  The point with x-coordinate 1 should be the block average from the first 100 energies, the point with x-coordinate 2 should be the block
average from the second 100 energies and so on.  

The x-axis label for your graph should be "Index" and the y-axis label should be "Average energy / natural units"
