import numpy as np

print('----- Tablica jednowymiarowa -----')
arr = np.random.randint(1,40,10)
print(arr)
print(np.sort(arr)) # jest to jedynie kopia wektora
arr = np.sort(arr)
# print(arr)  # nowy zaktualizowany arr
print(np.sort(arr)[::-1])  # sortowanie malejąco

print('\n----- Tablica wielowymiarowa -----')
arr2d = np.array([np.arange(1,6),np.arange(6,1,-1)]).reshape(5,2)
print(arr2d)
print('----- Sortowanie po osi x -----')
print(np.sort(arr2d))
print('----- Sortowanie po osi y -----')
print(np.sort(arr2d, axis=0))