import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
y = x ** 2

plt.plot(x,y)

plt.subplot(1,2,1)
plt.plot(x,y,color='red')

plt.subplot(1,2,2)
plt.plot(y,x,color='blue')

plt.show()