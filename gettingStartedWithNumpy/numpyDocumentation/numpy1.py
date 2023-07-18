import numpy as np


#   GETTING STARTED WITH NUMPY, THE BASICS

matrix = np.array([[0, 1, 2, 3],
                  [4, 5, 6, 7]], dtype=int)


print(matrix)

print('Numero de ejes del arreglo: ', matrix.ndim)

print('El tamaño del array en cada dimension es: ', matrix.shape)
# SALIDA >>> TUPLE : (COLUMNAS , FILAS)

print('El numero total de elementos de la matriz es: ', matrix.size)
# SALIDA >>> INT
