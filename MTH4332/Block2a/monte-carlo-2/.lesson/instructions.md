# Monte Carlo Integration

The algorithm that you just implemented computed an approximate version of the integral.  The total area of the xy-plane was divided into a set of squares.  Each of these squares had an area of `1/(npoints*npoints)`.  We determined whether the centre of each of the squares was within the unit circle or not.  If the centre of the square was within the circle then we assumed the whole square was and thus approximated the integral as `nsquares_inside * area_of_square`.

To understand Monte Carlo the key thing to recognise is that we had to loop over all the little squares and determine whether or not their centres were inside the unit circle.  Obviously, the order in which we go through the squares when doing this doesn't matter.  Furthermore, if, instead of running through all the squares, we selected only N of the squares at random and ran the algorithm on only those squares we would, once we divided the number of squares whose centres were found to be inside the circle by N, obtain a number close to the value of the final integral.  The reason for this being that the ratio between the number of squares whose centre is inside the circle to the total number of squares is constant.  

This realisation is the basis of the Monte Carlo algorithm.  In this algorithm:

1. A random grid of points is generated instead of a regular grid of points 
2. A function (in this case whether or not the point is within the unit circle) is evaluated at each of these randomly chosen points
3. The average value of the function is evaluated.

We can understand why calculating averages in this way gives us an approximate value for the integral using arguments similar to the one given above.  Alternatively, because the argument given above is a bit sketchy, we can use ideas from probability theory to write the expectation (this the same as the quantity we have called the ensemble average in this module) of a function, A(x), as:

![](eq1.png)

 where P(x) is a probability density.  The law of large numbers and central limit theorem tell us that:
 
![](eq2.png)

where each X_i in this expression is a random sample from the distribution with probability density P(x).

With that theory explained lets now turn to what I would like you to actually do.  I would like you to write a function called `circle_estimate`.  This function should take in a single argument `N` and should return an estimate for the area of a quarter circle.  The way the function should calculate this estimate is as follows:

1. `N` pairs of uniform random variables between 0 and 1 should be generated.  
2.Each pair of random variables that you generate can be thought of as a set of (x,y) coordinates in the Cartesian plane.  You should thus test whether or not these points are within the unit circle.
3. You should calculate an estimate for the area of the circle by dividing the number of points that were inside the circle by `N`. 

Please note that you can generate a uniform random variable between 0 and 1 by using:

````
U = np.random.uniform(0,1) 
````
