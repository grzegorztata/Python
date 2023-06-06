import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,x**2,label='x^2')
axes.plot(x,x**3,label='x^3')

# loc=0 - Matplotlib sam znajdzie najlepsze miejsce na legendę
# axes.legend(loc=0)

axes.legend(loc=(1.05,0.0))

plt.show()