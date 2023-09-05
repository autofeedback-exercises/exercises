try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func 
           
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

def simulate( s, n, p ) :
    ngoes = 0
    while ( s>0 and s<n ) :
       ngoes = ngoes + 1
       if np.random.uniform(0,1)<p : s = s + 1
       else : s = s - 1 
    return ngoes

def get_var( s, n, p ) :
    myvar = simulate(s,n,p)
    S, S2 = myvar, myvar*myvar 
    for i in range(1,200) : 
        myvar = simulate(s,n,p)
        S, S2 = S + myvar, S2 + myvar*myvar
    mean = S / 200
    return ( 200 / 199 ) * ( S2/200 - mean*mean ) 

class UnitTests(unittest.TestCase) :
    def test_gambler(self) : 
        inputs, variables = [], []
        for s in range(1,4) : 
            for n in range(6,8) :
                for i in range(1,5) :
                    p = i*0.2
                    inputs.append((s,n,p,))
                    rat = (1-p)/p
                    exp = s/(1-2*p) - ( n/(1-2*p) ) * ( 1 - rat**s ) / ( 1 - rat**n )
                    testvar = get_var( s, n, p )  # It would be nice to have an exact value here
                    myvar = randomvar( exp, variance=testvar, vmin=1, isinteger=True )
                    variables.append( myvar )
        assert( check_func('nplays',inputs, variables ) )
