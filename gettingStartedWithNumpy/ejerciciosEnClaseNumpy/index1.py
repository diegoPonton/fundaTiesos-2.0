import numpy as np


def sumArr(arr):
    sum = 0
    for i in arr:
        sum += i

    return sum


newArr = np.array([1, 2, 3, 4, 5])


print(sumArr(newArr))


def sumArr2(arr):
    return sum(arr)


# USO DE LA FUNCION SUM
