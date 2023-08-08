from pokedex import *


def bienvenidaPokedex():
    print("""
                                  ,'\\
    _.----.        ____         ,'  _\\   ___    ___     ____
_,-'       `.     |    |  /`.   \\,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
""")


def mostrarPokemonNames():
    for pokemon in nombres:
        print(pokemon)


def mostrarTipos():
    newList = []
    for tipo in tipos:
        if tipo not in newList:
            newList.append(tipo)

    for i in newList:
        print(i)


def datosPokemon(nombre):
    if nombre in nombres:
        indice = nombres.index(nombre)

        return f'El tipo de {nombre} es {tipos[indice]}'
    else:
        return -1
