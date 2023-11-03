try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

import AutoFeedback.varchecks as vc
from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotclass import line
import unittest
from main import *

# Insert code from last exercise to create an atoms object and set masses and velocities here.
gatatoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )

# Attach the method that should be used to calculate energies and forces to the atoms object
gatatoms.calc = pairwise_calculator( rc=4, pairwise_e=fff )

# Run the optimisation
gatopt = BFGS(gatatoms)
gatopt.run(fmax=0.001)

# And get the vibrations
gatvib = Vibrations(gatatoms)
gatvib.run()
data = gatvib.get_vibrations()
gathessian = data.get_hessian_2d()
gateigvals, crap= np.linalg.eig( gathessian )

# And get the density of states
gat_frequencies = np.sqrt( gateigvals )

gathisto = np.zeros(nbins)
for e in gat_frequencies :     
    ibin = int( np.floor( (e-minx) / delx) )
    gathisto[ibin] = gathisto[ibin] + 1

line1 = line( xvals, gathisto )
axislabels = ['frequencies / arbitrary units', 'Number of states' ]

def mylj(r) :
    r2 = r*r
    r6 = r2*r2*r2
    r12 = r6*r6
    eng = 4*( ( 1/r12 ) - (1/r6) )
    force = -24*( 2/r12 - 1/r6 ) / r2
    return eng, force

class UnitTests(unittest.TestCase) :
    def test_forces(self) :
        inputs, outputs, xv, d = [], [], np.linspace(0.5,4,200), 0.000001
        for x in xv :
            inputs.append((x,))
            e, f = mylj(x)
            outputs.append((e,f,))
        assert check_func("fff", inputs, outputs )

    def test_calculator(self):
        myatoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
        try:
            from main import atoms
            student_pos = atoms.get_positions()
        except ImportError:
            assert vc.check_vars("atoms",0)

        try:
           student_energy = atoms.get_potential_energy()
        except AttributeError:
           assert vc.check_vars("atoms.potential_energy",0)

        myatoms.set_positions( student_pos )
        myatoms.calc = pairwise_calculator( rc=4, pairwise_e=mylj )
        myeng = myatoms.get_potential_energy()

        assert vc.check_vars( student_energy, myeng, printname="atoms.potential_energy" )

    def test_density_of_states(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
