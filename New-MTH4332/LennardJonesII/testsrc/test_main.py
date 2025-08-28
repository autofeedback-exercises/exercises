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
from AutoFeedback.utils import get_internal
import unittest

def mylj(r) :
    r2 = r*r
    r6 = r2*r2*r2
    r12 = r6*r6
    eng = 4*( ( 1/r12 ) - (1/r6) )
    force = -24*( 2/r12 - 1/r6 ) / r2
    return eng, force

class UnitTests(unittest.TestCase) :
    def test_forces1(self) :
        inputs, outputs, xv, d = [], [], np.linspace(0.5,4,200), 0.000001
        for x in xv :
            inputs.append((x,))
            e, f = mylj(x)
            outputs.append((e,f,))
        assert check_func("fff", inputs, outputs )

    def test_calculator1(self):
        myatoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
        atoms = get_internal('atoms')        
        student_pos = atoms.get_positions()
        student_energy = atoms.get_potential_energy()

        myatoms.set_positions( student_pos )
        myatoms.calc = pairwise_calculator( rc=4, pairwise_e=mylj )
        myeng = myatoms.get_potential_energy()

        assert vc.check_vars( student_energy, myeng, printname="atoms.potential_energy" )

    def test_density_of_states(self) :
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
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))

    def test_heat_capcity3(self) :
        temps = get_internal("T")
        frequency = get_internal("frequency")
        gb = np.exp(-frequency/temps)
        gnb = 1-gb
        gat_heatcv = (frequency*frequency)/(temps*temps)*( gb /gnb + gb*gb/(gnb*gnb) )
        
        line1 = line( temps, gat_heatcv )
        axislabels = ['Temperature / natural units', 'Heat capacity / natural units' ]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))

    def test_heat_capcity4(self) :
        temps = get_internal("T")
        frequency = get_internal("frequency")
        gat_heatcv = np.zeros(len(temps))
        for i, t in enumerate(temps) :
           gb = np.exp(-frequencies/t)
           gnb = 1-gb
           gat_sumheatcv = (frequencies*frequencies)/(t*t)*( gb /gnb + gb*gb/(gnb*gnb) )
           gat_heatcv[i] = sum(gat_sumheatcv)/(len(frequency)/3)
        
        line1 = line( temps, gat_heatcv )
        axislabels = ['Temperature / natural units', 'Heat capacity per atom / natural units' ]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))

    def test_forces2(self) :
        inputs, outputs, xv, d = [], [], np.linspace(0.5,4,200), 0.000001
        for x in xv :
            inputs.append((x,))
            e, f = mylj(x)
            outputs.append((e,f,))
        assert check_func("fff", inputs, outputs )

    def test_calculator2(self):
        myatoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
        atoms = get_internal('atoms')
        student_pos = atoms.get_positions()
        student_energy = atoms.get_potential_energy()

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

    def test_heat_capcity1(self) :
        ncorr = get_internal("ncorr")
        gatftraj = Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesII/nve-short.traj')
        gat_acf, gat_norm = np.zeros(ncorr), np.zeros(ncorr)
        
        k = 0
        for atoms in gatftraj :
            vel = atoms.get_velocities().flatten()
            maxn = min( len(gatftraj), k + ncorr ) - k
            for i in range(maxn) :
                veln = ftraj[k + i].get_velocities().flatten()
                gat_acf[i] = gat_acf[i] + np.dot( veln.T, vel ) / (3*len( atoms ))
                gat_norm[i] = gat_norm[i] + 1
            k = k + 1
        
        gat_acf = gat_acf / gat_norm
        
        gattimes = 0.005*np.linspace(0, ncorr-1, ncorr)
        line1 = line( gattimes, gat_acf )
        axislabels = ['time / arbitrary units', 'velocity autoccoreation function' ]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))

    def test_heat_capcity2(self) :
        gatftraj = Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesII/nve-short.traj')
        gatnatoms = len( gatftraj[0].get_velocities() )
        gatvtraj = np.zeros([ 3*gatnatoms, len(gatftraj) ])
        
        k = 0
        for atoms in gatftraj :
            gatvtraj[:,k] = atoms.get_velocities().flatten()
            k = k + 1
        
        gatfftraj = np.fft.rfft(gatvtraj,axis=1)
        gatfdos = np.mean(gatfftraj*np.conjugate(gatfftraj),axis=0) / len(gatftraj)
        
        gatfreq = np.fft.rfftfreq( len(gatftraj), d=0.005 )
        line1 = line( gatfreq, gatfdos )
        axislabels = ['frequency / arbitrary units', 'vibrational density of states' ]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
