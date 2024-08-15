# Working with lists 2

Write a function to separate the elements in a list into a list of integers into
two lists, one containing the even numbers, and one containing the odd numbers.

Your function should

1. be called `separateEvenOdd`
2. take one input argument: `mylist` the list to be separated
3. return two lists, the first containing only the even elements of `mylist` and
   the second, only the odds.

To do this you can use the modulus operator, `%` which gives the remainder when two
numbers are divided. So `16 % 2` gives `0`, whereas `15 % 2` gives 1` (2 divides
16 but not 15). To return two things in a function, you just separate them by a
comma: 
      
      return evens, odds
