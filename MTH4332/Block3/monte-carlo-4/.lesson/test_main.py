try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_MC(self) : 
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
