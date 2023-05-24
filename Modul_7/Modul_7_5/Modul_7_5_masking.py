import numpy as np

arr = np.arange(0,50,5)  # start=0, stop=50, step=5
print(arr)

print(arr>15)  # [False False False False  True  True  True  True  True  True]
print(arr[arr>15])  # [20 25 30 35 40 45]

print((arr>15) & (arr!=40))  # [False False False False  True  True  True  True False  True]  & - i
print(arr[(arr>15) & (arr!=40)])  # [20 25 30 35 45]

print((arr<10) | (arr>=20))  # [ True  True False False  True  True  True  True  True  True]  | - lub
print(arr[(arr<10) | (arr>=20)])  # [ 0  5 20 25 30 35 40 45]

np.logical_or(arr<10,arr>=20) # to samo co powyżej
print(arr[np.logical_or(arr<10,arr>=20)])

a = np.array([0, 1, 0, 1])
b = np.array([0, 0, 1, 1])
result = np.logical_xor(a, b)
print(result)  # [False  True  True False]

