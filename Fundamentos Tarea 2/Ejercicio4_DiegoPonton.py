"""
Ejercicio 04
Escriba una función ConvertirPalabra(cadena) que reciba como parámetro una cadena detexto
y cambie la primera letra a mayúscula de sólo las palabras que terminan con una vocal. Para
esto usted debe convertir la cadena en una lista, verificar palabra por palabra y convertirla con
la correspondiente función y a continuación convertir la lista ya cambiada en cadena de texto.
Considere que las palabras están separadas por un espacio en blanco

"""


def convertirPalabra(cadena):
    lista = cadena.split(" ")
    newList = []

    for palabra in lista:
        if palabra.endswith('a') or palabra.endswith('e') or palabra.endswith('i') or palabra.endswith('o') or palabra.endswith('u'):

            newList.append(palabra.capitalize())
            continue
        newList.append(palabra)

    return ' '.join(newList)


print(convertirPalabra('hola mundo'))
