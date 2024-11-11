import numpy as np

ar1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(ar1)
ar2 = ar1.transpose()
print(ar2)
s = ar1.sum()
print(s)
armul = ar1.dot(ar2)
print(armul)