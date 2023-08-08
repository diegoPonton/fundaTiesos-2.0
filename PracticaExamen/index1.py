videoURL = "https://www.youtube.com/watch?v=XxhAJM73Nmk"

album = ["4 Non Blondes - What's Up", 'Metallica - Nothing Else Matters', "Guns N' Roses - Sweet Child O' Mine", "R.E.M. - Losing My Religion", "Guns N' Roses - November Rain",
         "The Police - Every Breath You Take", "Scorpions - Wind Of Change", "Bon Jovi - Always", "The Verve - Bittersweet Symphony", "Toto - Africa", "3 Doors Down - Here Without You"]

segundos = [0, 248, 567, 839, 1077, 1584, 1768, 1999, 2340, 2578, 2808]


texto = input('Ingrese la palabra clave: ')

for i in album:
    if texto in i:
        indice = album.index(i)
        print(f'La cancion {i} tiene indice {indice}')
        print(videoURL + "&t=" + str(segundos[indice]))
