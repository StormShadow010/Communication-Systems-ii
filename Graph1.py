import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10, 1000,endpoint=True)

f1=15*np.cos(1000*x)
print(f"Function:{f1}")
plt.plot(x,f1)
plt.show()