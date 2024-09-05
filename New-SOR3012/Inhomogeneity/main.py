import matplotlib.pyplot as plt
import numpy as np
class Poisson : 
    def __init__(self, lamd) : 
        self.lamd = lamd
        self.clock = 0
    def advance_time(self) :
        self.clock = self.clock + self.generate_interarrival()
    def generate_interarrival(self) :
        return -np.log( np.random.uniform(0,1) ) / self.lamd
# This is my code for generating the graph -- you don't need to modify this
lamd, nevents = 2, 100
times, number, g = np.zeros(nevents), np.linspace(1,nevents,nevents), Poisson(lamd)
for i in range(nevents) : 
    g.advance_time()
    times[i] = g.clock
plt.plot( times, number, 'ko' )
plt.xlabel("Time / s")
plt.ylabel("Number of events")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

class GeneralPoisson : 
    def __init__(self) : 
        self.clock = 0
    def advance_time(self) :
        self.clock = self.clock + self.generate_interarrival()
    def generate_interarrival(self) :
        return np.random.normal(4,1) 
# This is my code for generating the graph -- you don't need to modify this
nevents = 100
times, number, g = np.zeros(nevents), np.linspace(1,nevents,nevents), GeneralPoisson()
for i in range(nevents) : 
    g.advance_time()
    times[i] = g.clock
plt.plot( times, number, 'ko' )
plt.xlabel("Time / s")
plt.ylabel("Number of events")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

def rate(t) :
    tp = t - np.floor(t/600)*600 
    if tp<60 : return 0.5
    if tp<180 : return 1/6 
    if tp<240 : return 0.5 
    if tp<360 : return 1/6
    if tp<420 : return 0.5
    if tp<540 : return 1/6
    return 0.5

def rate(t) :
    return (1/6)*np.cos( (t - 30 ) * (2*np.pi / 180 ) ) + 1/3 

class InhomogenousPoisson : 
    def __init__(self) : 
        self.clock = 0
    def rate(self,t) :
        return np.sin(t) + 2
    def advance_time(self) :
        self.clock = self.clock + self.generate_interarrival()
    def generate_interarrival(self) :
        newtime = self.clock
        while True : 
          newtime = newtime + self.exponential_rv(3.0)
          if np.random.uniform(0,1) <= self.rate(newtime)/3.0 : break
        return newtime - self.clock
    def exponential_rv(self, lamd) :
        return -np.log( np.random.uniform(0,1) ) / lamd   
# This is my code for generating the graph -- you don't need to modify this
nevents = 100
times, number, g = np.zeros(nevents), np.linspace(1,nevents,nevents), InhomogenousPoisson()
for i in range(nevents) : 
    g.advance_time()
    times[i] = g.clock
plt.plot( times, number, 'ko' )
plt.xlabel("Time / s")
plt.ylabel("Number of events")
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()
