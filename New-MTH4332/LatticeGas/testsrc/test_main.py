try:
    import AutoFeedback.varchecks as vc
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotclass import line
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.utils import get_internal
import unittest

class UnitTests(unittest.TestCase) :
    def test_alternating(self) :
        alt = np.ones(nspins)
        for i in range(nspins) :
            if i%2==0 : alt[i] = -1
        assert( vc.check_vars("alternating", alt ) ) 
            
    def test_spinDown(self) :
        assert( vc.check_vars("alldown", -1*np.ones(nspins) ) )
        
    def test_spinUp(self) :
        assert( vc.check_vars("allup", np.ones(nspins) ) )

    def test_rising(self) :
        inputs, variables = [], []
        for i in range(6,21) :
            for j in range(3,5) :
                inputs.append((i,j))
                spins = np.zeros(i)
                for k in range(i) : spins[k] = k%j 
                variables.append( spins )
        assert( check_func('rising_states',inputs, variables ) )         
   
    def test_lowering(self) :
        inputs, variables = [], []
        for i in range(6,21) :
            for j in range(3,5) :
                inputs.append((i,j))
                spins = np.zeros(i)
                for k in range(i) : spins[k] = j - 1 - k%j 
                variables.append( spins )
        assert( check_func('lowering_states',inputs, variables ) )
        
    def test_updown(self) :
        inputs, variables = [], []
        for i in range(6,21) :
            for j in range(3,5) :
                inputs.append((i,j))
                spins = np.zeros(i)
                for k in range(i) :
                    kb = np.floor( k / j )
                    if kb%2==0 : spins[k] = k%j
                    else : spins[k] = j - 1 - k%j 
                variables.append( spins )
        assert( check_func('updown_states',inputs, variables ) )

    def test_eng1(self) :
        inputs, outputs = [], [] 
        for n in range(3,6) : 
            for i in range(2**n) :
                num, spins = i, np.zeros(n)
                for j in range(n) :
                    spins[j] = np.floor( num / 2**(n-1-j) )
                    num = num - spins[j]*2**(n-1-j)
                    if spins[j]==0 : spins[j] = -1
                for f in range(1,4) : 
                    inputs.append((spins,f))
                    outputs.append( -f*sum(spins) )
        assert( check_func('hamiltonian', inputs, outputs ) )   

    def test_eng2(self) :
        inputs, outputs = [], [] 
        for n in range(3,6) : 
            for i in range(3**n) :
                num, spins, eng = i, np.zeros(n), 0
                for j in range(n) :
                    spins[j] = np.floor( num / 3**(n-1-j) )
                    num = num - spins[j]*3**(n-1-j)
                    if spins[j]==1 : eng = eng+2 
                    elif spins[j]==2 : eng = eng+3
                inputs.append((spins,))
                outputs.append( eng )
        assert( check_func('hamiltonian2', inputs, outputs ) )   

    def test_eng3(self) :
        inputs, outputs = [], [] 
        for n in range(3,6) : 
            for i in range(4**n) :
                num, spins, eng = i, np.zeros(n), 0
                for j in range(n) :
                    spins[j] = np.floor( num / 4**(n-1-j) )
                    num = num - spins[j]*4**(n-1-j)
                    if spins[j]==1 or spins[j]==2 : eng = eng+1 
                    elif spins[j]==3 : eng = eng+2
                inputs.append((spins,))
                outputs.append( eng )
        assert( check_func('hamiltonian3', inputs, outputs ) )   

    def test_function1(self) :
        inputs, outputs = [], []
        for i in range(20) :
            val = np.random.randint(0,63)
            inputs.append((val,))
            oval = np.zeros(6)
            for j in range(6) : 
                ppp = 2**(5-j)
                oval[j] = int(np.floor( val / ppp ) )
                val = val - oval[j]*ppp
            outputs.append( oval )
        assert( fc.check_func('getBinary', inputs, outputs ) ) 

    def test_function2(self) :
        inputs, outputs = [], []  
        for b in range(2,11) :
            for i in range(20) :
                val = np.random.randint(0,127)
                inputs.append((val,b,))
                outval = np.zeros(7)
                for j in range(7) : 
                    ppp = b**(6-j)
                    outval[j] = int(np.floor( val / ppp ) )
                    val = val - outval[j]*ppp
                outputs.append( outval )
        assert( fc.check_func('convertToBase', inputs, outputs ) )

    def test_function3(self) :
        inputs, outputs = [], []  
        for n in range(4,9) :
            energies = np.zeros(2**n)
            for k in range(2**n) : 
                val = k
                for j in range(n) :
                    ppp = 2**(n-1-j)
                    coord = np.floor( val / ppp ) 
                    val = val - coord*ppp
                    if( coord==0 ) : energies[k] = energies[k] - 1
                    else :  energies[k] = energies[k] + 1
            inputs.append((n,))
            outputs.append( energies )
        assert( fc.check_func('microstate_energies', inputs, outputs ) )

    def test_partition_function(self) : 
        inputs, outputs = [], []  
        for k in range(5,8) :
            pfunc1, pfunc2, pfunc3 = 0, 0, 0
            for i in range(2**k) :
                num, spins = i, np.zeros(k)
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                pfunc1 = pfunc1 + np.exp( -hamiltonian( spins, 1 ) / 0.5 )
                pfunc2 = pfunc2 + np.exp( -hamiltonian( spins, 1 ) / 0.1 )
                pfunc3 = pfunc3 + np.exp( -hamiltonian( spins, 2 ) / 0.8 )
            inputs.append((k,1,0.5,))
            outputs.append( pfunc1 )
            inputs.append((k,-1,0.1,))
            outputs.append( pfunc2 )
            inputs.append((k,2,0.8,))
            outputs.append( pfunc3 )
        assert( check_func('partitionfunction', inputs, outputs ) )
            
    def test_hamiltonian( self ) :
        inputs, outputs = [], []
        for k in range(5,8) :  
            for i in range(2**k) :
                num, spins = i, np.zeros(k)
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                sumspins = sum( spins )
                for j in range(-3,4) : 
                    if j==0 : continue
                    inputs.append((spins,j,))
                    outputs.append( -j*sumspins )
        assert( check_func('hamiltonian', inputs, outputs ) )

    def test_hamiltonian1( self ) :
        inputs, outputs = [], []
        for k in range(5,8) :
            for i in range(2**k) :
                num, spins = i, np.zeros(k)
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                sumspins = sum( spins )
                for j in range(-3,4) :
                    if j==0 : continue
                    inputs.append((spins,j,))
                    outputs.append( -j*sumspins )
        assert( check_func('hamiltonian', inputs, outputs ) )
        
    def test_graph2(self) :
        xvals = np.linspace(0,2**8-1,2**8)
        yvals = np.zeros( 2**8 )
        for i in range(2**8) :
            val = i
            for j in range(8) :
                ppp = 2**(7-j)
                spin = np.floor( val / ppp )
                val = val - spin*ppp
                if spin==0 : yvals[i] = yvals[i] + 1
                else : yvals[i] = yvals[i] - 1
        
        line1 = line(xvals, yvals)
        
        axislabels=["numerical index","energy"] 
        assert( check_plot( [line1], explabels=axislabels, explegend=False,output=True) )
   
    def test_hamiltonian2( self ) :
        inputs, outputs = [], []
        for k in range(5,8) :
            for i in range(2**k) :
                num, spins = i, np.zeros(k)
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                sumspins = sum( spins )
                for j in range(-3,4) :
                    if j==0 : continue
                    inputs.append((spins,j,))
                    outputs.append( -j*sumspins )
        assert( check_func('hamiltonian', inputs, outputs ) )
        
    def test_graph4(self) :
        xvals = np.linspace( -8, 8, 9 )
        yvals = np.zeros(9)
        for i in range(2**8) :
            num, spins = i, np.zeros(8)
            for j in range(8) :
                spins[j] = np.floor( num / 2**(7-j) )
                num = num - spins[j]*2**(7-j)
                if spins[j]==0 : spins[j] = -1
            binn = int( ( hamiltonian(spins, 1)  + 8 ) / 2 )
            yvals[binn] = yvals[binn] + 1
        
        line1 = line( xvals, yvals )
        axislabels = [ "energy", "Number of microstates" ]
        assert( check_plot([],exppatch=line1,explabels=axislabels,explegend=False,output=True) ) 

    def test_hamiltonian5( self ) :
        inputs, outputs = [], []
        for k in range(5,8) :
            for i in range(2**k) :
                num, spins = i, np.zeros(k)
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                sumspins = sum( spins )
                for j in range(-3,4) :
                    if j==0 : continue
                    inputs.append((spins,j,))
                    outputs.append( -j*sumspins )
        assert( check_func('hamiltonian', inputs, outputs ) )
        
    def test_graph3(self) :
        xvals = np.linspace( -8, 8, 9 )
        yvals = np.zeros(9)
        for i in range(2**8) :
            num, spins = i, np.zeros(8)
            for j in range(8) :
                spins[j] = np.floor( num / 2**(7-j) )
                num = num - spins[j]*2**(7-j)
                if spins[j]==0 : spins[j] = -1
            binn = int( ( hamiltonian(spins, 1)  + 8 ) / 2 )
            yvals[binn] = yvals[binn] + 1
        
        line1 = line( xvals, np.log(yvals) )
        axislabels = [ "energy", "Entropy" ]
        assert( check_plot([],exppatch=line1,explabels=axislabels,explegend=False,output=True) ) 

    def test_ensemble_average(self) :
        inputs, outputs = [], [] 
        for k in range(5,8) :
            Z, numer = np.zeros(9), np.zeros(9)
            for i in range(2**k) :
                num, spins = i, k*[0]
                for j in range(k) :
                   spins[j] = np.floor( num / 2**(k-1-j) )
                   num = num - spins[j]*2**(k-1-j)
                   if spins[j]==0 : spins[j] = -1
                j = 0 
                for h in range(-1,2) : 
                    eee = hamiltonian( spins, h )
                    for t in [0.5,1.0,2.0] : 
                        bweight = np.exp( -eee / t )
                        numer[j] = numer[j] + eee*bweight
                        Z[j] = Z[j] + bweight
                        j = j + 1 
            j=0
            for h in range(-1,2) : 
                for t in [0.5,1.0,2.0] :
                    inputs.append((k,h,t,)) 
                    outputs.append(numer[j]/Z[j])
                    j = j + 1
        assert( check_func('ensemble_average', inputs, outputs ) )
        
    def test_hamiltonian3( self ) :
        inputs, outputs = [], []
        for k in range(5,8) :
            for i in range(2**k) :
                num, spins = i, np.zeros(k)
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                sumspins = sum( spins )
                for j in range(-3,4) :
                    if j==0 : continue
                    inputs.append((spins,j,))
                    outputs.append( -j*sumspins )
        assert( check_func('hamiltonian', inputs, outputs ) )    

    def test_hamiltonian4( self ) :
        inputs, outputs = [], []
        for k in range(5,8) :
            for i in range(2**k) :
                num, spins = i, np.zeros(k)
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                sumspins = sum( spins )
                for j in range(-3,4) :
                    if j==0 : continue
                    inputs.append((spins,j,))
                    outputs.append( -j*sumspins )
        assert( check_func('hamiltonian', inputs, outputs ) )
            
    def test_graph5(self) :
        xvals = get_internal('temperatures')
        yvals, k = np.zeros(len(xvals)), 0
        for t in xvals :
            n, z = 0, 0
            for i in range(2**8) :
                val, eng = i, 0
                for j in range(8) :
                    ppp = 2**(7-j)
                    spin = np.floor( val / ppp )
                    val = val - spin*ppp
                    if spin==0 : eng = eng + 1
                    else : eng = eng - 1
                bw = np.exp(-eng/t)
                n, z = n + eng*bw, z + bw
            yvals[k] = n / z
            k = k + 1
        
        line1 = line(xvals, yvals)
        axislabels=["temperature / arbitrary units","average energy / arbitrary units"]
        assert( check_plot( [line1], explabels=axislabels, explegend=False,output=True) )

    def test_graph1(self) :
        xvals = get_internal('temperatures')
        yvals = -8*( -np.exp(-1/xvals) - 3*np.exp(-3/xvals) )/ (1  + np.exp(-1/xvals) + np.exp(-3/xvals) )
        line1 = line(xvals, yvals)
        axislabels=["temperature","average energy"]
        assert( check_plot( [line1], explabels=axislabels, explegend=False,output=True) )
