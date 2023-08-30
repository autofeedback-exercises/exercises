# Error bars

To start this exercise you will need copy the code that you wrote in the last exericse into the function called `area`.  This function takes a single number `N` as input.  It should then generates `N` pairs of x and y coordinates all of which lie within the unit square.  A test is then performed to determine whether or not each of these points is within the unit circle.  If the point is within the circle then the variable, `nin`, which measures how many of the generated points are within the unit circle, is incremented by one.  At the end of the code the final estimate for the area of the quarter-circle, `nin/N`, is returned.  

It is important to note that because random numbers are used to generate the x and y coordinates you get a different value every time you repeat the experiment.  You can see this clearly if, after you have completed the `circle` function you run the code in the cell on the left.  The code that I have written will output three estimates for the area of the circle and you should see that all three estimates are different.  (the relevant part of the output is the first line - the second line should contain a single 0).  

The fact that you get different numbers every time you run the code because there is this element of randomness in the coordinates is problematic as it makes it difficult for another researcher to reproduce the results that we obtain.  In other words, if Alice says that she got 0.792 how does Bob know his code is doing the same thing as Alice's if he gets 0.795?  They are almost guaranteed to get different results because running the code involves generating random numbers.

The answer to this conundrum is for Alice and Bob to quote error bars on their values.  The reason for doing so is that if the two codes are the same then the distributions that Alice and Bob are sampling random numbers from should be the same.  By quoting error bars we provide information on the distribution and we can thus make a judgement as to whether the two results that Alice and Bob obtained are the same or not.

In this next exercise, therefore, I would like you to write some code to calculate these error bars.  The most conceptually simple way to compute the error bars is resampling.  The way this would work for this particular problem is as follows:

1. You call the `area` function multiple times and thus obtain multiple estimates for the area, which you store in a list. 
2. You sort the list.
3. You find a value, `l`, that 5% of the values in the sorted list are less than and a value, `u`, that 95% of the values in the sorted list are less than.  You can then state that if the experiment is reperformed there is a probability of 90 % that any new estimate of the area will lie between `l` and `u`.

Your task is thus to implement what I have described above.   In particular, you need to complete the function called `myerrors`.  This function takes two arguments `N` and `M` and it should return three numbers, `l`, `m` and `u`.    Within this function, you should generate `M` estimates for the area of the quarter circle each of which should be computed for a random grid of `N` (x,y) coordinates.  All these estimates should then be stored in a list.  From this list, you will need to extract the following quantities:

1. `l` - a value that 5% of your estimates for the area are less than (the 5th percentile of the distribution).
2. `m` - the median of the estimates for the area that you obtained.
3. `u` - a value that 95% of your estimates for the area are less than (the 95th percentile of the distribution).

Please note that if you have a list called `data` and you would like to extract the 5th percentile of the data within the list you can use:

````
pp = np.percentile( data, 5 )
````

Furthermore, if you use this function you don't actually need to sort the list.
