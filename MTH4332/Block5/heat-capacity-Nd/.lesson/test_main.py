try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
import unittest
from main import *

temps = T
gat_heatcv = np.zeros(len(T))
for i, t in enumerate(temps) : 
   gb = np.exp(-frequencies/t)
   gnb = 1-gb
   gat_sumheatcv = (frequencies*frequencies)/(t*t)*( gb /gnb + gb*gb/(gnb*gnb) )
   gat_heatcv[i] = sum(gat_sumheatcv)/3


line1 = line( temps, gat_heatcv )
axislabels = ['Temperature / natural units', 'Heat capacity per atom / natural units' ]

class UnitTests(unittest.TestCase) :
    def test_heat_capcity(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
