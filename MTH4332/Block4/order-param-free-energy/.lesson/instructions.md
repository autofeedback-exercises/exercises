# Calculating the free energy as a function of an order parameter

This exercise should revise ideas that you covered last week when you learned to calculate the free energy as a function of the total magnetisation for the 2D Ising model.
What I would like you to calculate is the free energy as a function of the order parameter.  Furthermore, I would like you to calculate an error on your estimate of this free 
energy using block averaging.

We covered how to esimtate a free energy surface when we looked at the 2D Ising model.  The only difference from what you did last week and what you will do here is that last 
week you only had one magnetisation value from each trajectory frame.  This week you have N=the number of atoms values for the order parameter for each trajectory frame.  You can use 
all of these N values when you accumulate your histograms.

You should devide up the trajectory into five blocks as you did when you caluclated the errors on the radial distribution function.  One histogram should be calculated from each block 
of trajectory data.  These histograms should show the distribution of CV values between `minx` and `mixx` and this interval should be split into `nbins` histogram bins.

Once you have calculated your 5 estimates for the histogram you can calculate the overal average and the error on the estimate of the distribution.  The error on the estimate of the distribution
should be calculated for a 90% confidence limit.

The free energy can be calculated from your estimate of the distribution in the usual way.  The variable `fes` should be set equal to the final estimate of the free energy.  You should use error 
propegation (as you did in the previous exercise) to calculate the error on the free energy.  The variabel `error` should be set equal to this value of the error.  The tests check that these two
variables have been set to the correct values.  At the end of the exercise I have included code that will generate a figure that shows the final estimate for the free energy as a function of the 
order parameter.  The width of the line in this figure is related to the error on your estimate of the this free energy.
