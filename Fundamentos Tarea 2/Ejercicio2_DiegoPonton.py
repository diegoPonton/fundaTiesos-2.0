import random

frutas = ['aguacate', 'cerezas', 'ciruelas', 'fresas',
          'kiwi', 'limon', 'mandarina', 'manzana', 'melon']


energias = [134, 58, 45, 34, 53, 39, 39, 41, 37]
agua = [79, 82, 84, 88, 83, 87, 86, 85, 88]
hidratos = [1.3, 13.5, 11.0, 7.0, 12.1, 9.0, 9.0, 10.5, 8.4]
fibras = [2.4, 1.5, 2.1, 2.2, 1.5, 1.0, 1.9, 2.3, 0.8]
grasas = [13.8, 0.5, 0.15, 0.5, 0.44, 0.3, 0.19, 0.2, 0.28]
proteinas = [1.3, 0.8, 0.6, 0.7, 1.0, 0.7, 0.8, 0.3, 0.9]


# ¿Cuál es el número de hidratos de la fruta que tiene mayor fibra? (Presentar el nombre de la fruta, el número de hidratos y el número de fibra

mayor = max(fibras)

indice = fibras.index(mayor)

print(f'La/El {frutas[indice]} y su numero de hidratos {hidratos[indice]}')

# ¿Cuál es el número de grasa de la fruta que tiene menor agua? (Presentar el nombre de la fruta, elnúmero de grasa y el número de agua)

indice_menor_agua = agua.index(min(agua))
fruta_menor_agua = frutas[indice_menor_agua]
grasa_menor_agua = grasas[indice_menor_agua]
agua_menor = min(agua)

print("La fruta con menor agua es:", fruta_menor_agua)
print("Número de grasa:", grasa_menor_agua)
print("Número de agua:", agua_menor)

# Elija 2 frutas aleatorias y compare su nivel de fibras. Si ambas frutas tienen el mismo nivel de fibras presentar por pantalla las frutas, sus niveles de fibra y la suma de ambas fibras. En caso de que no sean iguales, mostrar la diferencia de sus niveles de fibras.


indice1 = random.randint(0, len(frutas))

indice2 = random.randint(0, len(frutas))

fruta_1 = frutas[indice1]

fruta_2 = frutas[indice2]

fibra_1 = fibra[indice1]

fibra_2 = fibra[indice2]

if fibras[indice1] == fibras[indice2]:
    print(
        f'Las frutas son: {fruta_1} y {fruta_2} y la suma de sus fibras es {fibra_1 + fibra_2}')


""" 
Escribir un programa que solicite por pantalla 2 nombres de frutas. Si el nivel de proteínas de la
primera fruta es menor que el promedio de los hidratos de todas las frutas, y el nivel de fibras de la
segunda fruta en menor que le promedio grasas de todas las frutas; presentar en pantalla la suma
de energías de las dos frutas; caso contario presentar la resta de energías de las dos frutas.

"""


def ejercicio4():
    fruta1 = input('Ingrese la primera fruta >>> ')

    fruta2 = input('Ingrese la segunda fruta >>> ')

    indice1 = frutas.index(fruta1)

    indice2 = frutas.index(fruta2)

    proteina1 = proteina[indice1]

    proteina2 = proteina[indice2]

    hidrato1 = hidratos[indice1]

    hidrato2 = hidratos[indice2]

    energia1 = energias[indice1]

    energia2 = energias[indice2]

    promedio_hidratos = sum(hidratos)/len(hidratos)

    promedio_grasas = sum(grasas)/len(grasas)

    fibras2 = fibras[indice2]

    if proteina1 < promedio_hidratos and fibras2 < promedio_grasas:
        print(energia1 + energia2)
    else:
        print(energia1 - energia1)
