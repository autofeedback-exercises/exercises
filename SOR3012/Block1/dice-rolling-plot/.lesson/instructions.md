# Plotting uniform discrete random variables

Now that you know you to generate uniform discrete random variables lets make a scatter plot showing 100 random variables that represent the outcomes that you get when you simulate rolling a six sided dice 100 times.  

To complete this exericse you will need to:

- Write a function called `uniform_discrete` that takes `a` (the lowest possible value of the random variable) and `b` (the highest possible value for the random variable) as arguments.  You should be able to do this using what you learned in the previous exercise. 

- Use this function and what you know about loops, lists and plotting to make a scatter plot showing the outcomes that you get when you roll a six sided dice 100 times.  The x-coordinates of the points in your plot should be 1, 2, 3 etc and the y-coordinates should be the values you get when you roll the (virtual) dice.  Notice that a dice has six sides, each side has a different integer on it and these integers are the numbers from 1 to 6.  The outcome for the dice roll is the number that appears uppermost when you roll the dice.  Furthermore, because the dice is fair the probabilities of finishing with each of the sides uppermost are all the same.  

- The x-axis label of the graph should be "Index" and the y-axis label should be "dice roll".
