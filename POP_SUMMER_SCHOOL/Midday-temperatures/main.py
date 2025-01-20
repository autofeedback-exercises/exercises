import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def multiply(a, b) :
  return a*b

def modulo( a ) :
  if a<0 : return a*-1
  return a

def moon_temperature(d) :
  LH = (1-0.12)*1361/(d*d) 
  T4 = LH / (0.98*5.67E-8)
  return T4**(1/4)

def planet_temperature(e,a,d) :
  LH = (1-a)*1361/(d*d)
  T4 = LH / (e*5.67E-8)
  return T4**(1/4)  
