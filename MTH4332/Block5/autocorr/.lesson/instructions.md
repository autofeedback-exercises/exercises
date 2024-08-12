# The velocity autocorrelation function

If we have performed a molecular dynamics simulation of a system of N particles we can investigate whether or not the 
particles are undergoing an oscillatory motion by calculating the velocity autocorrelation function.  This function is 
calculated as follows:

![](eq1.ong)

In this expression v(t) is a vector that contains the velocities of all the particles at time t, T is the number of frames in the trajectory and 
N is the number of atoms.  The expression above is thus the ensemble average of the dot product between the instantaneous velocities at two times separated by a time interval \tau. 

If the mass of the particles is one the velocity autocorrelation should be equal to the k_B T when \tau equals 0 as it is basically 
the sum of the squares of all the velocities divided by the total number of atoms, N.  For particles with mass 1 this is double the 
kinetic energy and we know that average kinetic energy should be equal to 0.5 k_B T by equipartition.  For \tau>0 the autocorrleation 
function should decay towards zero.  There may, however, be some oscillations in the decay and if these are present that is indicative 
of the sorts of oscilations about the lattice sites that you see in a solid.

__Your task in this exercise is to write code to calculate a velocity autocorrelation function.__  You should use the trajectory in the 
file `nve-short.traj` that I have provided for you to calculate this function.  You will see that I have read in this trajectory by using the 
command:

```python
ftraj = Trajectory('nve-short.traj')
``` 

Remember that you can cycle over all the frames in the trajectory by using a loop like this one:

```python
for atoms in ftraj : 
    # Do some analysis on the atoms data in each frame of the trajectory
```

Notice that you can get a 1D vector with 3N elements that contain the velocities of all the atoms for the nth frame in the trajectory by using the command below:

```python
vel = ftraj[n].get_velocities().flatten()
```

You can then calculate the dot product that is being averaged in the equation for the autocorrelation function as follows:

```pythnon
dp = np.dot( veln.T, vel ) / len(vel)
```

In the expression above `veln` is a second vector of velocities that is extracted from the trajectory in the same way that the vector `vel` was obtained.

You should calculate the autocorrelation and store its values in the NumPy array called `acf`.  This array has `ncorr` elements.  The 0th element of this array 
should contain the velocity autocorrelation for \tau=0.  The 1st element should contain the velocity autocorrelation function for frames that are separated by one
timestep.  The 2nd element frames that are separated by two timesteps and so on. To loop and accumulate these averages I would recommend using code like this:

```python
n=0
for atoms in ftraj : 
   maxn = min(len(ftraj), n + ncorr) - n
   for i in range(maxn) :
       # Insert code to update the appropriate element of the autocorrelation function here.
```

If you complete the exercise correctly a graph should be generated that shows your estimate of the autocorrelation function.
