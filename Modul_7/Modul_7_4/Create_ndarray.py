import numpy as np

### Podsumowanie
""" my_list = [1,2,3,4,5]
my_new_list = np.array(my_list)
print(f"My New List {my_new_list}")

my_nested_list = ([1,2,3],[4,5,6],[7,8,9])
my_new_nested_list = np.array(my_nested_list)
print(my_new_nested_list) """
###

print(np.arange(0,20)) # lista od 0 do 19
print(np.arange(0,20,2)) # lista od 0 do 19 parzyste
print(np.zeros(3)) # trzy zera
print(np.zeros((5,3))) # lista dwuwymiarowa z zerami y-5, x-3
print(np.ones(5)) # to samo z jedynkami

### Elementy różnego typu dla wektora
arr_01 = np.array([5, 10, 20])  # int32
print(arr_01, arr_01.dtype)
arr_02 = np.array([5, 10, 20.0])  # float64
print(arr_02, arr_02.dtype)
arr_03 = np.array([5, 10, '20'])  # <U11
print(arr_03, arr_03.dtype)

### Pozostałe funkcje
print("\n--- Pozostałe funkcje ---")
print(np.linspace(0,5,10))  # od 0 do 5  - dziesięć elementów w różnych odstępach
print(np.eye(4)) # macież kwadratowa z przekątną = 1, pozostałe wartości = 0
print(np.diag([5,0,4,1,3,2]))  #macież diagonalna - przekątna z listy, reszta ma zera