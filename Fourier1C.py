import matplotlib.pyplot as plt
import numpy as np
import sk_dsp_comm.sigsys as ss

t = np.linspace(-15, 15, 1000, endpoint=True) 
Function=[]
harmonics=20
for i in range(0,harmonics,1):
    if i==0: an=2
    else: an=(20/(np.pi*i))*np.sin((i*np.pi)/5)
    Function.append(an*np.cos(i*np.pi/5*t))

T=10
x = ss.rect(np.mod(t+1,T)-1,2)
plt.plot(t,T*x)
plt.plot(t,np.sum(Function,axis=0))

plt.title('Even Pulse Function')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
