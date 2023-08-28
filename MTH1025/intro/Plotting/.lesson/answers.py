import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,7,500)
y=np.sin(x) # phase = 0
z=np.sin(x+np.pi/2) # phase = pi/2

# Your code here:
plt.plot(x,y,'r',label='phase = 0')
plt.plot(x,z,'b--',label='phase = pi/2')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (cm)')
plt.title("Harmonic motion with differing starting phases")
plt.legend()
plt.axis([0,2*np.pi,-1,1])
