import numpy as np

import random as rd

sur = ['LosEsteros', 'Pradera', 'RiocentroSur']
centro = ['Bahia', 'Malecon2000', 'MaleconSalado']
norte = ['MallDelSol', 'CityMall', 'RiocentroNorte']

futbol = ['zapatos-Nike', 'medias-Nike', 'rodilleras-Reebok']
natacion = ['short-Nike', 'gafasPiscina-Swingo', 'aletas-Speedo']

matriz_valores = np.array([[2000, 1200, 1478, 234, 43, 54],
                           [1000, 1000, 2344, 5543, 66, 357],
                           [0, 300, 2111, 33, 255, 614],
                           [1500, 0, 754, 1298, 0, 941],
                           [239.45, 0, 9532, 528, 235, 242],
                           [850, 2100, 53, 264, 54, 63],
                           [2365, 234, 86, 654, 0, 375],
                           [1800, 665, 0, 2341, 0, 153],
                           [1300, 373, 0, 9877, 234, 25]])


"""
        a) Escoja vía programación 3 tiendas aleatoriamente (1 de norte, 1 de sur y 1 de centro)
        y presente el nombre de la tienda y el promedio de la venta de productos de estas tiendas,
        pero sólo en la categoría natación.
"""

aleatoria_sur = sur[rd.randint(0,2)]
aleatoria_centro = centro[rd.randint(0,2)]
aleatoria_norte = norte[rd.randint(0,2)]

indexSur = sur.index(aleatoria_sur)

indexCentro = centro.index(aleatoria_centro)

indexNorte = norte.index(aleatoria_norte)


natacion = matriz_valores[:,3:]

promedioTiendaAleatoriaSur = np.mean(natacion[indexSur,:])

promedioTiendaAleatoriaCentro = np.mean(natacion[indexCentro,:])

promedioTiendaAleatoriaNorte = np.mean(natacion[indexNorte,:])

print(promedioTiendaAleatoriaSur)

print(promedioTiendaAleatoriaCentro)

print(promedioTiendaAleatoriaNorte)


"""
        b) Imprima el Top 3 de las tiendas que más han vendido productos.
"""


ventas = np.sum(matriz_valores, axis=1)

tiendas = sur + centro + norte

tiendasVentas = zip(tiendas,ventas)

tiendasVentasOrdenadas = sorted(tiendasVentas, key=lambda tienda: tienda[1], reverse=True)

print(tiendasVentasOrdenadas[0:3])



"""
c) Presente la suma total de venta de los productos de natación de todas las tiendas del centro.
"""

tiendasCentroNatacion = matriz_valores[3:6,3:]

ventasNatacionCentro = np.sum(tiendasCentroNatacion)

print(ventasNatacionCentro)

"""
d) Presente el nombre de las tiendas que han vendido entre $4000 y $6000
"""

ventasPorTienda = np.sum(matriz_valores, axis = 1)


# condicion = ventasPorTienda > 4000 and ventasPorTienda < 6000     NO SE PUEDE HACER SE HACE EN DOS MASCARAS BOOLEANAS COMBINADAS  

arrTiendas = np.array(tiendas)


#RESOLUCION POR MASCARAS BOOLEANAS:


condicion1 = ventasPorTienda > 4000

condicion2 = ventasPorTienda < 6000

combined = condicion1 & condicion2

print(arrTiendas[combined])


#RESOLUCION USANDO ZIP Y FILTER

tiendasVentas = zip(arrTiendas, ventasPorTienda)

arrFiltrado = list(filter(lambda tienda: tienda[1] > 4000 and tienda[1] < 6000, tiendasVentas))

print(arrFiltrado)