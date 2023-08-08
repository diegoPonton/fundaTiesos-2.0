##### JUEGO DEL CALAMAR ######

import random

pregunta = input('Quiere jugar? ')

counter = 0

dinero = 0

while pregunta == 'si':
    # 0 = BOCA ABAJO ----- 1 = BOCA ARRIBA
    roja = random.randint(0, 1)
    azul = random.randint(0, 1)

    if roja == 1 and azul == 1:
        print('Player WINS 10 DOLARES')
        dinero += 10
    else:
        print('El jugador recibe una cachetada')
        counter += 1

    pregunta = input('Quieres volver a jugar? ')


print('El juego termino',
      f'Cachetadas recibidas: {counter}', f'DINERO GANADO: {dinero}')
