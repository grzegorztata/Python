import numpy as np

# Dwuwymiarowa ndarray
print("----- Dwuwymiarowa ndarray -----")
my_arr = np.arange(25).reshape(5,5)
print(my_arr)
print(my_arr[(0,1)])  # pierwszy rząd, druga kolumna
print(my_arr[(0,1),])  # dwa indeksy w pierwszym wymiarze i wszystkie indeksy w drugim, czyli [[0 1 2 3 4],[5 6 7 8 9]]
print(my_arr[[0,1],[0,4]])  # wybieramy (0,0) i (1,4), czyli [0,9]
print(my_arr[[3,4,2],[0,3,1]])  # [15 23 11]

print("\n----- Wielowymiarowa ndarray -----")
vals = np.array([100,5,0])
select = np.random.randint(0,3,size=(4,3))
print(select)
print(vals[select])