import numpy as np

print("----- Ćwiczenie 1 - wyświetl indexy wartości niezerowych")
arr = np.array([1,2,0,0,4,0])
non_zero_arr = np.nonzero(arr)
print(non_zero_arr)