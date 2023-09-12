# Generating a microstate

In your next assignment you perform Monte Carlo simulations of a 2D Ising model. This series of Repl exercises are designed to teach you how to run and analyse this type of simluation.
The first step in this process is to find a suitable way of representing the microstate for the 2D Ising model system on a computer.  

The 2D Ising model can be used to describe interacting spins on a two-dimensional square lattice. Each spin can be in one of two states, up (+1) or down (-1) so we can thus represent 
the microstate using a 2D NumPy array with elements that are either 1 or -1.  

We can create a 2D NumPy array full of zeros with 5 rows and 5 columns using the command:

```python
myarray = np.zeros([5,5])
``` 

To assign value to element (i,j) of this array you use the command:

```python
myarray[i,j] = 1
```

and to loop over all the elements of the array you can use a double loop like this:

```python 
for i in range(5) : 
    for j in range(5) : print( myarray[i,j] )
```

(This double loops prints all the elements in the array)

Your task in this exercise is to write a function called `getstate` that takes one argument `N`.  Your function should return an array that contains a randomly selected microstate for a 2D Ising model
composed of (N X N) spins.  You should generate your state so that approximately half of the spins will be in the up (+1) state and half should be in the down (-1) state.  Your function should not return
the same state every time it is called, however.  There should be some randomness in the way the spins are assigned. 
