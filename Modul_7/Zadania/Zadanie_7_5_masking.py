import numpy as np

print("----- Ćwiczenie 1 -----")
arr = np.arange(0,50,5)
print(arr)
print(arr[(arr<10) | (arr>=20) & (arr!=40)])

print("----- Ćwiczenie 2 v1 -----")
arr1 = np.zeros((4,4), dtype=bool)
for i in range(4):
    for j in range(4):
        arr1[i, j] = bool(i != j)
print(arr1)

print("----- Ćwiczenie 2 v2 -----")
matrix = np.fromfunction(lambda i, j: (i != j), (4, 4))
np.fill_diagonal(matrix, False)

print(matrix)