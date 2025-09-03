try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.utils import get_internal
from AutoFeedback.varchecks import check_vars
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import unittest

def genSpins(N) :
    spins = np.ones([N,N])
    for i in range(N) :
        for j in range(N) :
            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1
    return spins

class UnitTests(unittest.TestCase) :
    def test_estimate(self) : 
       inputs, outputs = [], []
       myvar = randomvar( 0, variance=1, vmin=-1, vmax=1, isinteger=True )
       for j in range(3,8) :
           inputs.append((j,))
           outputs.append( myvar )
       assert( check_func('getstate',inputs, outputs ) )

    def test_flipSpin(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            spins = genSpins( N )
            for j in range(30) : 
                ispin = int(np.floor( N*np.random.uniform(0,1) ) )
                jspin = int(np.floor( N*np.random.uniform(0,1) ) )
                inputs.append((spins,ispin,jspin,))
                spincopy = np.copy(spins) 
                spincopy[ispin,jspin] = -1*spincopy[ispin,jspin]
                outputs.append(spincopy)
        assert( check_func("flipSpin", inputs, outputs ) )

    def test_flipAllSpins(self) : 
        inputs, outputs = [], []
        for N in range(3,8) :
            for k in range(3) :
                spins = genSpins( N ) 
                for j in range(2) :
                    inputs.append((spins,))
                    spins = -1*np.copy(spins)
                    outputs.append(spins) 
        assert( check_func("flipAllSpins", inputs, outputs ) )

    def test_chooseMove(self) : 
        inputs, outputs = [], []
        for N in range(3,6) :
            spins = np.ones([N,N])
            inputs.append((spins,))
            p = 1/(1+N*N)
            myvar = randomvar( p, variance=p*(1-p), vmin=0, vmax=1, isinteger=True )
            outputs.append( myvar )
        assert( check_func("chooseMove", inputs, outputs ) )

    def test_chooseSpin(self) :
        inputs, outputs = [], []
        for N in range(3,8) :
            spins = np.ones([N,N])
            inputs.append((spins,))
            myvar = randomvar( (N-1)/2, variance=(N*N-1)/12, vmin=0, vmax=N-1, isinteger=True, nsamples=100 )
            outputs.append( myvar )
        assert( check_func("chooseSpin", inputs, outputs ) )

    def test_mag(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            for k in range(10) : 
                spins = np.ones([N,N])
                for i in range(N) :
                    for j in range(N) :
                        if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                inputs.append((spins,))
                outputs.append( sum(sum(spins)) / (N*N) )
        assert( check_func("magnetisation", inputs, outputs ) )

    def test_hamiltonian1(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            for h in [-2,-1,1,2] :
                for k in range(10) : 
                    spins = np.ones([N,N])
                    for i in range(N) :
                        for j in range(N) :
                            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                    inputs.append((spins,h))
                    outputs.append( -h*sum(sum(spins)) )
        assert( check_func("hamiltonian", inputs, outputs ) )

    def test_hamiltonian2(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            for k in range(10) : 
                spins = np.ones([N,N])
                for i in range(N) :
                    for j in range(N) :
                        if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                inputs.append((spins,))
                Ene = 0 
                for i in range(N) :
                    for j in range(N) :
                        Ene = Ene + spins[i,j]*( spins[ (i+1)%N, j] + spins[ i, (j+1)%N] + spins[(i-1)%N, j] + spins[ i, (j-1)%N] )
                outputs.append( - Ene / 2 )
        assert( check_func("hamiltonian", inputs, outputs ) )

    def test_hamiltonian3(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            for h in [-2,-1,1,2] :
                for k in range(10) : 
                    spins = np.ones([N,N])
                    for i in range(N) :
                        for j in range(N) :
                            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                    inputs.append((spins,h))
                    Ene = 0 
                    for i in range(N) :
                        for j in range(N) :
                            Ene = Ene + spins[i,j]*( spins[ (i+1)%N, j] + spins[ i, (j+1)%N] + spins[(i-1)%N, j] + spins[ i, (j-1)%N] )
                    outputs.append( - Ene / 2 - h*sum( sum( spins ) )  )
        assert( check_func("hamiltonian", inputs, outputs ) )

    def test_graph4(self) :
        temp = get_internal("temp")
        nframes = get_internal("nframes")
        xv = np.linspace( 1, nframes, nframes )
        yv = randomvar( 0, variance=temp/2, isinteger=False )
        line1 = line( xv, yv )
        axislabels = [ "index", "particle position" ]
        assert( check_plot([line1],explabels=axislabels,explegend=False,output=True) ) 

    def test_hamiltonian4(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            for h in [-2,-1,1,2] :
                for k in range(10) : 
                    spins = np.ones([N,N])
                    for i in range(N) :
                        for j in range(N) :
                            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                    inputs.append((spins,h))
                    Ene = 0 
                    for i in range(N) :
                        for j in range(N) :
                            Ene = Ene + spins[i,j]*( spins[ (i+1)%N, j] + spins[ i, (j+1)%N] + spins[(i-1)%N, j] + spins[ i, (j-1)%N] )
                    outputs.append( - Ene / 2 - h*sum( sum( spins ) )  )
        assert( check_func("hamiltonian", inputs, outputs ) )

    def test_move(self) :
        hamiltonian = get_internal("hamiltonian") 
        inputs, outputs = [], []
        for N in range(10,15) :
            for h in [-2,-1,0,1,2] :
                spins = np.ones([N,N])
                for i in range(N) :
                        for j in range(N) :
                            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                e = hamiltonian(spins,h)
                inputs.append((np.copy(spins),e,h,N*N,))
                spins = -1*spins
                e = hamiltonian(spins,h)
                outputs.append(e)
                for i in range(10) : 
                    rmove = int( np.floor( N*N*np.random.uniform(0,1) ) )
                    inputs.append((np.copy(spins),e,h,rmove,))
                    i, j = int( np.floor( rmove / N ) ), rmove%N
                    spins[i,j] = -1*spins[i,j]
                    e = hamiltonian(spins,h)
                    outputs.append(e)
        assert( check_func("new_energy", inputs, outputs ) )    

    def test_MC1(self) : 
        inputs, outputs = [], []
        for N in [30,40,50,60,70,80,90,100] :
            for e in [10,20] : 
                for s in [1,5,10] :
                    for h in [-1,0,1] :
                        for t in range(1,2,3) : 
                            myseed = np.random.randint(1000)
                            inputs.append((N,e,s,10,h,t,myseed,))
                            np.random.seed(myseed)
                            spins = np.ones([10,10])
                            for i in range(10) :
                                for j in range(10) : 
                                    if np.random.uniform(0,1)<0.5 : spins[i,j]=-1

                            eng = 0
                            for i in range(spins.shape[0]) :
                                for j in range(spins.shape[1]) :
                                    eng = eng + spins[i,j]*( spins[ (i+1)%spins.shape[0], j] + spins[ i, (j+1)%spins.shape[1]] + spins[(i-1)%spins.shape[0], j] + spins[ i, (j-1)%spins.shape[1]] )
                            eng = - eng / 2 - h*sum( sum( spins ) )

                            neweng, vals = 0, np.zeros( int( np.floor(N / s ) ) )
                            for i in range(e + N) : 
                                move = np.floor( (101)*np.random.uniform(0,1) )
                                if move==100 : 
                                   neweng = eng + 2*h*sum( sum(spins) )
                                else :
                                   j, k = int( np.floor( move / 10 ) ), int( move%10 )
                                   neweng = eng + 2*spins[j,k]*( spins[(j+1)%10,k] + spins[(j-1)%10,k] + spins[j,(k-1)%10] + spins[j,(k+1)%10] + h )

                                if np.random.uniform(0,1)<min(1.0, np.exp( -neweng/t ) / np.exp( -eng/t ) )  :
                                   eng = neweng
                                   if move==100 : 
                                       spins = -1*spins
                                   else : 
                                       j, k = int( np.floor( move / 10 ) ), int( move%10 )
                                       spins[j,k] = -1*spins[j,k]

                                step = i-e
                                if step>=0 and step%s==0 :
                                   vals[int(step/s)] = eng
                            outputs.append(vals)
        assert( check_func("monte_carlo", inputs, outputs ) )    

    def test_MC2(self) : 
        inputs, outputs = [], []
        for N in [30,40,50,60,70,80,90,100] :
            for e in [10,20] : 
                for s in [1,5,10] :
                    for h in [-1,0,1] :
                        for t in range(1,2,3) : 
                            myseed = np.random.randint(1000)
                            inputs.append((N,e,s,10,h,t,myseed,))
                            np.random.seed(myseed)
                            spins = np.ones([10,10])
                            for i in range(10) :
                                for j in range(10) : 
                                    if np.random.uniform(0,1)<0.5 : spins[i,j]=-1

                            eng = 0
                            for i in range(spins.shape[0]) :
                                for j in range(spins.shape[1]) :
                                    eng = eng + spins[i,j]*( spins[ (i+1)%spins.shape[0], j] + spins[ i, (j+1)%spins.shape[1]] + spins[(i-1)%spins.shape[0], j] + spins[ i, (j-1)%spins.shape[1]] )
                            mag = sum( sum( spins ) )
                            eng = - eng / 2 - mag 

                            neweng, M, M2, ns = 0, 0, 0, 0
                            for i in range(e + N) : 
                                move = np.floor( (101)*np.random.uniform(0,1) )
                                if move==100 : 
                                   neweng = eng + 2*h*mag 
                                else :
                                   j, k = int( np.floor( move / 10 ) ), int( move%10 )
                                   neweng = eng + 2*spins[j,k]*( spins[(j+1)%10,k] + spins[(j-1)%10,k] + spins[j,(k-1)%10] + spins[j,(k+1)%10] + h )

                                if np.random.uniform(0,1)<min(1.0, np.exp( -neweng/t ) / np.exp( -eng/t ) )  :
                                   eng = neweng
                                   if move==100 : 
                                       spins = -1*spins
                                       mag = -1*mag
                                   else : 
                                       j, k = int( np.floor( move / 10 ) ), int( move%10 )
                                       mag = mag + 2*spins[j,k]
                                       spins[j,k] = -1*spins[j,k]

                                step = i-e
                                if step>=0 and step%s==0 : M, M2, ns = M + mag, M2 + mag*mag, ns + 1 
                      
                            
                            M = M / ns 
                            S = ( ns / (ns-1) )*( M2/ns - M*M )
                            outputs.append( S / ( 100*t ) )
        assert( check_func("monte_carlo", inputs, outputs ) )    

    def test_graph1(self) :
        maxx = get_internal("maxx")
        minx = get_internal("minx")
        nbins = get_internal("nbins")
        ddd = (maxx - minx) / nbins
        n, xv, yv = 0, np.zeros(nbins), np.zeros(nbins)
        for m in np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/IsingModel/magnetisations") :
            mave = m / (20*20)
            xb = int( np.floor( (mave-minx) / ddd ) )
            yv[xb] = yv[xb] + 1
            n = n + 1
        
        yv = yv / n
        xv = np.zeros(nbins)
        for i in range(nbins) : xv[i] = (i+0.5)*ddd

        line1 = line( xv, yv )
        axislabels = [ "average magnetisation per spin", "probability density" ]
        assert( check_plot([line1],explabels=axislabels,explegend=False,output=True) ) 

    def test_graph2(self) :
        maxx = get_internal("maxx")
        minx = get_internal("minx")
        nbins = get_internal("nbins")
        ddd = (maxx - minx) / nbins
        n, xv, yv = 0, np.zeros(nbins), np.zeros(nbins)
        for m in np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/IsingModel/magnetisations") :
            mave = m / (20*20)
            xb = int( np.floor( (mave-minx) / ddd ) )
            yv[xb] = yv[xb] + 1
            n = n + 1
        
        yv = -5.0*np.log( yv / n )
        xv = np.zeros(nbins)
        for i in range(nbins) : xv[i] = (i+0.5)*ddd
        
        line1 = line( xv, yv )
        axislabels = [ "average magnetisation per spin", "free energy / natural units" ]
        assert( check_plot([line1],explabels=axislabels,explegend=False,output=True) ) 

    def test_x( self ) : 
        maxx = get_internal("maxx")
        minx = get_internal("minx")
        nbins = get_internal("nbins")
        testx, testdelx = np.zeros(nbins), ( maxx - minx ) / nbins
        for i in range(nbins) : testx[i] = (i+0.5)*testdelx
        assert( check_vars( "xv", testx ) )

    def test_errors( self ) :
        testmags = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/IsingModel/magnetisations")
        maxx = get_internal("maxx")
        minx = get_internal("minx")
        nbins = get_internal("nbins")
        blocksize = get_internal("blocksize")
        testdelx = ( maxx - minx ) / nbins
        test_v, test_v2 = np.zeros(nbins), np.zeros( nbins )
        testnblocks = int( np.floor( len(testmags) / blocksize ) )
        for i in range(testnblocks) :
            testhisto = np.zeros(nbins)
            for j in range(i*blocksize,(i+1)*blocksize) :
                testmav = testmags[j] / (20*20)
                txbin = int( np.floor( (testmav-minx) / testdelx ) )
                testhisto[txbin] = testhisto[txbin] + 1
            testhisto = testhisto / blocksize
            test_v = test_v + testhisto
            test_v2 = test_v2 + testhisto*testhisto
        
        test_v = test_v / testnblocks
        test_v2 = np.sqrt( (1/(testnblocks-1))*( test_v2/testnblocks - test_v*test_v ) )*scipy.stats.norm.ppf(0.95)
        
        testfes = -5.0*np.log( test_v )
        testerr = 5*test_v2 / test_v
        for i in range(len(test_v)) :
            if test_v[i]==0 : testerr[i] = 0

        assert( check_vars( "lower_yv",  testfes-testerr ) )
        assert( check_vars( "upper_yv", testfes+testerr ) )  

    def test_graph3(self) :
        data = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/IsingModel/magnetisations")
        maxx = get_internal("maxx")
        minx = get_internal("minx")
        nbins = get_internal("nbins")
        ddd = (maxx - minx) / nbins
        xv = np.array([10, 20, 25, 100, 200, 250, 500])
        yv = np.zeros(len(xv))
        for k,bls in enumerate(xv) :
            nb = int( len(data) / bls )
            fv, fv2 = np.zeros(nbins), np.zeros( nbins )
            # This loop calculates your nblocks estimates of the histogram
            for i in range(nb) :
                # Your code for calculating each of the nblocks estimate of the histogram goes here
                histo = np.zeros(nbins)
                for j in range(i*bls,(i+1)*bls) :
                    mav = data[j] / (20*20)
                    xbin = int( np.floor( (mav-minx) / ddd ) )
                    histo[xbin] = histo[xbin] + 1
                histo = histo / bls
                fv = fv + histo
                fv2 = fv2 + histo*histo
        
            fv = fv / nb
            fv2 = np.sqrt( (1/(nb-1))*( fv2/nb - fv*fv ) )*scipy.stats.norm.ppf(0.95)
        
            n = 0
            for i in range(len(fv)) :
                if fv[i]>0 :
                   yv[k] += 5*fv2[i] / fv[i]
                   n = n + 1
            yv[k] = yv[k] / n
        
        
        line1 = line( xv, yv )
        axislabels = [ "Length of block", "Average error on free energy" ]
        assert( check_plot([line1],explabels=axislabels,explegend=False,output=True) ) 
