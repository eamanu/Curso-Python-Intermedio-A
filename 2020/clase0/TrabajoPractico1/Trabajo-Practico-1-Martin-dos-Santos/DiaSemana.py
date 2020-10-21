import datetime
def diaSemana(dato="DD/MM/YYYY HH:MM"):
    
    dato=dato.split(' ')
    fecha=[]
    dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    hora=[]
    
    if(dato[0].find('/')>0):
        if(dato[0].find('-')>0):
            print("Escriba la fecha tipo DD/MM/YYYY, no se permiten guiones -")        
        else:
            fecha=dato[0].split('/')
            if(dato[1].find(':')):
                hora=dato[1].split(':')
                print(dias[datetime.datetime(int(fecha[2]),int(fecha[1]),int(fecha[0]),int(hora[0]),int(hora[1])).weekday()])
            else:
                print("El formato de hora ingresado es incorrecto. Debe ser HH:MM")
    