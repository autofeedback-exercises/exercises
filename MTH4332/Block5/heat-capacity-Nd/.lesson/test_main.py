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

class UnitTests(unittest.TestCase) :
    def test_heat_capcity4(self) :
        temps = get_internal("T")
        frequency = get_internal("frequency")
        gat_heatcv = np.zeros(len(temps))
        for i, t in enumerate(temps) :
           gb = np.exp(-frequencies/t)
           gnb = 1-gb
           gat_sumheatcv = (frequencies*frequencies)/(t*t)*( gb /gnb + gb*gb/(gnb*gnb) )
           gat_heatcv[i] = sum(gat_sumheatcv)/3
        
        line1 = line( temps, gat_heatcv )
        axislabels = ['Temperature / natural units', 'Heat capacity per atom / natural units' ]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
