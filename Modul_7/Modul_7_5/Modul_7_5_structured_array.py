import numpy as np

dt = np.dtype([('student','S10'),('exam1',int),('exam2',int)])
a = np.array([("Student A",89,74),("Student B",85,56),
              ("Student C", 93,44), ("Student D",83,92)],dtype=dt)

print(a)
print('----- Sortowanie po exam1 -----')
print(np.sort(a,order='exam1'))
print('----- Sortowanie po exam2 -----')
print(np.sort(a,order='exam2'))
print('----- Który student zdobył najwięcej punktów z exam2 -----')
print(np.sort(a,order='exam2')[-1][0]) # Student pierwszy od końca po sortowaniu exam2, kolumna 0 - Student


print('----- Wyświetlanie indeksów posortowanych wartości -----')
arr = np.random.randint(1,40,10)
print(arr)
display_sorted_index = np.argsort(arr)
print(display_sorted_index)  # do dopytania na sporkaniu