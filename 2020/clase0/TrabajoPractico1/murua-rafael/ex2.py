#EJERCICIO N°2 

from calendar import isleap

val = True
while val: 
    año = int(input('Ingrese año a consultar: '))
    if isleap(año): 
        print('El año', año, 'es bisiesto')
    else: 
        print('El año', año, 'no es bisiesto')
    
    option = input('Desea continuar? Y/N: ')
    if option == 'Y':
        pass
    else: 
        val = False