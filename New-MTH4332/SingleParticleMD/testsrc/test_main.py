try:
    from AutoFeedback.funcchecks import check_func
except: 
    import subprocess
    import sys
        
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func
 
import AutoFeedback.plotchecks as pc
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal               
from AutoFeedback.randomclass import randomvar
from AutoFeedback.varchecks import check_vars
import numpy as np
import unittest      

class UnitTests(unittest.TestCase) :
    def test_energy(self) : 
        inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
        for x in xvals : 
            inputs.append((x,))
            outputs.append(x*x/2)
        assert( check_func('potential', inputs, outputs ) ) 

    def test_forces3(self) :
        potential = get_internal("potential")
        inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
        for x in xvals :
            inputs.append((x,))
            mp, crap = potential(x+1E-8)
            op, crap = potential(x)
            outputs.append((op,-(mp-op)/1E-8,))
        assert( check_func('potential', inputs, outputs ) ) 

    def test_potential1(self) :
        inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
        for x in xvals :  
            inputs.append((x,))
            outputs.append((x*x/2,-x,))
        assert( check_func('potential', inputs, outputs ) )  
                
    def test_trajectory1(self) :
        nsteps = get_internal("nsteps")
        timestep, stride = get_internal("timestep"), get_internal("stride")
        p, v, f = get_internal("init_pos"), get_internal("init_vel"), -get_internal("init_pos")
        yvals = np.zeros([int(nsteps/stride)])
        for s in range(nsteps) :
            v = v + 0.5*timestep*f
            p = p + timestep*v
            f = -p
            v = v + 0.5*timestep*f
        
            if s%stride==0 : yvals[int(s/stride)] = p
        
        xv = np.linspace( 0, (nsteps-stride)*timestep, len(yvals) )
        line1 = line( xv, yvals )
        axislabels=["time", "position"]
        assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )

    def test_kinetic3(self) :
        inputs, outputs = [], []
        for i in range(3,10) : 
            for j in range(5) :
                vel, eng = np.zeros(i), 0
                for k in range(i) :  
                    vel[k] = np.random.normal()
                    eng = eng + 0.5*vel[k]*vel[k]
                inputs.append((vel,))
                outputs.append(eng)
        assert( check_func('kinetic', inputs, outputs ) )

    def test_potential2(self) :
       inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
       for x in xvals :
           inputs.append((x,))
           outputs.append((x*x/2,-x,))
       assert( check_func('potential', inputs, outputs ) )
       
    def test_kinetic5(self) :
       inputs, outputs = [], []
       for i in range(100) :
           vel = np.random.normal()
           eng =  0.5*vel*vel
           inputs.append((vel,))
           outputs.append(eng)
       assert( check_func('kinetic', inputs, outputs ) )

    def test_trajectory2(self) :
       nsteps = get_internal("nsteps")
       timestep, stride = get_internal("timestep"), get_internal("stride")
       p, v, f = get_internal("init_pos"), get_internal("init_vel"), -get_internal("init_pos")
       xvals = np.zeros(int(nsteps/stride))
       yvals1 = np.zeros(int(nsteps/stride))
       yvals2 = np.zeros(int(nsteps/stride))
       yvals3 = np.zeros(int(nsteps/stride))
       for s in range(nsteps) :
           v = v + 0.5*timestep*f
           p = p + timestep*v
           f = -p
           v = v + 0.5*timestep*f
       
           if s%stride==0 :
              xvals[int(s/stride)] = s
              yvals1[int(s/stride)] = p*p/2
              yvals2[int(s/stride)] = v*v/2
              yvals3[int(s/stride)] = yvals1[int(s/stride)] + yvals2[int(s/stride)]
       
       line1 = line( xvals, yvals1, label='potential' )
       line2 = line( xvals, yvals2, label='kinetic' )
       line3 = line( xvals, yvals3, label='total' )
       axislabels=["time", "energy"]
       assert( pc.check_plot([line1,line2,line3],explabels=axislabels,explegend=False,output=True) )      

    def test_vel(self) :
        inputs, outputs = [], []
        for T in [0.5,1.0,1.5,2.0,2.5] : 
            inputs.append((T,))
            r = randomvar( 0, variance=T, isinteger=False, nsamples=100 )
            outputs.append(r)
        assert( check_func('gen_vel', inputs, outputs) ) 

    def test_potential3(self) :
       inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
       for x in xvals :
           inputs.append((x,))
           outputs.append((x*x/2,-x,))
       assert( check_func('potential', inputs, outputs ) )

    def test_kinetic9(self) :
       inputs, outputs = [], []
       for i in range(100) :
           vel = np.random.normal()
           eng =  0.5*vel*vel
           inputs.append((vel,))
           outputs.append(eng)
       assert( check_func('kinetic', inputs, outputs ) )

    def test_trajectory3(self):
       nsteps, stride, timestep, temperature = get_internal("nsteps"), get_internal("stride"), get_internal("timestep"), get_internal("temperature")
       xv = np.linspace( 0, (nsteps-stride)*timestep, int(nsteps/stride) )
       var = randomvar( 0, variance=temperature )
       line1 = line( xv, var )
       axislabels=["time", "velocity"]
       assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )
   
    def test_potential4(self) :
       inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
       for x in xvals :
           inputs.append((x,))
           outputs.append((x*x/2,-x,))
       assert( check_func('potential', inputs, outputs ) )

    def test_kinetic8(self) :
       inputs, outputs = [], []
       for i in range(100) :
           vel = np.random.normal()
           eng =  0.5*vel*vel
           inputs.append((vel,))
           outputs.append(eng)
       assert( check_func('kinetic', inputs, outputs ) )

    def test_trajectory4(self):
       conserved_quantity = get_internal("conserved_quantity")
       init_pos, init_vel = get_internal("init_pos"), get_internal("init_vel") 
       nsteps, stride, timestep = get_internal("nsteps"), get_internal("stride"), get_internal("timestep")
       xv = np.linspace( 0, (nsteps-stride)*timestep, len(conserved_quantity) )
       init_eng = 0.5*( init_pos*init_pos + init_vel*init_vel )
       yv = init_eng*np.ones( len(conserved_quantity) )
       line1 = line( xv, yv )
       axislabels=["time", "conserved quantity / energy units"] 
       assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )

    def test_mean(self) : 
        mye = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/energies")[:,1]
        myeng = sum( mye ) / len( mye )
        assert(check_vars("average",myeng))

    def test_energies(self) :
        myeng = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/energies")[:,1]
        xvals = np.linspace( 1, 10, 10 )
        yvals = np.zeros(10)
        for i in range(10) : yvals[i] = sum( myeng[i*100:(i+1)*100] ) / 100
        line1, axislabels  = line(xvals,yvals), ["Index", "Average energy / natural units"]
        assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )

    def test_graph1(self) : 
        myeng = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/energies")[:,1]
        xvals, yvals = np.linspace(1,10,10), np.zeros(10)
        for i in range(10) :
            thisav = sum( myeng[i*100:(i+1)*100] ) / 100
            thisav2 = sum( np.power(myeng[i*100:(i+1)*100],2) ) / 100
            yvals[i] = (100/99)*( thisav2 - thisav*thisav )
        
        N = len( myeng )
        mean = sum( myeng ) / N
        mean2 = sum( np.power(myeng,2) ) / N
        myvar = (N/(N-1))*( mean2 - mean*mean )
        line1, line2 = line(xvals, yvals), line([1,10], [myvar,myvar])
        axislabels = ["Index","Variance / energy^2"]
        assert( pc.check_plot([line1,line2],explabels=axislabels,explegend=False,output=True) )

    def test_average_correct(self) :
        myeng = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/energies")[:,1]
        myblocks, myaverage = 10*[0], 0
        for i in range(10) :
            myblocks[i] = sum( myeng[i*100:(i+1)*100] ) / 100 
            myaverage = myaverage + myblocks[i] 
        assert( check_vars("average", myaverage / 10 ) )
        
    def test_error_correct(self) :
        myeng = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/energies")[:,1]
        myblocks, myaverage, mysq = 10*[0], 0, 0
        for i in range(10) :
            myblocks[i] = sum( myeng[i*100:(i+1)*100] ) / 100 
            myaverage = myaverage + myblocks[i] 
            mysq = mysq + myblocks[i]*myblocks[i]
  
        mysq, myaverage = mysq / 10, myaverage / 10
        myvar = ( 10 / 9 )*( mysq - myaverage*myaverage )
        assert( check_vars("error", np.sqrt( myvar / 10 ) ) )

    def test_blockVals(self) :
        myeng = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/energies")[:,1]
        inputs, outputs = [], []
        for bb in [10,20,30,40,60,100,120,200,300,400] : 
            nblocks = int( len( myeng ) / bb )
            myaverage, mysq = 0, 0
            for i in range(nblocks) :
                myblocks = sum( myeng[i*bb:(i+1)*bb] ) / bb
                myaverage = myaverage + myblocks
                mysq = mysq + myblocks*myblocks

            mysq, myaverage = mysq / nblocks, myaverage / nblocks
            myvar = ( nblocks / (nblocks - 1) )*( mysq - myaverage*myaverage )
            inputs.append((bb,myeng,))
            outputs.append( np.sqrt( myvar / nblocks )  )
        assert( check_func('block_average',inputs,outputs ) )

    def test_plot(self):
       myeng = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/energies")[:,1]
       xvals, yvals = [10,20,30,40,60,100,120,200,300,400], np.zeros(10)
       for bb in xvals :
           nblocks = int( len( eng ) / bb )
           myaverage, mysq = 0, 0
           for i in range(nblocks) :
               myblocks = sum( myeng[i*bb:(i+1)*bb] ) / bb
               myaverage = myaverage + myblocks
               mysq = mysq + myblocks*myblocks
       
           mysq, myaverage = mysq / nblocks, myaverage / nblocks
           myvar = ( nblocks / (nblocks - 1) )*( mysq - myaverage*myaverage )
           yvals[k] = np.sqrt( myvar / nblocks )
       
       line1 = line(xvals,yvals)
       axislabels=["Size of blocks", "Error"] 
       assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )

    def test_block_averages1(self) :
        # Do the block averaging
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        correct_average, correct_error = np.zeros(len(this_x)), np.zeros(len(this_x))
        for k, block in enumerate(this_x) :
            blocksize = int( block )
            # Your code to calculate the block averages goes here
            nblocks, average, error = int( len(total) / blocksize ), 0, 0
            for j in range(nblocks) :
                av = sum( total[j*blocksize:(j+1)*blocksize] ) / blocksize
                average = average + av
                error = error + av*av
            correct_average[k] = average / nblocks
            correct_error[k] = (nblocks / (nblocks-1))*( error / nblocks - average*average )*np.sqrt( error / nblocks )*st.norm.ppf(0.95)
        
        line1 = line( this_x, correct_average )
        axislabels = ["Length of block", "Average energy / natural units"]
        pc.check_plot([line1], explabels=axislabels)

    def test_block_errors1(self) :
         assert( check_vars( 'errros', correct_error ) )
         
    def test_conserved1(self) :
         init_eng = 0.5*( init_pos*init_pos + init_vel*init_vel )
         cc = init_eng*np.ones( len(conserved) )
         assert( check_vars('conserved', cc ) ) 
             
    def test_kinetic1(self) :
         inputs, outputs = [], []
         for i in range(100) :
            vel = np.random.normal()
            eng =  0.5*vel*vel
            inputs.append((vel,))
            outputs.append(eng)
         assert( check_func('kinetic', inputs, outputs ) )
            
    def test_forces1(self) : 
         inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
         for x in xvals :
             inputs.append((x,))
             outputs.append((x*x/2,-x,))
         assert( check_func('potential', inputs, outputs ) )

    def test_block_averages2(self) :
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
         pc.check_plot([line1], explabels=axislabels)

    def test_block_errors2(self) :
         assert( check_vars( 'errros', correct_error ) )
         
    def test_conserved2(self) :
         init_eng = 0.5*( init_pos*init_pos + init_vel*init_vel )
         cc = init_eng*np.ones( len(conserved) )
         assert( check_vars('conserved', cc ) ) 
             
    def test_kinetic2(self) :
         inputs, outputs = [], []
         for i in range(100) :
            vel = np.random.normal()
            eng =  0.5*vel*vel
            inputs.append((vel,))
            outputs.append(eng)
         assert( check_func('kinetic', inputs, outputs ) )
            
    def test_forces2(self) : 
         inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
         for x in xvals :
             inputs.append((x,))
             outputs.append((x*x/2,-x,))
         assert( check_func('potential', inputs, outputs ) )
  
    def test_graph3(self) :
         filedata = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/md_results.txt")
         tmid, cvmid = np.zeros(len(filedata)-1), np.zeros(len(filedata)-1)
         for i in range(len(filedata)-1) :
             tmid[i] = (filedata[i,0] + filedata[i+1,0] ) / 2
             cvmid[i] = (filedata[i+1,1] - filedata[i,1]) / (filedata[i+1,0] - filedata[i,0])
         
         line1 = line( tmid, cvmid )
         axislabels = ["temperature / natural units", "heat capacity / natural units"]
         assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )

    def test_graph4(self) :
         filedata = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/md_results.txt")
         tmid, cvmid = np.zeros(len(filedata)-1), np.zeros(len(filedata)-1)
         for i in range(len(filedata)-1) :
             tmid[i] = (filedata[i,0] + filedata[i+1,0] ) / 2
             cvmid[i] = (filedata[i+1,1] - filedata[i,1]) / (filedata[i+1,0] - filedata[i,0])
         
         line1 = line( tmid, cvmid )
         axislabels = ["temperature / natural units", "heat capacity / natural units"]
         assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )

    def test_errors1( self ) :
         err = np.zeros(len(filedata)-1)
         for i in range(len(filedata)-1) :
             err[i] = ( filedata[i+1,2] + filedata[i,2] ) / ( filedata[i+1,0] - filedata[i,0] )
         assert( check_vars( "cv_errors", err ) ) 

    def test_graph5(self) :
         filedata = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/md_results.txt")
         cvmid = np.zeros(len(filedata))
         for i in range(len(filedata)) :
             cvmid[i] = (filedata[i,3] - filedata[i,1]*filedata[i,1]) / (filedata[i,0]*filedata[i,0])
         
         line1 = line( filedata[:,0], cvmid )
         axislabels = ["temperature / natural units", "heat capacity / natural units"] 
         assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )

    def test_graph6(self) :
         filedata = np.loadtxt("https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/SingleParticleMD/md_results.txt")
         cvmid = np.zeros(len(filedata))
         for i in range(len(filedata)) :
             cvmid[i] = (filedata[i,3] - filedata[i,1]*filedata[i,1]) / (filedata[i,0]*filedata[i,0])
         
         line1 = line( filedata[:,0], cvmid )
         axislabels = ["temperature / natural units", "heat capacity / natural units"] 
         assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )

    def test_errors2( self ) :
         err = np.zeros(len(filedata))
         for i in range(len(filedata)) :
             err[i] = ( filedata[i,4] + 2*filedata[i,1]*filedata[i,2] ) / ( filedata[i,0]*filedata[i,0] )
         assert( check_vars( "cv_errors", err ) ) 

    def test_cv( self ) :
         assert( check_vars( "CV", sy.Rational(3,4) ) )
