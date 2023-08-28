try:                
    from AutoFeedback.funcchecks import check_func
except: 
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func
 
from AutoFeedback.plotclass import line
from AutoFeedback.plotchecks import check_plot                   
import numpy as np  
import unittest     
from main import *

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

class UnitTests(unittest.TestCase) :
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
        
    def test_graph(self) :
        assert( check_plot( [line1], explabels=axislabels, explegend=False,output=True) )
   
