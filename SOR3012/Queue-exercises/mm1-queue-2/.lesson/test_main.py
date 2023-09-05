try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
from AutoFeedback.varchecks import check_vars
import unittest
from main import *

p = lam / expr
x, e, v, bmin, bmax, isi = [], [], [], [], [], [] 
for i in range(9) :
    x.append(i) 
    prob = (1-p)*(p**i)
    e.append( prob )
    v.append( prob*(1-prob) / N ) 
    bmin.append(0) 
    bmax.append(1)
    isi.append(False)

rvar = randomvar( e, variance=v, vmin=bmin, vmax=bmax, isinteger=isi )
line1 = line( x, rvar  )
axislabels=["number of people in queue", "probability"]

class UnitTests(unittest.TestCase) :
    def test_variables(self) : 
      assert(check_vars("lam",0.5))
      assert(check_vars("expr",1.0))
      assert(check_vars("N",100000)) 
 
    def test_queue(self) :
      assert(check_plot([],exppatch=line1,explabels=axislabels,explegend=False,output=True)) 
