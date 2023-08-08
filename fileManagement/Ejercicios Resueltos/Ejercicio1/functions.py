import numpy as n


def splitting(cadena):
    trozos = cadena.split('artist:')[1].split('song:')

    nombre_artista = trozos[0].strip()

    return nombre_artista
    


def nombresArtistas():
    with open('legendarysongs.txt', mode='r') as f:
        contenido = f.readlines()
        
        artistas = list(map(splitting,contenido))

        newList = []
        
        for artista in artistas:
            if artista not in newList:
                newList.append(artista)

        return newList

def cantidadCancionesArtista():
    with open('legendarysongs.txt', mode='r') as f:
        contenido = f.readlines()

        artistas = list(map(splitting, contenido))

        lista = nombresArtistas()

        numeroCanciones = []

        for artista in lista:
            numeroCanciones.append(artistas.count(artista))

        return numeroCanciones

def ReproduccionesPorArtista():
    with open('legendarysongs.txt', mode='r') as f:
        content = f.readlines()

        listaArtistas = nombresArtistas()

        reproducciones = []

        for artista in listaArtistas:
            for linea in content:
                if artista in linea:
                    plays = int(linea.split('plays: ')[-1].strip())
                    reproducciones.append(plays)
    return reproducciones    
            

def totalReproduccionesPorArtista(lista):
    artistas = nombresArtistas()
    total_reproducciones_por_artista = {}
    
    index_artista = 0
    for reproducciones in lista:
        # Si el índice supera el número de artistas, volvemos a empezar
        index_artista %= len(artistas)
        artista_actual = artistas[index_artista]
        
        # Si el artista no existe en el diccionario, lo agregamos con las reproducciones actuales
        if artista_actual not in total_reproducciones_por_artista:
            total_reproducciones_por_artista[artista_actual] = reproducciones
        else:
            # Si el artista ya existe en el diccionario, sumamos las reproducciones actuales a las existentes
            total_reproducciones_por_artista[artista_actual] += reproducciones
        
        index_artista += 1
    
    return total_reproducciones_por_artista
