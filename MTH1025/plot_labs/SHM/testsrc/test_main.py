try:
    from AutoFeedback import varchecks as vc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback[plot]"])
    from AutoFeedback import var as vc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line

import unittest
import numpy as np

x= np.linspace(-7,7,1000)
xf = np.linspace(-2*np.pi,2*np.pi,17)
xg = np.linspace(-2*np.pi,2*np.pi,21)
line1=line(x, np.sin(4*x), linestyle=['-','solid'],\
colour=['b','blue',(0.0,0.0,1.0,1)],label='sin(4x)')
line2=line(x, np.sin(5*x), linestyle=['--','dashed'],\
colour=['r','red',(1.0,0.0,0.0,1)],label='sin(5x)')
line3=line(xf,np.zeros(17),marker=['o','circle'],\
colour=['b','blue',(0.0,0.0,1.0,1)])
line4=line(xg,np.zeros(21),marker=['D','d','thin_diamond','diamond'],\
colour=['r','red',(1.0,0.0,0.0,1)])

axes=[-2*np.pi,2*np.pi,-1.5,1.5]

axislabels=["x","y",""]


class UnitTests(unittest.TestCase):
    def test_step1(self):
        assert(vc.check_vars('x',np.linspace(-7,7,1000)))

    def test_step2(self):
        assert(vc.check_vars('f',np.sin(4*np.linspace(-7,7,1000))))

    def test_step3(self):
        assert(vc.check_vars('g',np.sin(5*np.linspace(-7,7,1000))))

    def test_step4(self):
        assert(vc.check_vars('xf',np.linspace(-2*np.pi,2*np.pi,17)))

    def test_step5(self):
        assert(vc.check_vars('xg',np.linspace(-2*np.pi,2*np.pi,21)))

    def test_step6(self):
        assert(vc.check_vars('zf',np.zeros(17)))

    def test_step7(self):
        assert(vc.check_vars('zg',np.zeros(21)))

    def test_step8(self):
        assert(pc.check_plot([line1,line2,line3,line4],expaxes=axes,explabels=axislabels,explegend=True,output=True))
