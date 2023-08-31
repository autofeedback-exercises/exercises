try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

import AutoFeedback.plotchecks as pc
from AutoFeedback import check_vars
from AutoFeedback.randomclass import randomvar
from AutoFeedback.plotclass import line
import unittest
from main import *

# Do the block averaging
fighand=plt.gca()
figdat = fighand.get_lines()[0].get_xydata()
this_x, this_y = zip(*figdat) 
ftotal_sq, correct_average, correct_error = total*total, np.zeros(len(this_x)), np.zeros(len(this_x))
for k, block in enumerate(this_x) :
    blocksize = int( block )
    # Your code to calculate the block averages goes here
    nblocks, average, error = int( len(ftotal_sq) / blocksize ), 0, 0
    for j in range(nblocks) : 
        av = sum( ftotal_sq[j*blocksize:(j+1)*blocksize] ) / blocksize
        average = average + av 
        error = error + av*av 
    correct_average[k] = average / nblocks
    correct_error[k] = (nblocks / (nblocks-1))*( error / nblocks - average*average )*np.sqrt( error / nblocks )*st.norm.ppf(0.95)

line1 = line( this_x, correct_average )
axislabels = ["Length of block", "Average squared energy"]

class UnitTests(unittest.TestCase) :
    def test_block_averages(self) :
        pc.check_plot([line1], explabels=axislabels)

    def test_block_errors(self) :
        check_vars( 'errros', correct_error )
        
    def test_conserved(self) :
        init_eng = 0.5*( init_pos*init_pos + init_vel*init_vel )
        cc = init_eng*np.ones( len(conserved) )
        assert( check_vars('conserved', cc ) ) 
            
    def test_kinetic(self) :
        inputs, outputs = [], []
        for i in range(100) :
           vel = np.random.normal()
           eng =  0.5*vel*vel
           inputs.append((vel,))
           outputs.append(eng)
        assert( check_func('kinetic', inputs, outputs ) )
           
    def test_forces(self) : 
        inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
        for x in xvals :
            inputs.append((x,))
            outputs.append((x*x/2,-x,))
        assert( check_func('potential', inputs, outputs ) )
  
