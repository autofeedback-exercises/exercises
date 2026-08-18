from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal as get
from AutoFeedback.randomclass import randomvar
import itertools
import numpy as np
import unittest
import inspect
import ast

class UnitTests(unittest.TestCase):
    def test_ex1(self):
        inputs, outputs = [], []
        for i in range(2,10) : 
            for j in range(3): 
                a = np.random.uniform(-1,1,size=i)
                b = np.random.uniform(-1,1,size=i)
                dp = np.dot(a,b)
                inputs.append((a,b,))
                outputs.append(dp)
        assert check_func("dot_product_1", inputs, outputs )

    def test_ex2(self):
        inputs, outputs = [], []
        for i in range(2,10) : 
            for j in range(3): 
                a = np.random.uniform(-1,1,size=i)
                b = np.random.uniform(-1,1,size=i)
                dp = np.dot(a,b)
                inputs.append((a,b,))
                outputs.append(dp)
        assert check_func("dot_product_2", inputs, outputs )

    def test_ex3(self):
        #calls = []
        #for c in ast.walk(ast.parse(inspect.getsource("dot_product_3"))):
        #    if isinstance(c, ast.Call): calls.append([c.func.value.id, c.func.attr])
        #assert ["np","dot"] in calls
        inputs, outputs = [], []
        for i in range(2,10) : 
            for j in range(3): 
                a = np.random.uniform(-1,1,size=i)
                b = np.random.uniform(-1,1,size=i)
                dp = np.dot(a,b)
                inputs.append((a,b,))
                outputs.append(dp)
        assert check_func("dot_product_3", inputs, outputs )

    def test_ex4(self):
        inputs, outputs = [], []
        for i in range(2,10) :
            for j in range(2,10) :
                a = np.random.uniform(-1,1,size=i)
                b = np.random.uniform(-1,1,size=j)
                out = np.outer(a,b)
                inputs.append((a,b,))
                outputs.append(out)
        assert check_func("outer_product_1", inputs, outputs )

    def test_ex5(self):
        inputs, outputs = [], []
        for i in range(2,10) :
            a = np.random.uniform(-1,1,size=i) 
            inputs.append((a,))
            outputs.append(np.fabs(np.subtract.outer(a,a))) 
        assert check_func("distance_matrix", inputs, outputs ) # calls=['np.subtract.outer'] ) 

    def test_ex6(self):
        inputs, outputs = [], []
        for i in range(2,10) :
            for j in range(2,10) :
                a = np.random.uniform(-1,1,size=[i,j])
                b = np.random.uniform(-1,1,size=j)
                inputs.append((a,b,))
                outputs.append( np.matmul(a,b) )
        assert check_func("matvec_mult", inputs, outputs )

    def test_ex7(self):
        inputs, outputs = [], []
        for r in [0.5,0.75,1.0,1,25,1.5,1.75] : 
            for i in range(100,600,100) :
                x = np.random.uniform(-1,1,size=i)
                d = np.fabs(np.subtract.outer(x,x))
                c = np.where(d<r, 1, 0)
                fn = np.matmul( c, np.ones(i) ) / i 
                inputs.append((x,r,))
                outputs.append(np.mean(fn))
        assert check_func("cumdist_estimate", inputs, outputs, calls=['distance_matrix'] ) # calls=['np.where','np.matmul'] ) 

    def test_ex8(self):
        inputs, outputs = [], []
        for i in range(2,10) :
            for j in range(2,10) :
                for k in range(2,10) : 
                    a = np.random.uniform(-1,1,size=[i,k])
                    b = np.random.uniform(-1,1,size=[k,j])
                    inputs.append((a,b,))
                    outputs.append(np.matmul(a,b))
        assert check_func("matrix_multiplication", inputs, outputs )

    def test_ex9(self):
        inputs, outputs = [], []
        for i in range(100,600,100) : 
            for j in range(2,6) :
                a = np.random.uniform(-1,1,size=[j,i])
                inputs.append((a,))
                outputs.append( np.matmul(a.T,a) )
        assert check_func("all_dot_products", inputs, outputs )

    def test_ex10(self):
        inputs, outputs = [], []
        for i in range(100,600,100) : 
            for j in range(2,6) :
                x = np.random.uniform(-1,1,size=[j,i])
                x2 = x*x
                mod = np.sqrt( np.matmul( x2.T, np.ones(j) ) )
                inputs.append((x,))
                outputs.append( np.acos( np.matmul( x.T, x ) / np.outer( mod, mod ) ) )
        assert check_func("all_angles", inputs, outputs ) #, calls=['np.matmul', 'np.outer'] ) 

    def test_ex11(self):
        inputs, outputs = [], []
        for i in range(100,600,100) :
            for j in range(2,6) :
                x = np.random.uniform(-1,1,size=[j,i])
                x2 = x*x
                mod = np.matmul( x2.T, np.ones(j) ) 
                inputs.append((x,))
                outputs.append( np.sqrt( np.add.outer( mod,mod) - 2*np.matmul( x.T, x ) ) )
        assert check_func("distance_matrix_nd", inputs, outputs ) #, calls=['np.matmul', 'np.add.outer'] )

    def test_ex12a(self):
        inputs, outputs = [], []
        for i in range(3,10) : 
            myset = set( np.linspace(1,i,i) )
            inputs.append((myset,))
            outputs.append(set( itertools.combinations(myset, 2 )))
        assert check_func("bounded_power_set_2", inputs, outputs )

    def test_ex12b(self):
        inputs, outputs = [], []
        for i in range(3,10) :
            myset = set( np.linspace(1,i,i) )
            inputs.append((myset,))
            outputs.append(set( itertools.combinations(myset, 3 )))
        assert check_func("bounded_power_set_3", inputs, outputs )

    def test_ex12c(self):
        inputs, outputs = [], []
        for i in range(3,10) :
            myset = set( np.linspace(1,i,i) )
            inputs.append((myset,))
            outputs.append(set( itertools.combinations(myset, 4 )))
        assert check_func("bounded_power_set_4", inputs, outputs )

    def test_ex13(self):
        inputs, outputs = [], []
        for i in range(10,60,10) : 
            x = np.random.uniform(-1,1,size=[2,i])
            inputs.append((x,))
            outputs.append( np.array(list(itertools.combinations( x.T, 3 ))) )
        assert check_func("get_all_sets_of_three_vectors", inputs, outputs ) #, calls=['itertools.combinations'] )
    
    def test_ex14(self):
        inputs, outputs = [], []
        for i in range(10,60,10) : 
            x = np.random.uniform(-1,1,size=[2,i])
            inputs.append((x,))
            corners = np.array(list(itertools.combinations( x.T, 3 )))
            edges = np.transpose( np.array( [corners[:,1,:]-corners[:,0,:],corners[:,2,:]-corners[:,0,:]], axes=[1,0,2] ) )
            outputs.append( 0.5*np.abs( np.linalg.det( edges ) ) ) 

        assert check_func("get_all_sets_of_three_vectors", inputs, outputs, calls=['get_all_sets_of_three_vectors'] ) # calls=["np.linalg.det"] )  
