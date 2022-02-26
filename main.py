import sys
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 12])
ypoints = np.array([-1, 1])

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)

plt.plot(x, y, xpoints, ypoints)
plt.show()


print (sys.version)


