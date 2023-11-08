from ase.io.trajectory import Trajectory
import matplotlib.pyplot as plt
import numpy as np

ftraj = Trajectory('nve-short.traj')
natoms = len(ftraj[0].get_velocities())
vtraj = np.zeros([ 3*natoms, len(ftraj) ])
    
k = 0
for atoms in ftraj : 
    vtraj[:,k] = atoms.get_velocities().flatten()
    k = k + 1

fftraj = np.fft.rfft(vtraj,axis=1)
fdos = np.mean(fftraj*np.conjugate(fftraj),axis=0) / len(ftraj)

freqvals = np.fft.rfftfreq( len(ftraj), d=0.005 ) 
plt.plot( freqvals, fdos, 'k-' )
plt.xlabel("frequency / arbitrary units")
plt.ylabel("vibrational density of states")
plt.savefig("vdos.png")
