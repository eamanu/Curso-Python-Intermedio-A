# Ejercicio 1: fecha

def fecha():
    import datetime
    from googletrans import Translator
    translator = Translator()
    fecha = input("Ingresar fecha en formato DD/MM/YYYY: ")
    dia, mes, año = (int(x) for x in fecha.split("/"))
    dia_en = datetime.date(año, mes, dia).strftime("%A %d %B %Y")
    dia_es = translator.translate(dia_en, dest='es')
    print(dia_es.text)


# Ejercicio 2: año bisiesto

def año_bisiesto():
    import calendar
    año = int(input("Ingresar año: "))
    bisiesto = calendar.isleap(año)
    if bisiesto is True:
        print ("El año " + str(año) + " es bisiesto")
    else:
        print ("El año " + str(año) + " no es bisiesto")

# Ejercicio 3: piedra, papel y tijera

def piedra_papel_tijera():
    import random

    def again():
        asd = input("Volver a jugar? si/no: ")
        if asd == "si":
            piedra_papel_tijera()
        else:
            print("Bye bye")
            quit()

    usuario = input("Ingresar elección: ")
    pc = random.choice(["piedra", "papel", "tijera"])
    if usuario == pc:
        print("Ambos eligieron " + pc + ", Empate! \U0001F91D")
        again()
    elif usuario == "piedra":
        if pc == "tijera":
            print("\U0001F44A     vs     \U0000270C")
            print("Piedra rompe tijera, Usuario gana ")
            again()
        if pc == "papel":
            print("\U0001F44A     vs     \U0001F91A")
            print("Papel envuelve piedra, Pc gana")
            again()
    elif usuario == "papel":
        if pc == "piedra":
            print("\U0001F91A     vs     \U0001F44A")
            print("Papel envuelve piedra, Usuario gana ")
            again()
        if pc == "tijera":
            print("\U0001F91A     vs     \U0000270C")
            print("Tijera corta al papel, Pc gana")
            again()
    elif usuario == "tijera":
        if pc == "piedra":
            print("\U0000270C     vs     \U0001F44A")
            print("Piedra rompe la tijera, Pc gana")
            again()
        if pc == "papel":
            print("\U0000270C     vs     \U0001F91A")
            print("Tijera corta el papel, Usuario gana")
            again()


