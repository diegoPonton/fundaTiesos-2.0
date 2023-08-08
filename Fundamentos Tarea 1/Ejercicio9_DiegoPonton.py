correoEspol = input('Ingrese su correo ESPOL: ')
valorVerdad = False

indexArroba = correoEspol.find('@')


if '@' in correoEspol:
    if indexArroba != correoEspol[0] or indexArroba != correoEspol[-1]:
        if correoEspol[indexArroba+1:] == 'espol.edu.ec':
            # COMO VERIFICAR SI UN STR CONTIENE UN NUMERO?
            arr = list(correoEspol[:-13])
            if type(correoEspol[:-13]) == str:
                valorVerdad = True
                print(f'El correo {correoEspol} es: {valorVerdad}')
        else:
            print(f'El correo {correoEspol} es: {valorVerdad}')
    else:
        print(f'El correo {correoEspol} es: {valorVerdad}')
else:
    print(f'El correo {correoEspol} es: {valorVerdad}')
