import numpy as np

import sys

np.set_printoptions(threshold=sys.maxsize)


# ARRAY CREATION

# CREATING AN ARRAY FROM AN PYTHON OBJECT

lista = [1, 2, 3, 4, 5]


arr = np.array(lista)


print('Esta es una lista: \n', lista)

print('Este es un arreglo creado a partir de dicha lista: \n', arr)

# CREATING USEFULL ARRAYS (zeros and ones):

arrZeros = np.zeros((3, 3))  # .zeros(tuple)

print('Esta es una matriz de ceros creada a partir de la funcion "ZEROS" : \n ', arrZeros)


# CREATING ARRAYS WITH ".arange" FUNCTION WICH IS ANALOGOUS TO "range" python built in function

arrArange = np.arange(0, 20, 5)  # .arange(INICIO, FINAL, STEP)


print('Esta es una funcion creada usando "arange": \n', arrArange)


# CREATING ARRAYS WITH ".linspace" FUNCTION WHERE ARGUMENTS ARE (INICIO, FIN, NUMBER OF ELEMENTS WE HOPE)

# USEFULL FOR CREATING ARRAYS WHERE WE WORK WITH FLOAT TYPE ELEMENTS


arrLinspace = np.linspace(0, 5, 10)

print('Este es un arreglo creado a partir de "linspace": \n', arrLinspace)


# ARRAYS BIGGER AND BIGGER


bigArr = np.arange(100)

reshapeBigArr = bigArr.reshape(10, 10)

print(reshapeBigArr)
