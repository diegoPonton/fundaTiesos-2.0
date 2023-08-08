materia = input('Nombre de la materia: ')

componentePractico = input('La materia tiene componente practico? : ').lower()

if componentePractico == 'si':

    porcentajeTeorico = int(
        input('Ingrese el porcentaje del componente teorico: '))

porcentajePractico = 100 - porcentajeTeorico

notasParciales = int(input('Ingrese notas parciales SOBRE 100: '))

notaPractica = int(input('Ingrese la nota practica: '))
