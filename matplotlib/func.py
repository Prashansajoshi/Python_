import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,21)
y = x**2

plt.subplot(1,2,1)
plt.plot(x,y,'b')