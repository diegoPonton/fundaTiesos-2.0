import numpy as np


# BASIC OPERATIONS USING NUMPY PART TWO !!!!

# UNARY OPERATIONS METHODS SUCH AS SUM, MIN OR MAX ARE ALREADY BUILT IN ON NDARRAY CLASS

# ESTA CLASE DE OPERACIONES UNUARIAS TRATA AL ARREGLO COMO SI DE UNA LISTA SE TRATASE

arr = np.arange(0, 20, 2).reshape(5, 2)

print('Este es nuestro arreglo: \n', arr)

print('La suma de todos sus elementos es:', arr.sum())

print('El elemento mas grande el el arreglo es:', arr.max())

print('El elemento mas pequeño de su arreglo es:', arr.min())

# PODEMOS USAR ESTAS OPERACIONES INDICANDO EN QUE EJE QUEREMOS QUE SEA APLICADA POR EJEMPLO

print(arr.max(axis=0))
#                       ESTO ME VA A DEVOLVER UN ARREGLO CON EL ELEMENTO MAYOR DE CADA COLUMNA DEL ARREGLO ORIGINAL

print(arr.min(axis=1))
#                       ESTO ME VA A DEVOLVER UN ARREGLO CON EL ELEMENTO MENOR DE CADA FILA DEL ARREGLO ORIGINAL

print(arr.sum(axis=0))
#                       LA FUNCION SUM DEVUELVE LA SUMA ACUMATIVA DE LAS FILAS O COLUMNAS
