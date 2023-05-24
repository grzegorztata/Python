import numpy as np

print("----- Tablica jednowymiarowa -----")
my_arr = np.arange(21)
print(my_arr) # wiadomo, 21 kolejnych liczb całkowitych
print(my_arr[10])  # wyciągamy wartość '10'
print(my_arr[5:15])  # wyciągamy wartości od 5 do 15 (bez 15)
print(my_arr[5:15:4])  # wartości od 5 do 15, step 4, czyli [ 5  9 13]

print("\n----- Tablica wielowymiarowa -----")
two_dim = np.array([[0,10,20],[5,15,25],[100,200,300]])
print(two_dim)
print(two_dim[0])  # [ 0 10 20]
print(two_dim[1][0])  #drugi rząd, pierwsza kolumna, czyli 5
print(two_dim[1:3,:2])  # przed przecinkiem - wiersze, po przecinku - kolumny, czyli [ 5 15], [100 200]  wiersze 1-2 i 2 pierwsze kolumny
print(two_dim[0:2,:2])  # przed przecinkiem - wiersze, po przecinku - kolumny, czyli [ 0 10], [ 5 15]  wiersze 0-1 i 2 pierwsze kolumny 
print(two_dim[0:2,1:])  # przed przecinkiem - wiersze, po przecinku - kolumny, czyli [ 10 20], [ 15 25]  wiersze 0-1 i od drugiej kolumny