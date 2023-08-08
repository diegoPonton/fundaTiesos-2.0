# NUMPY ARGMIN

import numpy as np

arr = np.array([[1, 3, 5],
                [2, 8, 4],
                [6, 7, 9]])


indiceMinimo = arr.argmin(axis=1)

print(indiceMinimo)
