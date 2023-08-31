try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback import check_vars
import AutoFeedback.plotchecks as pc
from AutoFeedback.plotclass import line
import unittest
from main import *

filedata = np.loadtxt("md_results.txt")
cvmid = np.zeros(len(filedata))
for i in range(len(filedata)) :
    cvmid[i] = (filedata[i,3] - filedata[i,1]*filedata[i,1]) / (filedata[i,0]*filedata[i,0])
    
line1 = line( filedata[:,0], cvmid )
axislabels = ["temperature / natural units", "heat capacity / natural units"]

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )

    def test_errors( self ) :
        err = np.zeros(len(filedata))
        for i in range(len(filedata)) :
            err[i] = ( filedata[i,4] + 2*filedata[i,1]*filedata[i,2] ) / ( filedata[i,0]*filedata[i,0] )
        assert( check_vars( "cv_errors", err ) ) 
