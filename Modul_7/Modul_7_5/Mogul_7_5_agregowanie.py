import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d, '\n')
print(arr_2d.min(axis=0), '\n')
print(arr_2d.min(axis=1))