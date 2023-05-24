import numpy as np

print("----- Ćwiczenie 1 -----")
arr = np.arange(20).reshape(4, 5)
print(arr)

column_sums = arr.sum(axis=1)  # DOPYTAĆ o axis - Sumowanie wyłącznie wewnątrz jednej osi

selected_columns = np.where(column_sums > 30)

result = arr[2, selected_columns]

print(result)

print("\n----- Ćwiczenie 2 -----")
a = np.array([97, 101, 105, 111, 117, 125])
b = np.array(['a', 'e', 'i', 'o', 'u', 'y'])
filtered_values = b[(a>100) & (a<110)]
print(filtered_values)

print("\n----- Ćwiczenie 3 -----")
macierz = np.array([[3,4,1],[0,2,5]])
min_value = np.min(macierz, axis=1)
max_value = np.max(macierz, axis=1)
for i in range(len(macierz)):
    print(f"Najmniejsza wartość w wierszu {i + 1} to: {min_value[i]}, natomiast największa to: {max_value[i]}")

print("\n----- Ćwiczenie 3 -----")
arr_4 = np.arange(11)
arr_4_reserved = np.where((arr_4>3) & (arr_4<8), -arr_4, arr_4)  # Jeśli warunek prawdziwy: -arr, jeśli fałszywy: arr
print(arr_4_reserved)