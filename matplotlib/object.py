#Object oriented method
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,21)
y = x**2

fig = plt.figure() # Imaginary blank canvas

#axes = fig.add_axes([left,button,height,width])
axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')