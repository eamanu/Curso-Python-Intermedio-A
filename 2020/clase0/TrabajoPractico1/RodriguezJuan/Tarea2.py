import datetime

fecha = datetime.date(1996, 2, 29)

try:
    year = input("Ingrese el año: ")
    fecha = fecha.replace(year=int(year))
    print("El año bisiesto")
except ValueError:
    print("El año no es bisiesto")
    fecha = fecha.replace(year=1996)
