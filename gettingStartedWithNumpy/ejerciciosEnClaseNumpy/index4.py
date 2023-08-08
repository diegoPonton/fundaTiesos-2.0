# NUMEROS PARES E IMPARES

import numpy as np


def paresYnoPares(arr):
    par = arr % 2 == 0
    impar = arr % 2 != 0

    return arr[par], arr[impar]


arreglo = np.array([1, 2, 3, 4, 5, 6, 7, 8])

par, impar = paresYnoPares(arreglo)


print(par)

print(impar)
