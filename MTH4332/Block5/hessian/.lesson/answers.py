import matplotlib.pyplot as plt
import numpy as np
from pairwise_calc import *
from ase.optimize import BFGS
from ase.vibrations import Vibrations

def fff(r):
   # Insert your code to calculate the Lennard Jones energy and forces here
   r2 = r*r 
   r6 = r2*r2*r2 
   r12 = r6*r6 
   e = 4*( ( 1/r12 ) - (1/r6) )
   f = -24*( 2/r12 - 1/r6 ) / r2
   return e, f  # First argument should be energy and second should be force

# Insert code from last exercise to create an atoms object and set masses and velocities here.
atoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )

# Attach the method that should be used to calculate energies and forces to the atoms object
atoms.calc = pairwise_calculator( rc=4, pairwise_e=fff )

# Run the optimisation
opt = BFGS(atoms)
opt.run(fmax=0.001)

# And get the vibrations
vib = Vibrations(atoms)
vib.run()
data = vib.get_vibrations()
hessian = data.get_hessian_2d()
eigvals, eigvecs = np.linalg.eig( hessian )

# And get the density of states
frequencies = np.sqrt( eigvals )

minfreq = min(frequencies)
maxfreq = max(frequencies)

nbins = 100
delx = 1.01*(maxfreq- minfreq) / nbins
minx = minfreq - (maxfreq-minfreq)*0.005
histo = np.zeros(nbins)
for e in frequencies :     
    ibin = int( np.floor( (e-minx) / delx) )
    histo[ibin] = histo[ibin] + 1

xvals = np.zeros(nbins) 
for i in range(nbins) : xvals[i] = minx + (i+0.5)*delx

plt.plot( xvals, histo, 'k-')
plt.xlabel("frequencies / arbitrary units")
plt.ylabel("Number of states")
plt.savefig("density-of-states.png")
