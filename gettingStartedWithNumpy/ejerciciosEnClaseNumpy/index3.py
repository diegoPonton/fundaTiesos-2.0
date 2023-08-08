# FILTRADO DE ELEMENTOS

import numpy as np


def filterValue(arr, value):
    condition = arr > value

    print(condition)

    return arr[condition]


print(filterValue(np.array([1, 2, 3, 4, 5]), 3))
