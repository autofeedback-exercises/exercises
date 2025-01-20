import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def moon_temperature(t) :
  phi = 15*(t-12)
  phi_rad = np.pi*phi/180
  T4 = 1361*(1-0.12)*np.cos(phi_rad) / (0.98*5.67E-8)
  return T4**(1/4)

times = np.linspace( 7,17,11)
temperatures = moon_temperature(times)

plt.plot( times,temperatures, 'k-')
plt.xlabel("time of day")
plt.ylabel("Temperature at equator / K")
plt.show()

def moon_rotation( time ) :
  return time / (29.5*24) * 360

new_times = (times - 7)*29.5/24

plt.plot( new_times,temperatures, 'k-')
plt.show()

def lunar_temperature( ang ):
  phi = 90 - ang
  phi_rad = np.pi*phi/180
  T4 = 1361*(1-0.12)*np.cos(phi_rad) / (0.98*5.67E-8)
  return T4**(1/4) - 273
