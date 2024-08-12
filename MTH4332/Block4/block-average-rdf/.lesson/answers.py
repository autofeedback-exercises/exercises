from ase.io.trajectory import Trajectory
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


mytraj = Trajectory('trajectory.traj')
maxd, nbins, nf, N, V = 3, 150, 0, 0, 0
delx, histo = maxd / nbins, np.zeros([5,nbins]) 
bsize = int( np.floor( len(mytraj) ) / 5 )
for atoms in mytraj :
    bnum = int( np.floor( nf / bsize ) )
    nf, N, V = nf + 1, len(atoms), atoms.get_volume()
    distances = atoms.get_all_distances( mic=True )
    for i in range(1,distances.shape[0]) : 
        for j in range(0,i) :
            if  distances[i,j]>maxd : continue 
            xbin = int( np.floor( distances[i,j] / delx ) )
            histo[bnum,xbin] = histo[bnum,xbin] + 2

xbins = np.zeros(nbins)
for i in range(nbins) :
    if i==0 : 
        xbins[i] = 0.5*delx
        vol = (4/3)*np.pi*delx**3*(N/V)
        histo[:,i] = histo[:,i] / ( vol*bsize*N )
    else :  
        xbins[i] = (i+0.5)*delx
        vol = (4/3)*np.pi*((delx*(i))**3 - (delx*(i-1))**3)*(N/V)
        histo[:,i] = histo[:,i] / ( vol*bsize*N )

average, average2 = np.zeros(nbins), np.zeros(nbins)
for i in range(5) : 
    average = average + histo[i,:]
    average2 = average2 + histo[i,:]*histo[i,:]

average = average / 5
error = np.sqrt( (1/4)*( average2 / 5 - average*average ) )*scipy.stats.norm.ppf(0.95)

plt.fill_between( xbins, average - error, average + error )
plt.xlabel("r / sigma")
plt.ylabel("g(r)")
plt.savefig("rdf.png")
