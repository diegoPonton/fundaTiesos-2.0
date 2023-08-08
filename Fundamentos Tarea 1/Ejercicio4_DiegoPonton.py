
denominacion = [50, 20, 10, 5, 1]

billetes = []

monto = int(input('Ingrese el monto a retirar en el ATM: '))


for i in denominacion:
    billete = int(monto/i)
    billetes.append(billete)
    monto = monto % i

print(
    f'Se expulsaran: {billetes[0]}x $50, {billetes[1]}x  $20, {billetes[2]}x  $10, {billetes[3]}x  $5, {billetes[4]}x  $1')
