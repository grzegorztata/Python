import numpy as np

print("----- Ćwiczenie 2 -----")
z_wektor = np.random.uniform(0,1,10)  # 10 liczb z zakresu 0,1
print(z_wektor)

z_argmin = z_wektor[np.argmin(np.abs(z_wektor - 0.5))]  # argmin - najmniejsza wartość, abs - szukamy najniższej wartości absolutnej
print(z_argmin)

print("----- Ćwiczenie 3 -----")
arr = np.random.randint(1, 100, 20)
print(arr)
max_value = np.argmax(arr)
arr[max_value] = 0
print(arr)

print("----- Ćwiczenie 4  - Znajdź części całkowite -----")
arr_4 = np.array([5, 0.0249139 , 0.11873564, 0., 0.72321586, 11308494, 0.29931472, 0.24439968, 0.61251754, 4])
integer_part = np.floor(arr_4)

print(integer_part)