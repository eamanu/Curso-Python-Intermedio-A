from datetime import datetime,date
fecha=""

while(fecha!="#"):
    fecha = input("Introducir fecha (dd/mm/aaaa) o utilice el # para salir:")
    if(fecha!="#"):
        try:
            formato = "%d/%m/%Y"
            fecha2 = datetime.strptime(fecha,formato)
        except ValueError:
            formato = "%d-%m-%Y"
            fecha2 = datetime.strptime(fecha,formato)
        dia=date.isoweekday(fecha2)
        dias=["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
        print(dias[dia])
    else: 
        print("El programa finalizó")

    