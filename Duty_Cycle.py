import numpy as np
import matplotlib.pyplot as plt

p_duty_Cycle=np.arange(0.4,0.7,0.1)
Amplitude=10
Period=10
Wo=2*np.pi/Period
# Duty Cycle = p_duty_Cycle[i]/T
C_Magnitudes=[]
C_Phases=[]

for i in range(0,len(p_duty_Cycle),1):#Recorrido por los diferentes ciclos de trabajo de la onda
    Magnitude=[]
    Phase=[]
    n=[]
    for j in range(-30,30,1): #Evaluación de los coefientes para cada Cn
        teta=j*Wo*p_duty_Cycle[i]/2
        if j==0: Magnitude.append((Amplitude*p_duty_Cycle[i])/Period)
        else: Magnitude.append(((Amplitude*p_duty_Cycle[i])/Period)*(np.sin(teta)/(teta)))
        n.append(j)
    for k in range(0,len(Magnitude),1): #Evaluación para los grados por cada Cn
        phase=0 if Magnitude[k]>0 else 180
        Phase.append(phase)
    C_Magnitudes.append(Magnitude)
    C_Phases.append(Phase)

fig, axs = plt.subplots(len(p_duty_Cycle),figsize=(50,400))
for i in range(0,len(p_duty_Cycle),1):#Gráficación
    axs[i].set_title(f"Duty Cycle {round(p_duty_Cycle[i],1)}")
    axs[i].stem(n,np.abs(C_Magnitudes[i]))
    
plt.subplots_adjust(hspace=1)
plt.show()

#Andrés Santiago Jiménez Guzmán - StormShadow