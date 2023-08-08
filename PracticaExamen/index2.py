album = [
    "4 Non Blondes - What's Up", 'Metallica - Nothing Else Matters',
    "Guns N' Roses - Sweet Child O' Mine", "R.E.M. - Losing My Religion",
    "Guns N' Roses - November Rain", "The Police - Every Breath You Take",
    "Scorpions - Wind Of Change", "Bon Jovi - Always",
    "The Verve - Bittersweet Symphony", "Toto - Africa",
    "3 Doors Down - Here Without You"
]

reproducciones = [
    1.52, 1.4, 1.0, 1.66, 1.82, 1.81, 2.11, 1.01, 1.63, 1.337, 1.7
]


print(len(album))

print(len(reproducciones))


print(sum(reproducciones))

maximoReproducciones = max(reproducciones)

indiceMax = reproducciones.index(maximoReproducciones)


print(
    f'La cancion con mas reproducciones es {album[indiceMax]} con {maximoReproducciones} reproducciones')

minReproducciones = min(reproducciones)

indiceMin = reproducciones.index(minReproducciones)


print(
    f'La cancion con menos reproducciones es {album[indiceMin]} con {minReproducciones} reproducciones')
