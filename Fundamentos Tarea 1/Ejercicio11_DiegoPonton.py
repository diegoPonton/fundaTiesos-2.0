cadena = input('Ingrese una cadena: ')


print(f'Numero total de caracteres {len(cadena)}')

for i in range(5):
    print(f'    {cadena}')

print(f'Primer caracter de cadena {cadena[0]}')

print(f'El ultimo caracter de la cadena es {cadena[-1]}')

print(f'Cadena en minusculas {cadena.upper()}')

print(f'Cadena en mayusculas {cadena.lower()}')

print(f"{cadena.replace('a', 'e')}")
