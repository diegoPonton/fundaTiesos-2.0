transacciones = [
    'centro|Bahia|futbol|zapatos-Adidas|290.78|25-03-2013',
    'centro|Malecon2000|natacion|chaleco-Fins|110.92|01-02-2013',
    'sur|MallDelSur|natacion|gafasPiscina-Swingo|90.07|13-05-2014',
    'centro|Bahia|natacion|zapatos-Adidas|315.72|13-05-2015'
]


sur = []

centro = []

norte = []


def clasificarNombreTienda():
    newArr = []
    for transaccion in transacciones:
        newArr = transaccion.split('|')
        if newArr[0] == 'centro':
            centro.append(newArr[1])
        elif newArr[0] == 'sur':
            sur.append(newArr[1])
        else:
            norte.append(newArr[1])

    print(sur)

    print(centro)

    print(norte)


def totalVentas(marca, fecha):
    totalVentas = 0
    newArr = []
    for transaccion in transacciones:
        newArr = transaccion.split('|')
        if marca in newArr[3] and fecha in newArr[5]:
            totalVentas += float(newArr[4])
    return totalVentas


# print(totalVentas('Adidas', '05'))


# TOTAL DE VENTAS TOTAL POR SECTOR

def totalVentaAnual(sector, año):
    totalVentas = 0
    newArr = []
    for transaccion in transacciones:
        newArr = transaccion.split('|')
        if sector == newArr[0] and año in newArr[5]:
            totalVentas += float(newArr[4])
    return totalVentas


print(totalVentaAnual('centro', '2013'))
