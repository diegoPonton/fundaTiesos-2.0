bajoPeso = False
pesoNormal = False
sobrePeso = False

estatura = float(input('Ingrese su estatura en m: '))

peso = float(input('Ingrese el peso en Kg: '))


IMC = peso / estatura**2

if IMC < 18.5:
    bajoPeso = True
    print(f'Bajo peso = {bajoPeso}')
else:
    print(f'Bajo peso = {bajoPeso}')

if IMC >= 18.5 and IMC <= 24.99:
    pesoNormal = True
    print(f'Peso normal = {pesoNormal}')
else:
    print(f'Peso normal = {pesoNormal}')

if IMC >= 25:
    sobrePeso = True
    print(f'Sobre peso = {sobrePeso}')
else:
    print(f'Sobre peso = {sobrePeso}')
