import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
y = x ** 2
rand_arr = np.random.randint(1,1000,2000).reshape(1000,2)

fig = plt.figure()  # pusty wykres bez żadnych właściwości
axes1 = fig.add_axes([0,0,1,1])  # left, bottom, width, height (musi być od 0 do 1)
axes2 = fig.add_axes([.2,.2,.8,.8])  # zestaw osi rozpoczyna się 20% na lewo i 20% od dolnej granicy płótna. Zajmuje też tylko 80% jego szerokości i wysokości, dlatego oba zestawy osi kończą się w tym samym miejscu.

axes1.plot(x,y)
axes2.scatter(rand_arr[:,0],rand_arr[:,1])

axes1.set_xlabel('Exponential')
axes2.set_xlabel('Random')

plt.show()