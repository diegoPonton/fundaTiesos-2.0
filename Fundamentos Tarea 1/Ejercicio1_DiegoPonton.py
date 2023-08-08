
valor = float(input("Ingrese el valor del producto: "))

if valor <= 10:
    print(
        f'El valor a pagar con descuento es {round(valor - valor*0.22,2   )}')
else:
    print(valor)
