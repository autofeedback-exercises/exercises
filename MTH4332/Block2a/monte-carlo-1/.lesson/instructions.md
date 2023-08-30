# Numerical integration

By now you have hopefully realised that when we calculate a partition function we are calculating the following (definite) high-dimensional integral:

![](eq1.png) 

Similarly, an ensemble average is the following ratio between two high-dimensional integrals:

![](eq2.png)

With this and all the mathematics you have learned during your degree in mind, you can hopefully see that the problem that we are going to encounter.  Calculating integrals analytically is only possible when the functions within them are relatively simple.  It is thus not possible to calculate these integrals exactly when the Hamiltonian is complicated.

In order to make progress and to study physical systems that are more complex (and thus more interesting) than the Ising model (snore!), we are going to have to learn some numerical recipes that we can use to calculate these integrals.  The aim of this next part of the course is thus to explain some numerical tools that we might employ.

In order to get a sense of how these tools work we are going to start with a much simpler problem.  We are going to perform the following integral:

![](eq3.png)

If you plot the integrand here you should see that the curve we are integrating traces out a quarter circle in the xy plane.  We can thus compute this integral without doing any maths -- it is pi/4.  (I would recommend plotting the function if you are unconvinced that the integrand is indeed a circle).

Having established the value of the integral lets now develop an algorithm that can be used to evaluate it numerically.  As you know the integral is equal to the area under the curve.  The numerical algorithm that we are going to employ in this first exercise is thus going to work as follows:

1. We are going to create a uniformly spaced grid of points that have x values between 0 and 1 and y values between 0 and 1.
2. We are then going to determine whether each of the points on the grid is within the unit circle or not.
3. The final value of the integral will be the total number of grid points that were found to be within the circle divided by the total number of points in our grid.

I have started implementing this algorithm in the code cell on the left.  In particular, I have written the code to generate a uniform grid of points.  There are `npoints` x `npoints` in total in this grid and each pair of neighbouring points along x or y are separated by a distance called `gridspacing`.  Within the double loop I have called a function called `incircle` that takes a pair of coordinates, (`x`,`y`), as input.  You must write this function.  The function should:

1. Return one if the input coordinates are within the unit circle.
2. Return zero if the input coordinates are not within the unit circle.  

If you do this you should see that the rest of the code that I have written for you will ensure that the variable called `npoints_in_circle` will be equal to the total number of grid points that sit within the circle.  The final value printed, which is the fraction of grid points that are within the circle, will thus be an approximate value for the integral that we were asked to compute.   

 
