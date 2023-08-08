
lados = []

print('Ingrese cada uno de los lados de un triangulo')

while len(lados) != 3:
    lados.append(float(input('Ingrese el lado del triangulo: ')))

if lados[0] == lados[1] == lados[2]:
    print('Los lados ingresados corresponden a un triángulo equilátero')

else:
    print('No es un triangulo equilatero')
