import ase
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from ase.build import bulk,make_supercell
from ase.visualize import view
from ase.io import write
from ase.neighborlist import NeighborList
from ase.calculators.calculator import Calculator, all_changes
from ase.stress import full_3x3_to_voigt_6_stress
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet 
from ase.io.trajectory import Trajectory 

class pairwise_calculator(Calculator) :
  """Implementation of a very basic Lennard Jones Calculator"""

  implemented_properties = ['energy', 'energies', 'forces', 'free_energy']
  implemented_properties += ['stress', 'stresses']  # bulk properties
  default_parameters = {'rc': None,}
  nolabel = True

  def __init__(self, **kwargs ) :
    Calculator.__init__( self, **kwargs )
    if self.parameters.pairwise_e is None :
      ValueError("function for evaluating pairwise energies has not been set")
    # Setup a cutoff value so we can use a neighbour list
    if self.parameters.rc is None : 
      ValueError("cutoff for pairwise interactions should be set")
    # Setup stuff for neighbour list
    self.nl = None
    self.pairwise_e = self.parameters.pairwise_e
    self.parameters.pairwise_e = None

  def calculate( self, atoms=None, properties=None, system_changes=all_changes, ) :
    if properties is None : properties = self.implemented_properties

    Calculator.calculate(self, atoms, properties, system_changes)

    natoms = len(self.atoms)

    rc = self.parameters.rc
    # potential value at rc
    e0, f0 = self.pairwise_e( rc )     

    if self.nl is None or 'numbers' in system_changes:
        self.nl = NeighborList([rc / 2] * natoms, self_interaction=False, bothways=True )
    
    self.nl.update(self.atoms)

    positions = self.atoms.positions
    cell = self.atoms.cell

    energies = np.zeros(natoms)
    forces = np.zeros((natoms, 3))
    stresses = np.zeros((natoms, 3, 3))

    for ii in range(natoms):
        neighbors, offsets = self.nl.get_neighbors(ii)
        cells = np.dot(offsets, cell)

        # pointing *towards* neighbours
        distance_vectors = positions[neighbors] + cells - positions[ii]

        r = np.sqrt( (distance_vectors ** 2).sum(1) )
        pairwise_energies, pairwise_forces = self.pairwise_e( r )
        pairwise_energies[r > rc] = 0.0
        pairwise_forces[r > rc] = 0.0

        pairwise_forces = pairwise_forces[:, np.newaxis] * distance_vectors
        energies[ii] += 0.5 * pairwise_energies.sum()  # atomic energies
        forces[ii] += pairwise_forces.sum(axis=0)
        stresses[ii] += 0.5 * np.dot(pairwise_forces.T, distance_vectors)

    # no lattice, no stress
    if self.atoms.cell.rank == 3:
        stresses = full_3x3_to_voigt_6_stress(stresses)
        self.results['stress'] = stresses.sum(axis=0) / self.atoms.get_volume()
        self.results['stresses'] = stresses / self.atoms.get_volume()

    energy = energies.sum()
    self.results['energy'] = energy
    self.results['energies'] = energies
    self.results['free_energy'] = energy
    self.results['forces'] = forces
