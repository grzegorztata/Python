import pandas as pd 

exam1 = [89,85,93,83]
labels  = ['Student A', 'Student B', 'Student C', 'Student D']

print('----- Drukowanie całej tabeli -----')
print(pd.Series(exam1, labels))

print('\n----- Drukowanie pojedyńczego wyniku -----')
print(pd.Series(exam1, labels)['Student D'])

print('\n----- Drukowanie słownika -----')
d = {s:p for s,p in zip(labels, exam1)}
print(d)
print(pd.Series(d))

print('\n----- Dodanie wyników z drugiego egzaminu -----')
exam2 = [74,56,44,92]
e1 = pd.Series(exam1, labels)
e2 = pd.Series(exam2, labels)

print('\n----- Dodanie wyników z obu egzaminów -----')
print(e1 + e2)