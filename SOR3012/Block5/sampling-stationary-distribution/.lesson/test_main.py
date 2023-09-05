try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

mya = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
mw, mlv = np.linalg.eig( mya.T )
for i in range(len(mw)) : 
    if mw[i]>0.9 : 
       myind = i
       break

e, v, bmin, bmax, isi = mlv[:,myind]/sum(mlv[:,myind]), [], [], [], []
for i in range(3) :
    v.append( e[i]*(1-e[i]) / nsteps )
    bmin.append(0)
    bmax.append(1)
    isi.append(False)

rvar = randomvar( e, variance=v, vmin=bmin, vmax=bmax, isinteger=isi )
line1 = line( [1,2,3], rvar  )
axislabels=["state", "probability"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([],exppatch=line1,explabels=axislabels,explegend=False,output=True))
