import numpy as np

# INDEXING, SLICING AND ITERATING

# ONE DIMENSIONAL ARRAYS CAN BE INDEXED SLICED AND ITERATED JUST AS A LIST


arr = np.arange(10)**3

print(arr)

# INDEXING ARRAYS

print(arr[2])  # salida >> 8

# SLICING ARRAYS

print(arr[0:4])

# ITERATING ARRAYS

for i in arr:
    print(i)


# Multidimensional arrays can


matrix = np.arange(0, 100, 2).reshape(5, 10)

print(matrix)


#           INDEXING MULTIDIMENSIONAL ARRAYS

# ME DEVUELVE EL ELEMENTO UBICADO EN LA FILA 4 COLUMNA 7
print(matrix[3, 7])

#           SLICING MULTIDIMENSIONAL ARRAYS

# ME DEVUELVE LAS COLUMNAS 3 PRIMERAS FILAS DE LA COLUMNA 3
print(matrix[0:3, 3])

# ME DEVUELVE LAS PRIMERAS 3 FILAS
print(matrix[0:3, :])

# ME DEVUELVE LAS PRIMERAS 3 COLUMNAS
print(matrix[:, 0:3])


#            ITERATING OVER MULTIDIMENSIONAL ARRAYS

# THERE ARE MANY FORMS ABOUT HOW WE CAN ITERATE A MULTI DIMENSIONAL ARRAY

# USING NESTED BUCLE FORS !!!

for row in matrix:  # ME DEVUELVE CADA UNA FILA DE LA MATRIZ
    print(row)

for row in matrix:  # ME DEVUELVE CADA UNO DE LOS ELEMENTOS DE LA MATRIZ EN ORDEN
    for element in row:
        print(element)


# USING FUNCTION np.nditer()

for element in np.nditer(matrix):
    print(element)
