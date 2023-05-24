import numpy as np

one_dim = np.array([1,2,3,4])
type(one_dim)

one_dim.shape # kształt
one_dim.ndim # liczba wymiarów


print(one_dim)  # [ 1 2 3 4]
print(one_dim.shape)  # (4,) - 4 elementy w pierwszym wymiarze
print(one_dim.ndim)  # 1 wymiar

####  Dwa poziomy ####
one_dim_horizontal = np.array([[1,2,3,4]])
print(one_dim_horizontal.shape)  # (1,4)

one_dim_vertical = one_dim_horizontal.reshape(-1, 1)  # tabela pionowa
print(one_dim_vertical)
print(one_dim_vertical.reshape(1, -1)) # powrót do układu horyzontalnego