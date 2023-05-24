import numpy as np

one_dim = np.array([1,2,3,4])
two_dim = np.array([[100, 200, 50, 400], [50, 0, 0, 100], [350, 100, 50, 200]])

print(one_dim.reshape(2, 2)) # 2 x 2
print(two_dim.reshape(4, 3))  # ????
# print(two_dim.reshape(4, 4))
print(two_dim.flatten()) # 1 rząd ze wszystkimi wartościami [100 200  50 400  50   0   0 100 350 100  50 200]
print(two_dim.transpose())