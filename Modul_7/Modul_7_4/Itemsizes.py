import numpy as np

two_dim = np.array([[100, 200, 50, 400], [50, 0, 0, 100], [350, 100, 50, 200]])

print("len: " + str(len(two_dim)))  # 3
print("shape: " + str(two_dim.shape))  # (3, 4) - 3 rzędy po 4 elementy
print("ndim: " + str(two_dim.ndim))  # 2 - wymiary
print(two_dim.size)  # liczba elementów
print(two_dim.itemsize)  # wielkość pojedyńczego elementu w bajtach