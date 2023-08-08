
import numpy as np

a = np.array([1, 1, 2, 3, 4, 5])
b = np.array([[1, 2, 1, 2, 3],
             [4., 1., 2., 0., 1]])


print(np.argmin(b, axis=0))
