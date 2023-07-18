import numpy as np

# NUMPY ALSO HAVE SPECIAL FUNCTIONS BUILT IN THESE ARE SOME OF THEM:

# CUANDO USAMOS UNA DE FUNCION ESPECIAL EN UN ARREGLO ESTA FUNCION SE APLICA A CADA UNO DE LOS
# ELEMENTOS DEL ARREGLO, DEVOLVIENDONOS UN ARREGLO RESULTANTE


arr = np.arange(0, 50, 2).reshape(5, 5)


print(np.sin(arr), '\n')

print(np.cos(arr), '\n')

print(np.absolute(arr), '\n')

print(np.exp(arr), '\n')
