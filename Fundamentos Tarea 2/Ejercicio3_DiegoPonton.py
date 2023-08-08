import random

def juego_de_las_ruedas():
    elementos = ["X"] * 11 + ["Rueda"] * 4
    random.shuffle(elementos)

    intentos = 7
    ruedas_encontradas = 0

    while intentos > 0 and ruedas_encontradas < 4:
        print("Lista actual:", elementos)

        indice = solicitar_indice()

        if not (0 <= indice < 15):
            print("Índice inválido. Debe estar entre 0 y 14.")
            continue

        if elementos[indice] == "Rueda":
            ruedas_encontradas += 1
            print("¡Encontraste una Rueda! Total de Ruedas encontradas:", ruedas_encontradas)
        else:
            print("No encontraste una Rueda.")

        intentos -= 1


    if ruedas_encontradas == 4:
        print("¡Felicidades! Ganaste un carro.")
    else:
        print("Se acabaron los intentos. No encontraste las cuatro Ruedas.")

def solicitar_indice():

    while True:
        try:
            indice = int(input("Ingresa un índice entre 0 y 14: "))
            break
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")

    return indice

juego_de_las_ruedas()
