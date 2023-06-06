import matplotlib.pyplot as plt
import numpy as np

rand_arr = np.random.randint(1,1000,2000).reshape(1000,2)  # macierz o kształcie (1000,2) wypełnioną losowymi wartościami.
plt.scatter(rand_arr[:,0],rand_arr[:,1])  # scatter - wizualizacja punktów

# Prawa górna ćwiartka w kolorze czerwonym
cmap = np.empty(rand_arr.shape,dtype='object')
cmap[:] = 'blue'
cmap[rand_arr.min(axis=1)>500] = 'red'
plt.scatter(rand_arr[:,0],rand_arr[:,1],c=cmap[:,0])

# Zwiększanie rozmiaru wykresu
plt.figure(figsize=(10,5))  # dimyślna wartość (6.4, 4.8)
plt.scatter(rand_arr[:,0],rand_arr[:,1],c=cmap[:,0])

plt.show()

### Wykres kołowy ###
pie_data = np.array([30,20,20,40,10])
labels = ['A','B','C','D','E']
plt.pie(pie_data,labels=labels,autopct='%1.1f%%')
plt.show()