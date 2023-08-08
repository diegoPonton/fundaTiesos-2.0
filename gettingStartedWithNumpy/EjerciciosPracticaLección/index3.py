import numpy as np

arr_albumes = np.array(['The Red Hot Chili Peppers', 'Freaky Styley', 'The Uplift Mofo Party Plan', "Mother's Milk",
                       'Blood Sugar Sex Magik', 'One Hot Minute', 'Californication', 'By the Way', 'Stadium Arcadium', "I'm with You", 'The Getaway'])
arr_ventas = np.array([500000, 650000, 750000, 2600000, 14000000,
                      8000000, 16000000, 12000000, 10000000, 4000000, 1000000])


totalVentas = sum(arr_ventas)

promedioVentas = np.mean(arr_ventas)

print(totalVentas)

print(promedioVentas)

condicion = arr_ventas < promedioVentas

print(arr_albumes[condicion])


condicion2 = arr_ventas >= promedioVentas

newArr = arr_albumes[condicion]

print(newArr.size)