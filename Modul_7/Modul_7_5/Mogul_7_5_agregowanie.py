import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d, '\n')
print(arr_2d.min(axis=0), '\n')  # axis=0 - poziomo
print(arr_2d.min(axis=1))  # axis=1 - pionowo

print("----- Dzielenie array przez samą siebie -----")
arr = np.arange(0,101,10)
print(arr)
print(arr / arr)