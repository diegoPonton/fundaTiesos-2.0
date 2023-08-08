
correo = input('Ingrese el correo: ')
value = None


arrobaIndex = correo.find('@')

if correo[arrobaIndex:] == '@gmail.com':
    value = True
    print(f'El correo tiene dominio Gmail? {value}')
else:
    value = False
    print(f'El correo tiene dominio Gmail? {value}')
