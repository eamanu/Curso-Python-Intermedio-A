#Ejercicio 1
#Crear una función que reciba una fecha en formato humano DD/MM/YYYY HH:MM e imprima el dia al que corresponda esa fecha

from datetime import datetime
def dia(fecha):
    semana = ('LUNES','MARTES','MIÉRCOLES','JUEVES','VIERNES','SÁBADO','DOMINGO')
    _fecha = datetime.strptime(fecha, "%d/%m/%Y %H:%M")
    print (semana[_fecha.weekday()])


fecha="17/10/2000 12:09"
dia(fecha)
