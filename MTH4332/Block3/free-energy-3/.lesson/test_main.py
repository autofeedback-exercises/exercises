try:
    from AutoFeedback import check_vars
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback import check_vars

import unittest
from main import *

testmags = np.loadtxt("magnetisations")
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

class UnitTests(unittest.TestCase) :
    def test_x( self ) : 
        testx, testdelx = np.zeros(nbins), ( maxx - minx ) / nbins
        for i in range(nbins) : testx[i] = (i+0.5)*testdelx
        assert( check_vars( "xv", testx ) )
  
    def test_lowe( self ) :
        assert( check_vars( "lower_yv",  testfes-testerr ) )

    def test_uppere( self ) :
        assert( check_vars( "upper_yv", testfes+testerr ) )  
