
anio = int(input("Ingresar anio:"))

if (anio %4) == 0:
    if (anio %100 ==0):
        if(anio %400 ==0):
            print("El Año bisiesto")
        else:
            print ("El Año NO es bisiesto")
    else:
        print("El Año bisiesto")
else:
    print("El Año NO es bisiesto")

