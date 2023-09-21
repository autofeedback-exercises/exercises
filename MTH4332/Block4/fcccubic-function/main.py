from ase.io.trajectory import Trajectory
import numpy as np

def fcc_cubic( atoms ) :
    N = len(atoms)
    order_p = np.zeros(N) 
    distances = atoms.get_all_distances( mic=True )
    vecs = atoms.get_all_distances( mic=True, vector=True ) 
    # Your code goes here


   return order_p
