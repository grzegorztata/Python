import numpy as np

print("----- View przy slicingu -----")
arr = np.arange(10)
print(arr)
slice_of_arr = arr[:5]
print(slice_of_arr)  # [0 1 2 3 4]
slice_of_arr[:] = 100
print(slice_of_arr)  # [100 100 100 100 100] - każdy element slice_of_arr zamieniamy na 100 
print(arr)  # [100 100 100 100 100   5   6   7   8   9]  - to co przed ucięciem zamieniono na 100 resztę wyświetlamy normalnie

print("\n----- View przy fancy indexing -----")
fancy_arr = np.arange(10)
print(fancy_arr)
fancy_index_arr = fancy_arr[np.arange(5)]
print(fancy_index_arr)  # [0 1 2 3 4]
fancy_index_arr[:] = 100
print(fancy_index_arr)  # [100 100 100 100 100]
print(fancy_arr)  #[0 1 2 3 4 5 6 7 8 9] - dlatego że "fancy_index_arr = fancy_arr[np.arange(5)]" tworzy kopię fancy_arr

print("\n----- Kopiowanie, jeżeli nie chcemy naruszyć oryginalnej tablicy -----")
arr_1 = np.arange(10)
print('arr_1')
print(arr_1)  # [0 1 2 3 4 5 6 7 8 9]

slice_of_arr_1 = arr_1[:5].copy()
print("slice_of_arr_1")
print(slice_of_arr_1)  # [0 1 2 3 4]

slice_of_arr_1[:] = 100
print("slice_of_arr_1") 
print(slice_of_arr_1)  # [100 100 100 100 100]

print('arr_1')
print(arr_1)  # [0 1 2 3 4 5 6 7 8 9]

print(slice_of_arr_1 is arr_1)  # False

print("\n----- Indeksowanie macierz w macierzy -----")
macierz = np.arange(9).reshape(3,3)
print(macierz)
macierz[-1, -1] = 999
print(macierz)  # ostatni rząd, ostatnia kolumna - wartość 999
macierz[1:, 1:] = 0
print(macierz)  