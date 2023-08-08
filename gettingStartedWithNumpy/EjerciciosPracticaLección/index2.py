import numpy as np


arr_paises = np.array([
  "Reino Unido", "Australia", "Austria", "Francia", "Alemania", "Italia",
  "Japón", "Países Bajos", "Noruega", " Suecia", "Estados Unidos"
])
arr_datos1977 = np.array([4, 8, 9, 1, 5, 16, 3, 1, 4, 9, 3])
arr_datos1978 = np.array([2, 15, 8, 2, 5, 36, 5, 4, 6, 6, 6])
arr_datos1980 = np.array([1, 1, 5, 17, 2, 9, 5, 2, 2, 7, 1])


#1 

"""
Para 1977, muestre los nombres de los países en los que se ubicaron en el primer lugar de preferencias.
"""

# condicion = arr_datos1977 == 1

# print(arr_paises[condicion])

#2

"""
Para 1980, muestre los nombres de los países en los que se ubicaron en el primer lugar de preferencias.
"""

# condicion = arr_datos1980 == 1

# print(arr_paises[condicion])

#3

"""
Para 1978, muestre los nombres de los países en los que se ubicaron en el top5 de preferencias.
"""

condicion = arr_datos1978 < 5 

print(arr_paises[condicion])


#4
"""
Para 1978, muestre la cantidad de países en los que se ubicaron en el top10.
"""

condicion = arr_datos1978 < 10

top10 = arr_datos1978[condicion]

print(top10.size)