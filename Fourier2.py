import scipy.signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-2, 2, 1000, endpoint=True) 
functions=[]
harmonics=10
for i in range(1,harmonics,1):
    functions.append(((-1**(i+1))/i)*np.sin(2*i*np.pi*t))

plt.plot(t,5*scipy.signal.sawtooth(2 * np.pi * 1 * t))
plt.plot(t,(10/np.pi)*np.sum(functions,axis=0))

plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Sawtooth Signal') 
plt.grid()
plt.autoscale()
plt.show() 