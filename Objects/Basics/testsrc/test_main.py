from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal as get
from AutoFeedback.randomclass import randomvar
import sympy
import itertools
import numpy as np
import unittest

class UnitTests(unittest.TestCase):
    def test_ex1(self):
        inputs, outputs = [], []
        for i in range(2,10) : 
            a = list(range(i))
            inputs.append((a,i,))
            inputs.append((a,1,))
            a1 = set(a.copy())
            a1.add(i)
            a2 = set(a.copy())
            a2.add(1)
            outputs.append(list(a1))
            outputs.append(list(a2))
        assert check_func("add_element", inputs, outputs )

    def test_ex2(self):
        inputs, outputs = [], []
        for i in range(2,10) : 
            a = tuple( np.random.randint(0,i, size=2*i, dtype=int) )
            inputs.append((a,))
            outputs.append( list(set(a)) )
        assert check_func("tuple_to_set", inputs, outputs )

    def test_ex3(self):
        inputs, outputs = [], []
        for i in range(2,5) : 
            lista = list( range(i) )
            seta = set(lista)
            for j in range(i+1,i+5) : 
                listb = list( range(i,j) )
                setb = set(listb)
                inputs.append((lista,listb,))
                outputs.append(list(seta.union(setb)))
                listb = list( range(j) )
                setb = set(listb)
                inputs.append((lista,listb,))
                outputs.append(list(seta.union(setb))) 
        assert check_func("set_union", inputs, outputs )

    def test_ex4(self):
        inputs, outputs = [], []
        for i in range(2,5) :
            lista = list( range(i) )
            seta = set(lista)  
            for j in range(i+1,i+5) :
                listb = list( range(i,j) )
                setb = set(listb)
                inputs.append((lista,listb,))
                outputs.append(list(seta.intersection(setb)))
                listb = list( range(j) )
                setb = set(listb) 
                inputs.append((lista,listb,))
                outputs.append(list(seta.intersection(setb)))
        assert check_func("set_intersection", inputs, outputs ) 

    def test_ex5(self):
        inputs, outputs = [], []
        inputs, outputs = [], []
        for i in range(2,5) :
            lista = list( range(i) )
            seta = set(lista)  
            for j in range(i+1,i+5) :
                listb = list( range(i,j) )
                setb = set(listb) 
                inputs.append((lista,listb,))
                outputs.append(list(seta.difference(setb)))
                inputs.append((listb,lista,))
                outputs.append(list(setb.difference(seta)))
                listb = list( range(j) )
                setb = set(listb)
                inputs.append((lista,listb,))
                outputs.append(list(seta.difference(setb)))
                inputs.append((listb,lista,))
                outputs.append(list(setb.difference(seta))) 
        assert check_func("set_difference", inputs, outputs )  

    def test_ex6(self):
        inputs, outputs = [], []
        for i in range(2,10) :
            for j in range(5) :  
                seta = set( range(i) )
                setb = set( np.random.randint( 0, i, size=2*i, dtype=int ) )
                inputs.append((seta,setb,))
                outputs.append(seta==setb)
        assert check_func("check_equality_of_sets", inputs, outputs )
                 

    def test_ex7a(self):
        inputs, outputs = [], []
        for i in range(2,6) :
            seta = set(range(i)) 
            for j in range(2,6) :
                setb = set(range(j))
                inputs.append((seta,setb,))
                outputs.append(set(itertools.product(seta,setb)))
        assert check_func("cartesian_product_2", inputs, outputs )


    def test_ex7b(self):
        inputs, outputs = [], []
        for i in range(2,6) :  
            seta = set(range(i))
            for j in range(2,6) :
                setb = set(range(j))
                for k in range(2,6) : 
                    setc = set(range(k))
                    inputs.append((seta,setb,setc,))
                    outputs.append(set(itertools.product(seta,setb,setc)))
        assert check_func("cartesian_product_3", inputs, outputs )

    def test_ex8(self):
        inputs, outputs = [], []
        for i in range(2,10) :
            a = np.random.uniform(-1,1,size=i)
            b = np.random.uniform(-1,1,size=i)
            inputs.append((list(a),list(b),))
            outputs.append(list(a+b))
        assert check_func("vector_addition", inputs, outputs )

    def test_ex9(self):
        inputs, outputs = [], []
        for i in range(2,10) :
            a = np.random.uniform(-1,1,size=i)
            b = np.random.uniform(-1,1)
            inputs.append((list(a), b,))
            outputs.append(list(a*b))
        assert check_func("vector_times_scalar", inputs, outputs )

    def test_ex10(self):
        inputs, outputs = [], []
        for i in range(2,10) :
            a = np.random.uniform(-1,1,size=i)
            b = np.random.uniform(-1,1,size=i)
            inputs.append((list(a),list(b),))
            outputs.append(list(a*b))
        assert check_func("array_product", inputs, outputs )

    def test_ex11a(self):
        inputs, outputs = [], []
        for i in range(20) : 
            a = np.random.uniform(-1,1, size=2)
            b = np.random.uniform(-1,1, size=2)
            inputs.append((a,b,))
            outputs.append(a+b)
        assert check_func("complex_number_add", inputs, outputs )

    def test_ex11b(self):
        inputs, outputs = [], []
        for i in range(20) : 
            a = np.random.uniform(-1,1, size=2)
            b = np.random.uniform(-1,1, size=2)
            inputs.append((a,b,))
            ac = complex(a[0],a[1])
            bc = complex(b[0],b[1])
            pc = ac*bc
            outputs.append(np.array([pc.real, pc.imag]))
        assert check_func("complex_number_multiply", inputs, outputs )

    def test_ex11c(self):
        inputs, outputs = [], []
        for i in range(20) :
            a = np.random.uniform(-1,1, size=2)
            inputs.append((a,))
            outputs.append(np.array([a[0],-a[1]]))

        assert check_func("complex_conjugate", inputs, outputs )

    def test_ex11d(self):
        inputs, outputs = [], []
        for i in range(20) :
            a = np.random.uniform(-1,1, size=2)
            inputs.append((a,))
            outputs.append(np.sqrt(a[0]*a[0]+a[1]*a[1]))
        assert check_func("modulus", inputs, outputs )

    def test_ex11e(self):
        inputs, outputs = [], []
        for i in range(20) :
            a = np.random.uniform(-1,1, size=2)
            b = np.random.uniform(-1,1, size=2)
            inputs.append((a,b,))
            ac = complex(a[0],a[1])
            bc = complex(b[0],b[1])
            pc = ac/bc
            outputs.append(np.array([pc.real, pc.imag]))
        assert check_func("complex_division", inputs, outputs )

    def test_ex12(self):
        inputs, outputs = [], []
        z = sympy.symbols("z")
        for r in [1,2,3,4] : 
            for i in range(1,4) :
                inputs.append((i,r,))
                eq = sympy.Eq(z**i-r, 0 )
                outputs.append( sympy.solve( eq, z ) ) 
        assert check_func("solve_basic_poly", inputs, outputs )

    def test_ex13(self):
        inputs, outputs = [], []
        z = sympy.symbols("z")
        eq = sympy.Eq(z**8-1, 0 )
        sol = sympy.solve( eq, z )
        real, imag = sol.copy(), sol.copy()
        for i in range(len(sol)):
            real[i] = sympy.re(sol[i])
            imag[i] = sympy.im(sol[i]) 
        line1 = line( real, imag )
        axislabels = ["real part", "imaginary part"]
        assert check_plot( [line1], explabels=axislabels, explegend=False, output=True) 

    def test_ex14(self):
        inputs, outputs = [], []
        out, z = set(), sympy.symbols("z")
        for i in range(1,21) :
            inputs.append((i,))
            eq = sympy.Eq(z**i-1, 0 )
            for s in sympy.solve( eq, z ) : 
                out.add(s)
            outputs.append( set(out.copy()) )
        assert check_func("set_of_solutions", inputs, outputs, calls="solve_basic_poly" )

    def test_ex15(self):
        inputs, outputs = [], []
        out, z = {}, sympy.symbols("z")
        for i in range(1,21) :
            inputs.append((i,))
            eq = sympy.Eq(z**i-1, 0 ) 
            for s in sympy.solve( eq, z ) : 
                if s in out.keys() : 
                   out[s] = out[s] + 1
                else :
                   out[s] = 1
            outputs.append( out.copy() )
        assert check_func("dictionary_of_solutions", inputs, outputs, calls="solve_basic_poly" ) 

    def test_ex16(self):
        z = sympy.symbols("z") 
        inputs, outputs = [], []
        for maxn in range(2,20) :
            bihisto = np.zeros([maxn,maxn])
            for i in range(1,maxn+1) :
              eqi = sympy.Eq(z**i-1, 0 )
              iroots = set(sympy.solve( eqi, z ))
              for j in range(1,maxn+1) :
                eqj = sympy.Eq(z**j-1, 0 )
                bihisto[i-1,j-1] = len( iroots.intersection(set(sympy.solve(eqj,z)) )
        inputs.append((maxn,))
        outputs.append(bihisto)
        assert check_func("get_array_of_shared_roots", inputs, outputs, calls="solve_basic_poly" )
