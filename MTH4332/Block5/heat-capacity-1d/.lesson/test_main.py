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
gb = np.exp(-frequency/temps)
gnb = 1-gb
gat_heatcv = (frequency*frequency)/(temps*temps)*( gb /gnb + gb*gb/(gnb*gnb) )

line1 = line( temps, gat_heatcv )
axislabels = ['Temperature / natural units', 'Heat capacity / natural units' ]

class UnitTests(unittest.TestCase) :
    def test_heat_capcity(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
