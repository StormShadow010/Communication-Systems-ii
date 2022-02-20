import scipy.signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 5, 1000, endpoint=True) 
functions=[]
harmonics=20
for i in range(1,harmonics,2):
    functions.append(np.sin(i*np.pi*t)/i)

plt.plot(t,0.5+(1/2)*scipy.signal.square(2 * np.pi * 1/2 * t))
plt.plot(t,1/2+(2/np.pi)*np.sum(functions,axis=0))

plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Square Signal') 
plt.grid()
plt.autoscale()
plt.show() 