import pandas as pd

exam1 = [89,85,93,83]
exam2 = [74,56,44,92]
exam3=[67,59,79,84]
labels = ['Student A','Student B','Student C', 'Student D']

df = pd.DataFrame({'e1':exam1, 'e2':exam2, 'e3':exam3}, index=labels)
df['semester1'] = df['e1']+df['e2']+df['e3']
print(df)

""" print("\n----- MultiIndex - Sposób 1 - MultiIndex_from_tuples() -----")
schools = ['High School X','High School X','High School Y','High School Y']
multi_index_list = [(school,student) for school,student in zip(schools,df.index)]
print(multi_index_list)
# teraz MultiIndex.from_tuples()
df.index = pd.MultiIndex.from_tuples(multi_index_list,names=['School', 'Students'])
print(f'\n{df}') """

print("\n----- MultiIndex - Sposób 1 - set_index() -----")
df.set_index([pd.Index(['High School X','High School X','High School Y','High School Y']), df.index], inplace=True)
print(df)

df.index.names = ['School', 'Student']
print(df)

print('\n----- Zwracanie wszystkich pozycji ze wskazanego indexu -----')
df_get_index = df.loc['High School X']
print(df_get_index)

print('\n----- Zwracanie wszystkich pozycji z niższego indeksu -----')
df_get_iloc = df.loc['High School X'].iloc[0]
print(df_get_iloc)

print('\n----- Zwracanie wszystkich pozycji ze wskazanego indexu dla MultiIndex -----')
get_multiindex = df.xs('High School Y')
print(get_multiindex)

print('\n----- Zwracanie wszystkich pozycji z niższego indexu dla MultiIndex -----')
get_chosen_multiindex = df.xs(('High School Y', 'Student C'))
print(get_chosen_multiindex)

print('\n----- Zwracanie wszystkich pozycji z niższego indexu z użyciem levela -----')
get_multiindex_level = df.xs('Student D', level='Student')
print(get_multiindex_level)