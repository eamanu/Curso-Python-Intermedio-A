#Ejercicio 2
#Programa que me diga si un año es bisiesto.
#Modo de uso: python Ejercicio2.py [año]
#ej: python Ejercicio2.py 1990

import sys

def isLeapYear(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


try:
    y = int(sys.argv[1])
except:
    print("Debe especificar un año válido")
    exit();
if(isLeapYear(y)):
    print(f"{y} es bisiesto")
else:
    print(f"{y} no es bisiesto")