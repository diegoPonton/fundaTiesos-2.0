boleto = int(input('Ingrese el numero del boleto: '))
valorBoleto = None

primerNumero = int(str(boleto)[0])

u2D = int(str(boleto)[-2:])

p2d = int(str(boleto)[0:2])


if u2D % primerNumero == 0:
    if 2*p2d < u2D**2:
        valorBoleto = True
else:
    valorBoleto = False

print(valorBoleto)
