from datetime import datetime


def conversion(fecha):
    dia_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    dia = datetime.weekday(fecha)

    for i in range(len(dia_semana)):
        if i == dia:
            print("El dia de la semana fue", dia_semana[i])


fecha = input("Introduce una fecha en formato DD/MM/YYYY: ")

conversion(fecha)