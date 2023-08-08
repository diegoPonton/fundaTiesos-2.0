animes = [
    "Fullmetal Alchemist: Brotherhood",
    "Death Note",
    "Attack on Titan",
    "Steins;Gate",
    "One Punch Man",
    "Hunter x Hunter",
    "Code Geass",
    "Naruto: Shippuden",
    "My Hero Academia",
    "One Piece",
    "Cowboy Bebop",
    "Dragon Ball Z",
    "Neon Genesis Evangelion",
    "Sword Art Online",
    "Fate/Zero",
    "Gintama",
    "Clannad: After Story",
    "Haikyuu!!",
    "JoJo's Bizarre Adventure",
    "Demon Slayer: Kimetsu no Yaiba"
]

puntuaciones = [
    9.18,
    8.66,
    8.47,
    8.67,
    8.71,
    9.10,
    8.78,
    8.16,
    8.38,
    8.53,
    8.79,
    8.31,
    8.33,
    7.41,
    8.35,
    9.04,
    9.01,
    8.59,
    8.32,
    8.75
]

copia = puntuaciones.copy()

copia.sort(reverse=True)

print(copia)

to10 = copia[:10]

print(to10)

for elemento in to10:
    indice = puntuaciones.index(elemento)
    nombre = animes[indice]

    print(f'{nombre, elemento}')
