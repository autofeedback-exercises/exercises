from ase.io.trajectory import Trajectory
import matplotlib.pyplot as plt
import numpy as np

ncorr = 50
ftraj = Trajectory('nve-short.traj')
acf, norm = np.zeros(ncorr), np.zeros(ncorr)

n = 0 
for atoms in ftraj :
    vel = atoms.get_velocities().flatten()
    maxn = min( len(ftraj), n + ncorr ) - n
    for i in range(maxn) : 
        veln = ftraj[n + i].get_velocities().flatten()
        acf[i] = acf[i] + np.dot( veln.T, vel ) / (3*len( atoms ))
        norm[i] = norm[i] + 1
    n = n + 1 

acf = acf / norm 

times = 0.005*np.linspace(0, ncorr-1, ncorr)
plt.plot( times, acf, 'k-' )
plt.xlabel("time / arbitrary units")
plt.ylabel("velocity autoccoreation function")
plt.savefig("vacf.png")
