import numpy as np

# Operacje na tablicach o różnej wielkości i różnych wymiarach

arr = np.arange(0,101,10)
print(arr)
print("----- arr + 5 -----")
print(arr + 5)
print("----- arr / 5 -----")
print(arr / 5)

left_ = np.arange(10).reshape(5,2)
right_ = np.arange(5).reshape(5,1)
print(left_)
print(right_)
multi_arr = left_ * right_
print(f"---- Mnożenie -----\n {multi_arr}")