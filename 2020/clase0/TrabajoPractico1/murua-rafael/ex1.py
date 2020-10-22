
# EJERCICIO N°1 
#Crear una función que reciba una fecha en formato humano DD/MM/YYYY HH:MM e imprima el dia al que corresponda esa fecha

import datetime

val = True
while val: 

    date = input('Ingrese una fecha con el siguiente formato Día/mes/Año Hora:Minutos: ')
    h = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M')
    result = datetime.datetime.strftime(h, '%A') 

    days_en = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    days_es = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']

    for day in days_en: 
        if result == day: 
            idxDay = days_en.index(day)
            print('El día asociado a la fecha', h , 'es:', days_es[idxDay])

    option = input('Desea continuar? Y/N: ')
    if option == 'Y':
        pass
    else: 
        val = False