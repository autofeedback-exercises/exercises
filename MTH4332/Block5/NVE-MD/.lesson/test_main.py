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

class UnitTests(unittest.TestCase) :
    def test_forces2(self) :
        inputs, outputs, xv, d = [], [], np.linspace(0.5,4,200), 0.000001
        for x in xv :
            inputs.append((x,))
            e, f = mylj(x)
            outputs.append((e,f,))
        assert check_func("fff", inputs, outputs )

    def test_calculator2(self):
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

    def test_conservation(self) :
        gatxvals = np.zeros(101)
        for i in range(101) : gatxvals[i] = i*tstep
        gatyvals = initial_energy*np.ones(101)
        
        line1 = line( gatxvals, gatyvals )
        axislabels = ['time / arbitrary units', 'total energy / arbitrary units' ]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
