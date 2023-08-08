"""
Feria Gastronómica Raíces - 2023
Después de la ronda de clasificación de la Feria Raíces tenemos una matriz de calificaciones.

Las filas representan a cada uno de los jueces y las columnas representan a cada uno de los participantes. Cada participante interviene con dos platos al concurso.

Cada uno de los valores de la matriz corresponde la calificación de un juez a un determinado plato. Cada plato es calificado sobre 5 puntos.

Agregue el código en el archivo main.py para las siguientes situaciones:

    Cree una matriz de ceros con las dimensiones (3x10) necesarias. Muestre la matriz resultante.
    Cambie los votos del juez 1 por los siguientes valores: [3,2,4.5,4,5,4,1,3,4,5] Muestre la matriz resultante.
    Cambie los votos del juez 2 por los siguientes valores:[4,1,2,3,3.5,4.2,3.7,4.8,2.9,5]
    Cambie los votos del juez 3 por los siguientes valores: [3.1,2.5,3.3,4.1,5,5,4,2,3,1]
    Muestre la cantidad de elementos en la matriz
    Muestre el número de filas y de columnas en la matriz
    Muestre los votos del juez 1
    Muestre el total de votos del juez 2
    Muestre el promedio de votos del juez 3
    Muestre el total de votos por cada juez
    Muestre el total de votos por cada plato
    Muestre el total de votos MENOR por juez
    Muestre el total de votos MAYOR por plato

"""

import numpy as np

matriz = np.zeros((3, 10))


# Votos Juez 1
votosJuez1 = matriz[0, :] = [3, 2, 4.5, 4, 5, 4, 1, 3, 4, 5]

# Votos Juez 2
votosJuez2 = matriz[1, :] = [4, 1, 2, 3, 3.5, 4.2, 3.7, 4.8, 2.9, 5]

# Votos Juez 3
votosJuez3 = matriz[2, :] = [3.1, 2.5, 3.3, 4.1, 5, 5, 4, 2, 3, 1]


print(matriz)


# cantidad de elementos en la matriz
print(matriz.size)

# numero de filas y numero de columnas

filas, columnas = matriz.shape

print('Filas: ', filas, 'Columnas: ', columnas)


# mostrar votos Juez 1:

print(votosJuez1)


# mostrar total de votos Juez 2:

print(len(votosJuez2))


# mostrar promedio votos juez 3:

print(np.mean(votosJuez3))


# mostrar total votos por cada juez

for i in range(matriz.shape[0]):
    print('total de votos juez', i+1, ': ', len(matriz[i, :]))
