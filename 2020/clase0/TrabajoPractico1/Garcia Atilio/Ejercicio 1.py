
"""Crear una función que reciba una fecha en formato humano DD/MM/YYYY HH:MM e imprima el dia al que corresponda esa fecha"""

import datetime

fecha= input("Ingrese la fecha con el formato DD/MM/AAAA HH:MM: ")

f2 = datetime.datetime.strptime(fecha, "%d/%m/%Y %H:%M")
dia = datetime.datetime.strftime(f2, "%A")

print(dia)