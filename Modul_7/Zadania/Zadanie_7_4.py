import numpy as np

print("----- Ćwiczenie 1 -----")
print(np.random.random(10))
print(np.random.uniform(0,1,10))

print("----- Ćwiczenie 2 -----")
my_list = np.zeros((5, 5))
for i in range(5):
    my_list[:,i] = np.arange(5)
print(my_list)

my_list = np.zeros((5, 5))
for i in range(5):
    my_list[i] = np.arange(5)
print(my_list.transpose())