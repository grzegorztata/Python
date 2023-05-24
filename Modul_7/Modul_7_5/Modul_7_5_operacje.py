import numpy as np

macierz_1 = np.array([[1,3,6],
                     [7,1,1],
                     [7,2,7]])
print(f'Macierz 1\n{macierz_1}')
macierz_2 = np.array([[-9,3,7],
                      [7,3,1],
                      [-1,-9,5]])
print(f'Macierz 2\n{macierz_2}')
add_macierz = macierz_1 + macierz_2
subtract_macierz = macierz_1 - macierz_2
print(f'Dodawanie macierzy \n {add_macierz}')
print(f'Odejmowanie macierzy \n {subtract_macierz}')
print('----- Mnożenie macierzy A -----')
print(macierz_1.dot(macierz_2))
print('----- Mnożenie macierzy B -----')
print(macierz_2.dot(macierz_1))