try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal
import unittest

def mylj(r) :
    r2 = r*r
    r6 = r2*r2*r2
    r12 = r6*r6
    eng = 4*( ( 1/r12 ) - (1/r6) )
    force = -24*( 2/r12 - 1/r6 ) / r2
    return eng, force

class UnitTests(unittest.TestCase) :
    def test_heat_capcity3(self) :
        temps = get_internal("T")
        frequency = get_internal("frequency")
        gb = np.exp(-frequency/temps)
        gnb = 1-gb
        gat_heatcv = (frequency*frequency)/(temps*temps)*( gb /gnb + gb*gb/(gnb*gnb) )
        
        line1 = line( temps, gat_heatcv )
        axislabels = ['Temperature / natural units', 'Heat capacity / natural units' ]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
