import datetime


class fecha():
    dia= ""
    mes= ""
    anio= ""
    hora= ""
    minutos= ""



fecha = fecha()
fecha.dia = int(input("dia:"))
fecha.mes = int(input("mes:"))
fecha.anio = int(input("anio:"))
fecha.hora = int(input("hora:"))
fecha.minutos = int(input("minutos:"))


def quediaes(dia,mes,anio):
    fechafinal = datetime.date(anio, mes, dia)
    print('El día es dia: {:%A}'.format(fechafinal))



quediaes(fecha.dia, fecha.mes, fecha.anio)