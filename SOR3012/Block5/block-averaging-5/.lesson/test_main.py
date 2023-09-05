try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

import AutoFeedback.plotchecks as pc
from AutoFeedback.plotclass import line
import unittest
from main import *

myeng = np.loadtxt("energies")[:,1]
xvals, yvals, k = [10,20,30,40,60,100,120,200,300,400], np.zeros(10), 0
for bb in xvals :
    nblocks = int( len( eng ) / bb )
    myaverage, mysq = 0, 0
    for i in range(nblocks) :
        myblocks = sum( myeng[i*bb:(i+1)*bb] ) / bb
        myaverage = myaverage + myblocks
        mysq = mysq + myblocks*myblocks

    mysq, myaverage = mysq / nblocks, myaverage / nblocks
    myvar = ( nblocks / (nblocks - 1) )*( mysq - myaverage*myaverage )
    yvals[k] = np.sqrt( myvar / nblocks )
    k = k + 1

line1 = line(xvals,yvals)
axislabels=["Size of blocks", "Error"]

class UnitTests(unittest.TestCase) :
    def test_blockVals(self) :
        inputs, outputs = [], []
        for i in range(len(xvals)) : 
            inputs.append((xvals[i],myeng,))
            outputs.append( yvals[i] )
        assert( check_func('block_average',inputs,outputs ) )

    def test_plot(self):
       assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )
