try:
    import AutoFeedback.varchecks as vc
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.funcchecks import check_func
from AutoFeedback.randomclass import randomvar
from AutoFeedback.utils import get_internal
import matplotlib.pyplot as plt
import ase
from ase.calculators.calculator import Calculator, all_changes
from ase.lattice.cubic import FaceCenteredCubic
from ase.io.trajectory import Trajectory 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def mylj(r) :
    r2 = r*r
    r6 = r2*r2*r2
    r12 = r6*r6
    eng = 4*( ( 1/r12 ) - (1/r6) )
    force = -24*( 2/r12 - 1/r6 ) / r2
    return eng, force

class UnitTests(unittest.TestCase) :
    def test_ase(self) :
        myatoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
        atoms = get_internal("atoms")
        student_pos = atoms.get_positions()
        student_mass = atoms.get_masses()
        student_velocities = atoms.get_velocities().flatten()

        r = randomvar( 0, variance=2, isinteger=False )
        assert vc.check_vars( student_velocities, r, printname="atoms.velocities" )

    def test_forces(self) :
        inputs, outputs, xv, d = [], [], np.linspace(0.5,4,200), 0.000001
        for x in xv :
            inputs.append((x,))
            e, f = mylj(x)
            outputs.append((e,f,))
        assert check_func("fff", inputs, outputs )

    def test_calculator(self):
        pairwise_calculator = get_internal("pairwise_calculator")
        myatoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
        atoms = get_internal('atoms')
        student_pos = atoms.get_positions()
        student_mass = atoms.get_masses()
        assert vc.check_vars( student_mass, np.ones(len(atoms)), printname="atoms.masses" )
        student_energy = atoms.get_potential_energy()

        myatoms.set_positions( student_pos )
        myatoms.calc = pairwise_calculator( rc=4, pairwise_e=mylj )
        myeng = myatoms.get_potential_energy()

        assert vc.check_vars( student_energy, myeng, printname="atoms.potential_energy" )
            
    def test_energies(self) :
        pairwise_calculator = get_internal("pairwise_calculator")
        try: 
          ftraj = Trajectory("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesI/mytraj.traj")
        except:
          assert vc.check_vars("energies", 0) 

        myatoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
        myeng = [] 
        myatoms.calc = pairwise_calculator( rc=4, pairwise_e=mylj )
        for a in ftraj : 
            myatoms.set_positions( a.get_positions() )
            myeng.append( myatoms.get_potential_energy() )

        ftraj.close()
        assert vc.check_vars( energies, myeng, printname="energies" )
            
    def test_rdf3(self) :
        nf, N, V = 0, 0, 0
        maxd = get_internal("maxd")
        nbins = get_internal("nbins")
        delx, histo = maxd / nbins, np.zeros(nbins)
        for atoms in Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesI/trajectory.traj') :
            nf, N, V = nf + 1, len(atoms), atoms.get_volume()
            distances = atoms.get_all_distances( mic=True )
            for i in range(1,distances.shape[0]) :
                for j in range(0,i) :
                    if  distances[i,j]>maxd : continue
                    xbin = int( np.floor( distances[i,j] / delx ) )
                    histo[xbin] = histo[xbin] + 2
        
        xbins = np.zeros(nbins)
        for i in range(nbins) :
            if i==0 :
                xbins[i] = 0.5*delx
                vol = (4/3)*np.pi*delx**3*(N/V)
                histo[i] = histo[i] / ( vol*nf*N )
            else :
                xbins[i] = (i+0.5)*delx
                vol = (4/3)*np.pi*((delx*(i))**3 - (delx*(i-1))**3)*(N/V)
                histo[i] = histo[i] / ( vol*nf*N )
        
        line1 = line( xbins, histo )
        axislabels = ['r / sigma', 'g(r)' ]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))

    def test_rdf1(self) :
        nf, N, V  = 0, 0, 0
        delx, histo = maxd / nbins, np.zeros([5,nbins])
        bsize = int( np.floor( len( Trajectory('trajectory.traj') ) / 5 ) )
        for atoms in Trajectory('trajectory.traj') :
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
        
        gat_average = average / 5
        gat_error = np.sqrt( (1/4)*( average2 / 5 - gat_average*gat_average ) )*scipy.stats.norm.ppf(0.95)

        assert vc.check_vars("average",gat_average)
        assert vc.check_vars("error",gat_error)

    def test_fcc(self) : 
        inputs, outputs = [], []
        for atoms in  Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesI//trajectory.traj') :
            inputs.append((atoms,))
            pppp = np.zeros(len(atoms))
            distances = atoms.get_all_distances( mic=True )
            vecs = atoms.get_all_distances( mic=True, vector=True )
            for i in range(distances.shape[0]) : 
                fcc_numer, fcc_denom = 0, 0
                for j in range(distances.shape[1]) : 
                    if i==j or distances[i,j]>1.5 : continue
                    fcc_denom += 1
                    x, y, z, r = vecs[i,j,0], vecs[i,j,1], vecs[i,j,2], distances[i,j]
                    fcc_numer += ( ( (x*y)**4 + (x*z)**4 + (y*z)**4 ) / (r**8) - ( 27*(x*y*z)**4 ) / r**12 )
    
                pppp[i] = 80080/(2717+16*27)*(fcc_numer/fcc_denom) + 16*(27-143)/(2717+16*27) 
            outputs.append( pppp ) 

        assert( check_func("fcc_cubic", inputs, outputs ) )

    def test_rdf2(self) :
        minx = get_internal("minx")
        maxx = get_internal("maxx")
        nbins = get_internal("nbins") 
        nf, delx = 0, (maxx-minx) / nbins 
        histo = np.zeros([5,nbins])
        bsize = int( np.floor( len( Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesI/trajectory.traj') ) / 5 ) )
        for atoms in Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesI/trajectory.traj') :
            bnum = int( np.floor( nf / bsize ) )
            nf = nf + 1
            distances = atoms.get_all_distances( mic=True )
            vecs = atoms.get_all_distances( mic=True, vector=True )
            for i in range(distances.shape[0]) : 
                fcc_numer, fcc_denom = 0, 0
                for j in range(distances.shape[1]) : 
                    if i==j or distances[i,j]>1.5 : continue
                    fcc_denom += 1
                    x, y, z, r = vecs[i,j,0], vecs[i,j,1], vecs[i,j,2], distances[i,j]
                    fcc_numer += ( ( (x*y)**4 + (x*z)**4 + (y*z)**4 ) / (r**8) - ( 27*(x*y*z)**4 ) / r**12 )
    
            final = 80080/(2717+16*27)*(fcc_numer/fcc_denom) + 16*(27-143)/(2717+16*27)
            xbin = int( np.floor( (final + 0.5) / delx ) )
            if xbin<0 : raise ValueError('xbin should not be negative')
            histo[bnum,xbin] = histo[bnum,xbin] + 1
 
        histo = histo / bsize
        average, average2 = np.zeros(nbins), np.zeros(nbins)
        for i in range(5) : 
            average = average + histo[i,:]
            average2 = average2 + histo[i,:]*histo[i,:]
        
        gat_average = average / 5
        gat_error = np.sqrt( (1/4)*( average2 / 5 - gat_average*gat_average ) )*scipy.stats.norm.ppf(0.95)

        gat_fes, gat_fes_error = -2.0*np.log( gat_average ), gat_error
        for i in range(len(gat_average)) :
            if gat_average[i]!=0 : gat_fes_error[i] = 2*gat_error[i] / gat_average[i]

        assert vc.check_vars("fes",gat_fes)
        assert vc.check_vars("error",gat_fes_error)
