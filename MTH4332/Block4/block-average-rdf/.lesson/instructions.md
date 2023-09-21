# Errors on radial distribution functions

When you calculate a radial distribution function from an MD simulation the result you get is an estimate.  Consequently, as with everything else you have learned to calculate from MD simulations,
you need to quote error bars on your estimate.  You can get these errors using the block averaging technique that we have seen elsewhere in this course.  Furthermore, when you work out the lengths 
of the blocks that are needed you use the same techniques as we have used in previous exercises.

__In this exercise you are going to generate a estimate of the radial distribution function along with the erorrs on this estimate of the distribution.__  I would like you to spit the data in the trajectory
that I have provided into __five__ blocks.  You can calculate 5 separate estimates of the radial distribution function from these five blocks of data.  Each of these estimates of the radial distribution function
should be calculated to a maximum distance of `maxd` and should use `nbins` bins.

Once you have calculated and normalised the five rdfs using what you learned in the previous exercise you should set the variable called `average` equal to the average of these five estimates of the rdf.  The variable 
called error should be set equal to the error for a 90% confidence limit on your estimate.  To set this array you will need to calculate the variance for each of the bins from your five estimates of the rdf.

The variabels `average` and `error` that you will set (and that I test) should be NumPy arrays.  I have included code at the end of `main.py` that will plot the radial distribution function and the estimate of the errors for you.
Notice that I use `plt.fill_between` as the rdf is a continuous function.  We thus do what we did in previous exericses and display the part of the xy-plane that this function passes through as a shaded area. 
