import numpy as np


lista_de_compras = []

titulos = ['1) La Ternura         $30',
           '2) Diario de un loco  $20',
           '3) Las irresponsable  $25']

precios = []

for titulo in titulos:
    precio = titulo.split()[-1]
    precios.append(int(precio[1:]))


def mostraInfo(titulos):
    arr = titulos.split('$')
    precio = arr[-1]
    return int(precio)()


respuesta = input('¿Deseas comprar una entrada para alguna obra? \n').lower()

while respuesta != 'si':
    respuesta = input('¿Deseas comprar una entrada para alguna obra?')

opciones = input("""
1) La Ternura         $30
2) Diario de un loco  $20
3) Las irresponsable  $25
 
 
Su opcion es : """)

while int(opciones) not in [1, 2, 3]:
    opciones = input("""
1) La Ternura         $30
2) Diario de un loco  $20
3) Las irresponsable  $25
 
 
Su opcion es : """)

boletos = int(input('Ingrese la cantidad de boletos que desea comprar: '))

while boletos <= 0:
    boletos = int(input('Ingrese la cantidad de boletos que desea comprar: '))

# Convert opciones to integer here
opciones = int(opciones)

if opciones == 1:

    lista_de_compras.append(
        f'{titulos[0]} {boletos} boletos          SUBTOTAL: {precios[0]*boletos}')
elif opciones == 2:
    lista_de_compras.append(
        f'{titulos[1]} {boletos} boletos          SUBTOTAL: {precios[1]*boletos}')

elif opciones == 3:
    lista_de_compras.append(
        f'{titulos[2]} {boletos} boletos          SUBTOTAL: {precios[0]*boletos}')


print(lista_de_compras)
