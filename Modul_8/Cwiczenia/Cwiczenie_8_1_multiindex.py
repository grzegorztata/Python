import pandas as pd
import random as rd

exam1 = [89,85,93,83]
exam2 = [74,56,44,92]
exam3 = [67,59,79,84]
exam4 = []
exam5 = []
exam6 = []
labels = ['Student A','Student B','Student C', 'Student D']

for i in range(len(labels)):
    exam4.append(rd.randint(1,100))
    exam5.append(rd.randint(1,100))
    exam6.append(rd.randint(1,100))

df = pd.DataFrame({'e1':exam1, 'e2':exam2, 'e3':exam3, 'e4':exam4, 'e5':exam5, 'e6':exam6}, index=labels)
df['semester1'] = df['e1']+df['e2']+df['e3']+df['e4']+df['e5']+df['e6']
print(df)

df = df.drop('semester1', axis=1)
print(f'\n{df}')

columns = pd.MultiIndex.from_tuples([
    ('Semestr 1', 'exam1'),
    ('Semestr 1', 'exam2'),
    ('Semestr 1', 'exam3'),
    ('Semestr 2', 'exam4'),
    ('Semestr 2', 'exam5'),
    ('Semestr 2', 'exam6')
])

# dodać nazwy kolumn żeby nie było NaN
df = pd.DataFrame({
    ('Semestr 1', 'exam1'): exam1,
    ('Semestr 1', 'exam2'): exam2,
    ('Semestr 1', 'exam3'): exam3,
    ('Semestr 2', 'exam4'): exam4,
    ('Semestr 2', 'exam5'): exam5,
    ('Semestr 2', 'exam6'): exam6
}, index=labels, columns=columns)

print(f'\n{df}')
