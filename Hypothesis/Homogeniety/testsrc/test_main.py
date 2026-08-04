from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal as get
from AutoFeedback.randomclass import randomvar
import scipy.stats
import numpy as np
import unittest

class UnitTests(unittest.TestCase):
    def test_ex1(self):
        inputs, output = [], []
        for n in range(2,8) : 
            for j in range(2) :
                # This code generates a random probability distribution 
                a = np.concatenate( (np.random.choice(np.arange(1,n), size=n-1),np.array([0, n])) )
                a = np.sort(a)
                probs = np.zeros(n)
                for i in range(n) : probs[i] = ( a[i+1] - a[i] ) / n 
                # Now we create a sample from this distribution
                sample = np.random.choice( n, p=probs, size=200 )
                inputs.append((sample,))
                # Make a histogram
                histo = np.zeros(n) 
                for s in sample : 
                    histo[int(s)] = histo[int(s)] + 1
                output.append(histo)
        assert( check_func("histo", inputs, output ) )

    def test_ex2(self):
        inputs, output = [], []
        for n in range(2,8) : 
            for j in range(2) :
                for m in range(2,4) :
                    all_sample, table = np.zeros([200,m]),np.zeros([m,n])
                    for k in range(m) :
                        # This code generates a random probability distribution 
                        a = np.concatenate( (np.random.choice(np.arange(1,n), size=n-1),np.array([0, n])) )
                        a = np.sort(a)
                        probs = np.zeros(n)
                        for i in range(n) : probs[i] = ( a[i+1] - a[i] ) / n 
                        # Now we create a sample from this distribution
                        all_sample[:,k] = np.random.choice( n, p=probs, size=200 )
                        inputs.append((sample,))
                        # Make a histogram
                        histo = np.zeros(n) 
                        for s in all_sample[:,k] : 
                            table[k,int(s)] = table[k,int(s)] + 1
                    inputs.append((all_sample,))
                    output.append(table)
        assert( check_func("contingency_table", inputs, output ) )

    def test_ex3(self):
        inputs, output = [], []
        for n in range(2,8) :
            for j in range(2) :
                for m in range(2,4) :
                    all_sample, table = np.zeros([200,m]),np.zeros([m,n])
                    for k in range(m) :
                        # This code generates a random probability distribution 
                        a = np.concatenate( (np.random.choice(np.arange(1,n), size=n-1),np.array([0, n])) )
                        a = np.sort(a)
                        probs = np.zeros(n)
                        for i in range(n) : probs[i] = ( a[i+1] - a[i] ) / n
                        # Now we create a sample from this distribution
                        all_sample[:,k] = np.random.choice( n, p=probs, size=200 )
                        inputs.append((sample,))
                        # Make a histogram
                        histo = np.zeros(n)
                        for s in all_sample[:,k] :
                            table[k,int(s)] = table[k,int(s)] + 1
                    inputs.append((table,))
                    colsums = np.sum( table, axis=1 )
                    rowsums = np.sum( table, axis=0 )
                    output.append( np.outer(colsums,rowsums)/np.sum(table) )
        assert( check_func("expectation", inputs, output ) ) 

    def test_ex4(self):
        inputs, output = [], []
        for n in range(2,8) :
            for j in range(2) :
                for m in range(2,4) :
                    all_sample, table = np.zeros([200,m]),np.zeros([m,n])
                    for k in range(m) :
                        # This code generates a random probability distribution 
                        a = np.concatenate( (np.random.choice(np.arange(1,n), size=n-1),np.array([0, n])) )
                        a = np.sort(a)
                        probs = np.zeros(n)
                        for i in range(n) : probs[i] = ( a[i+1] - a[i] ) / n
                        # Now we create a sample from this distribution
                        all_sample[:,k] = np.random.choice( n, p=probs, size=200 )
                        inputs.append((sample,))
                        # Make a histogram
                        histo = np.zeros(n)
                        for s in all_sample[:,k] :
                            table[k,int(s)] = table[k,int(s)] + 1  
                    inputs.append((all_sample,))
                    colsums = np.sum( table, axis=1 )
                    rowsums = np.sum( table, axis=0 )
                    expect = np.outer(colsums,rowsums)/np.sum(table)
                    test_mat = np.divide( (table - expect)**2,  expect, out=np.zeros_like(expect), where=expect!=0 )
                    output.append( np.sum(test_mat) )
        assert( check_func("teststat", inputs, output ) ) 

    def test_ex5(self):
        inputs, output = [], []
        for n in range(2,8) :
            for j in range(2) :
                for m in range(2,4) :
                    all_sample, table = np.zeros([200,m]),np.zeros([m,n])
                    for k in range(m) :
                        # This code generates a random probability distribution 
                        a = np.concatenate( (np.random.choice(np.arange(1,n), size=n-1),np.array([0, n])) )
                        a = np.sort(a)
                        probs = np.zeros(n)
                        for i in range(n) : probs[i] = ( a[i+1] - a[i] ) / n
                        # Now we create a sample from this distribution
                        all_sample[:,k] = np.random.choice( n, p=probs, size=200 )
                        inputs.append((sample,))
                        # Make a histogram
                        histo = np.zeros(n)
                        for s in all_sample[:,k] :
                            table[k,int(s)] = table[k,int(s)] + 1
                    inputs.append((all_sample,))
                    colsums = np.sum( table, axis=1 )
                    rowsums = np.sum( table, axis=0 )
                    expect = np.outer(colsums,rowsums)/np.sum(table)
                    test_mat = np.divide( (table - expect)**2,  expect, out=np.zeros_like(expect), where=expect!=0 )
                    output.append( 1-scipy.stats.norm.chi2.cdf( np.sum(test_mat), (n-1)*(m-1) ) )
        assert( check_func("pvalue", inputs, output ) )  
 
