import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
y = x ** 2

plt.plot(x,y)

plt.plot(x,y, color='red')
plt.plot(x,y-10,color='blue',ls='dashed') # dodanie drugiej linii przerywanej
plt.xlabel('oś X')
plt.ylabel('oś Y')
plt.title('Tytuł wykresu')
plt.xticks(color='indigo')
plt.yticks(color='indigo')
plt.grid()
plt.axhline(y=50, color='k', linestyle='--')
plt.axvline(x=5, color='k', linestyle='--')

plt.show()