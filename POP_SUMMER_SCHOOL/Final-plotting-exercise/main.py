import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
def moon_temperature( time, lattitude ) : 
  phi = 15*(time - 12)
  phi_rad = phi*np.pi/180
  lamb = lattitude*np.pi/180
  T4 = (1-0.12)*1361*np.cos(lamb)*np.cos(phi_rad) / ( 0.98*5.67E-8)
  return T4**(1/4)

times = np.linspace(7,17,11)
temperatures = moon_temperature(times, 30)
plt.plot( times, temperatures, 'k-')
plt.xlabel("time of day")
plt.ylabel("Temperature at lattitude of 30 degrees / K")
fighand=plt.gca()

lattitudes = np.linspace(0,90,10)
temperatures = moon_temperature(10, lattitudes)
plt.plot( lattitudes, temperatures, 'k-')
plt.xlabel("latitude / degrees")
plt.ylabel("Temperature at 10:00 / K")
fighand=plt.gca()

def temperature_change( initial_lattitude, start_time, duration, final_latitude ) :
  return moon_temperature( start_time + duration, initial_lattitude ) - moon_temperature( start_time, initial_lattitude )

times = np.linspace(7,17,11)
temperatures = moon_temperature(times, 25)
plt.plot( times, temperatures, 'k-')
plt.xlabel("time / lunar hours")
plt.ylabel("temperature at latitude 25 degrees / Kelvin")
fighand=plt.gca()

times = np.linspace(7,17,11)
lattitudes = np.linspace(90,35,11)
temperatures = np.zeros(11)
for i in range(11) : temperatures[i] = moon_temperature(times[i], lattitudes[i])
plt.plot( times, temperatures, 'k-')
plt.xlabel("time / lunar hours")
plt.ylabel("temperature / K")
fighand=plt.gca()
