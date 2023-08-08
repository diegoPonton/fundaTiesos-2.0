import random

import numpy as np



#SUCURSALES

sur = ['LosEsteros','Pradera', 'RiocentroSur']
centro = ['Bahia', 'Malecon2000', 'MaleconSalado']
norte = ['MallDelSol', 'CityMall', 'RiocentroNorte']


#PRODUCTOS

futbol = ['zapatos-Nike', 'medias-Nike', 'rodilleras-Reebok']
natacion = ['short-Nike', 'gafasPiscina-Swingo', 'aletas-Speedo']


# MATRIZ SUCURSAL ( FILAS ) - PRODUCTOS ( COLUMNAS )

matriz_valores=np.array([[2000,1200,1478,234,43,54],
                        [1000,1000,2344,5543,66,357],
                        [0,300,2111,33,255,614],
                        [1500,0,754,1298,0,941],
                        [239.45,0,9532,528,235,242],
                        [850,2100,53,264,54,63],
                        [2365,234,86,654,0,375],
                        [1800,665,0,2341,0,153],
                        [1300,373,0,9877,234,25]])


                    ############### EJERCICIOS ##################

"""

a) Escoja vía programación 3 tiendas aleatoriamente (1 de norte, 1 de sur y 1 de centro)
    y presente el nombre de la tienda y el promedio de la venta de productos de estas tiendas,
    pero sólo en la categoría natación.

"""


norteIndex = random.randint(0,2)

surIndex = random.randint(0,2)

centroIndex = random.randint(0,2)


randomSur = sur[surIndex]
randomCentro = centro[centroIndex]
randomNorte = norte[norteIndex]


filaTiendaNorte = matriz_valores[norteIndex, :]

filaTiendaSur = matriz_valores[3 + surIndex, :]

filaTiendaCentro = matriz_valores[6 + centroIndex, :]

print(f'Sucursal Sur { randomSur}               {np.mean(filaTiendaSur)}')
print(f'Sucursal Norte { randomNorte}           {np.mean(filaTiendaNorte)}')
print(f'Sucursal Centro { randomCentro}         {np.mean(filaTiendaCentro)}')

"""
b) Imprima el Top 3 de las tiendas que más han vendido productos.

"""

shape = matriz_valores.shape

totalProductosPorTienda = []

for i in range(shape[0]):                                           #USAR BUCLE FOR O "np.sum(matriz_valores, axis=1)"
    sumaPorIteracion = sum(matriz_valores[i , : ])
    totalProductosPorTienda.append(sumaPorIteracion)


listaSucursalProductos = zip(sur + centro + norte, totalProductosPorTienda)

ordenadaSucursalesProductos = sorted(listaSucursalProductos, key = lambda tupla: tupla[1])

print(ordenadaSucursalesProductos[0:3])


"""

c) Presente la suma total de venta de los productos de natación de todas las tiendas del centro.

"""

matrizReducida = matriz_valores[3:6, 3:6]

print(np.sum(matrizReducida))




"""

d) Presente el nombre de las tiendas que han vendido entre $4000 y $6000

"""

sumaProductosFila = np.sum(matriz_valores, axis=1)

listaSucursalVentas = zip(sur + centro + norte, sumaProductosFila)

listaFiltrada = filter(lambda tupla: tupla[1] > 4000 and tupla[1] < 6000, listaSucursalVentas)

print(list(listaFiltrada))




"""
e) El promedio de ventas de los productos de la marca Nike.
"""

columnas_nike = [0, 1, 2]


filas_sucursales = np.arange(len(matriz_valores))


promedio_nike_por_sucursal = np.mean(matriz_valores[filas_sucursales, columnas_nike], axis=1)

for i, sucursal in enumerate(sur + centro + norte):
    print(f"Promedio de ventas productos Nike en {sucursal}: {promedio_nike_por_sucursal[i]}")
