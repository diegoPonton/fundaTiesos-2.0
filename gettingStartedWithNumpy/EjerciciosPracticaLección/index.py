
import numpy as np

conciertos = [
  "The concert for the New York City", "Band Aid 30", "Live Earth",
  "The Concert for Bangladesh", "We are the Word", "Live 8",
  "One Love Manchester", "12-12-12: The Concert for Sandy Relief",
  "Fire Fight Australia"
]
anios = [2001, 2014, 2007, 1971, 1985, 2005, 2017, 2012, 2020]


conciertos_arr = np.array(conciertos)

anios_arr = np.array(anios)

# print(conciertos_arr)

# print(anios_arr)

# print(conciertos_arr.size)


# for i in range(conciertos_arr.size):
#     print(f'{conciertos[i]} {anios[i]}')


# print(conciertos[3], anios[3])

# print(conciertos[-1], anios[-1])


for i in range(conciertos_arr.size):
    if anios_arr[i] > 2000:
        print(conciertos_arr[i])