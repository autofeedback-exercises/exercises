# The virbrational density of states

We can get a spectrum showing the vibrational frequencies at a particular temperature by taking the 
Fourier transform of the autocorrelation function that you learned to calculate.  Some researchers have 
then used the vibrational density of states that emerges from such calculations to calculate heat capacities
in the way that is similar that I showed you for calculating the heat capacity from the eigenvalues of the Hessian.

Calculating the autocorrelation function directly in the way that I showed you in the last exercise hopefully helped you to 
understand what this function measures. Researchers typically avoid using this method, however, as it is computationally 
expensive and there is a faster way to get the Fourier Transform of the velocity autocorrelation function that uses the 
convolution theorem.  I am thus going to teach you this method for getting the fourier transform of the autocorrelation 
function in this exercise (if you ever want the autocorrelation function again you can get this by taking the inverse fourier
transform of the function that emerges from the method that I will show you here.)

I have once again written code in `main.py` that reads in the trajectory `nve-short.traj` to a variable called `ftraj`.  Your 
first task in calculating the vibrational density of states is to transfer the velocity data in this trajectory into a 
matrix that I will call `vtraj` in what follows.  The matrix should have 3N rows, where N is the number of atoms, and M columns,
where M is the number of frames in the trajectory.  The ith column in your matrix should contain the instantaneous velocities that all 
N atoms in the system had during at the start of the the ith frame in the trajectory.

Once you have you set all the elements of the matrix you can calculae the spectrum using the following commands:

```python
fftraj = np.fft.rfft(vtraj,axis=1)
fdos = np.mean(fftraj*np.conjugate(fftraj),axis=0) / len(ftraj)
```

There is already code in `main.py` to plot the spectrum for you.  Notice that I have used the function `np.fft.rfftfreq` to generate the 
set of frequencies where I have estimates for the spectrum.
