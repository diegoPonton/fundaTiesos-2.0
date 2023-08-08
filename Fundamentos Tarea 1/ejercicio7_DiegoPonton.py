import random

premios = ["lápiz", "carro", "televisor", "pc gamer", "Nuevo Intento"]

premioElegido = input('Ingrese el premio que le interesa: ').lower()

indicePremioElegido = premios.index(premioElegido)

premios.append('laptop')
premios.append('tablet')

indiceLapiz = premios.index('lápiz')
premios.pop(indiceLapiz)

key = random.randint(0, len(premios))

if indicePremioElegido == key:
    print(f'Felicidades se ha llevado ${premios[indicePremioElegido]}')
elif indicePremioElegido == premios[4]:
    print('Tienes un nuevo intento vuelve a correr el programa')
else:
    print('Siga participando')
