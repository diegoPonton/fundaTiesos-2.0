
print('Ingrese los datos con el formato FEDERACION,ATLETAS,MEDALLAS|FEDERACION,ATLETAS,MEDALLAS|... consecutivamente ')

datos = input('\nIngrese los datos:')


arrFederacion = datos.split("|")

ingresos = []

for i in arrFederacion:
    ingresoFederacion = 0
    adicional = 0
    data = i.split(",")
    ingresoFederacion = int(data[1]) * 250
    if int(data[2]) > 4:
        adicional = ingresoFederacion * 0.2
    elif int(data[2]) >= 2 and int(data[2]) <= 4:
        adicional = ingresoFederacion * 0.1
    elif int(data[2]) == 1:
        adicional = ingresoFederacion * 0.05

    arr = [data[0] + ',' + str(ingresoFederacion + adicional) + '|']
    ingresos.extend(arr)


print('\n'+''.join(ingresos))
