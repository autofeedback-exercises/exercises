import matplotlib.pyplot as plt
import numpy as np
def exponential(lam):
  # Your code to generate an exponential random variable goes here
  return -np.log( np.random.uniform(0,1) ) / lam  

lamd = 2      # The parameter for the exponential random variable you should sample
xmax = 6     # The maximum value for x that you should use in your histogram
nbins = 200   # The number of bins you should use for your histogram
histo = np.zeros(nbins)     # The variable you should use to store the histogram
xvals = np.zeros(nbins)     # The midpoints of your histogram bins that are used for plotting
delx = xmax / nbins
# Your code to compute an estimate for the probability density function of an exponential random
# variable goes here.
for i in range(500) :
    mybin = int( np.floor( exponential(lamd) / delx ) )
    histo[mybin] = histo[mybin] + 1
histo = histo / (delx*500)
for i in range(nbins) : xvals[i] = (i+0.5)*delx
# This draws the histogram - do not delete this code
plt.plot( xvals, histo, 'k-')
plt.xlabel("Random variable value")
plt.ylabel("Probability")
fighand=plt.gca()

nevents = 20
lamd = 2  
number_of_events = np.zeros(nevents)
arrival_times = np.zeros(nevents)
time = 0
for i in range(nevents) : 
  # You need to write code in here in order to set the elements 
  # of the two lists number_of_events and arrival_times
  time = time + exponential( lamd ) 
  arrival_times[i] = time
  number_of_events[i] = i+1
plt.plot( arrival_times, number_of_events, 'ko' )
plt.xlabel("time")
plt.ylabel("number of events")
fighand=plt.gca()

class Simulation : 
    def __init__(self,lambd,mu) :
       self.lam = lambd
       self.mu = mu
       self.num_in_system = 0
       self.clock = 0.0
       self.t_arrival = self.generate_interarrival()
       self.t_depart = float('inf')
       self.num_arrivals = 0
       self.num_departs = 0
       self.total_wait = 0.0
    def advance_time(self) :
       t_event = min( self.t_arrival, self.t_depart )
       self.total_wait += self.num_in_system*(t_event - self.clock)
       self.clock = t_event
       if self.t_arrival <= self.t_depart : 
          self.handle_arrival_event()
       else :
          self.handle_depart_event()
    def handle_arrival_event(self) :
       self.num_in_system += 1
       self.num_arrivals += 1
       if self.num_in_system <=1 :
          self.t_depart = self.clock + self.generate_service()
       self.t_arrival = self.clock + self.generate_interarrival() 
    def handle_depart_event(self) :
       self.num_in_system -= 1
       self.num_departs += 1
       if self.num_in_system > 0 :
          self.t_depart = self.clock + self.generate_service()
       else :
          self.t_depart = float('inf')
    def generate_interarrival(self) : 
       return -np.log( np.random.uniform(0,1) ) / self.lam
    def generate_service(self) : 
       return -np.log( np.random.uniform(0,1) ) / self.mu 
def average_time_in_queue( t, lambd, mu ) :
    # This creates an instance of the Simulation class called s
    # by calling the (constructor) function called __init__.
    s = Simulation(lambd,mu)
    # Your code goes here
    while s.clock<t : s.advance_time()
    return s.total_wait / s.num_departs
for i in range(10) :
    print( 1/(0.8), average_time_in_queue( 10000, 0.2, 1.0 ) )

class Simulation : 
    def __init__(self, lambd, mu) :
       self.lam = lambd
       self.mu = mu
       self.time_with_length = np.zeros(9)
       self.num_in_system = 0
       self.clock = 0.0
       self.t_arrival = self.generate_interarrival()
       self.t_depart = float('inf')
       self.num_arrivals = 0
       self.num_departs = 0
       self.total_wait = 0.0    
    def advance_time(self) :
       t_event = min( self.t_arrival, self.t_depart )
       self.total_wait += self.num_in_system*(t_event - self.clock)
       if self.num_in_system<9 : 
          self.time_with_length[self.num_in_system] += (t_event - self.clock)
       self.clock = t_event
       if self.t_arrival <= self.t_depart : 
          self.handle_arrival_event()
       else :
          self.handle_depart_event()
    def handle_arrival_event(self) :
       self.num_in_system += 1
       self.num_arrivals += 1
       if self.num_in_system <=1 :
          self.t_depart = self.clock + self.generate_service()
       self.t_arrival = self.clock + self.generate_interarrival()
    def handle_depart_event(self) :
       self.num_in_system -= 1
       self.num_departs += 1
       if self.num_in_system > 0 :
          self.t_depart = self.clock + self.generate_service()
       else :
          self.t_depart = float('inf')
    def generate_interarrival(self) : 
       return -np.log( np.random.uniform(0,1) ) / self.lam
    def generate_service(self) : 
       return -np.log( np.random.uniform(0,1) ) / self.mu
    
    def get_fraction_of_time_with_length(self):
       return self.time_with_length / self.clock
# This creates an instance of the Simulation class called s
# by calling the (constructor) function called __init__.
lam, expr, N = 0.5, 1, 100000
s = Simulation(lam,expr)
# Run a simulation of 10000 events 
for i in range(N) : s.advance_time()
indices, times = np.linspace( 0, 8, 9 ), s.get_fraction_of_time_with_length()
print( indices, times )
plt.bar( indices, times, width=0.1 )
plt.xlabel("number of people in queue")
plt.ylabel("probability")
# This code is required for the autofeedback- don't delete it!
fighand=plt.gca()

