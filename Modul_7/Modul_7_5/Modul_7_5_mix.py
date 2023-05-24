import numpy as np

print("--- Bazowy array ---")
arr = np.arange(20).reshape(4,5)
print(arr)
print("--- Wybieramy row 3, 0 i 1 z kolumn 1-3 ---")
print(arr[[3,0,1],:3])  # Wybieramy row 3, 0 i 1 z kolumn 1-3 - fancy indexing + slicing. Jest to kopia arr, ponieważ użyliśmy fancy indexingu
print("--- Wyświetlamy wszystkie kolumny licząc od indexu 2, lecz tylko te wiersze, których suma przekracza 10 ---")
arr.sum()
print(arr[arr.sum(axis=1)>10,2:])  # Wyświetlamy wszystkie kolumny licząc od indexu 2, lecz tylko te wiersze, których suma przekracza 10. Zmień na 9