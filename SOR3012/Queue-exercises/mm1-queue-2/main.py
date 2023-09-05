import matplotlib.pyplot as plt
import numpy as np

# These are the parameters of the queue that you should use.  If you change the values
# of these parameters you will fail the test as I have set up the test this way.  In 
# writing your project you can change them but you should always ensure that lam<expr
lam, expr = 0.5, 1.0
# This is the number of people who you should model entering your queue
# Once again you adjust this value in your project.  You must set this value to 100000 to pass
# the test, however
N = 100000

# Use this to hold the times when the queue changes length as is discussed in the text
events = []
# Add code here to simulate the queue and to determine the distribution of lengths
