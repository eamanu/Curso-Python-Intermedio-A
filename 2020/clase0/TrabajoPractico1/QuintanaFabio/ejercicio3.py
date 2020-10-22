import random

aleatorio = random.randrange(0, 3)
eligePc = ""
print("1) Piedra")
print("2) Papel")
print("3) Tijera")
opcion = int(input("Qué eliges: "))

if opcion == 1:
    eligeUsuario = "Piedra"
elif opcion == 2:
    eligeUsuario = "Papel"
elif opcion == 3:
    eligeUsuario = "Tijera"
print("Elige: ", eligeUsuario)

if aleatorio == 0:
    eligePc = "Piedra"
elif aleatorio == 1:
    eligePc = "Papel"
elif aleatorio == 2:
    eligePc = "Tijera"
print("PC eligio: ", eligePc)
print("...")
if eligePc == "Piedra" and eligeUsuario == "Papel":
    print("Ganaste, papel envuelve Piedra")
elif eligePc == "Papel" and eligeUsuario == "Tijera":
    print("Ganaste, Tijera corta Papel")
elif eligePc == "Tijera" and eligeUsuario == "Piedra":
    print("Ganaste, Piedra pisa Tijera")
if eligePc == "Papel" and eligeUsuario == "Piedra":
    print("Perdiste, papel envuelve Piedra")
elif eligePc == "Tijera" and eligeUsuario == "Papel":
    print("Perdiste, Tijera corta Papel")
elif eligePc == "Piedra" and eligeUsuario == "Tijera":
    print("Perdiste, Piedra pisa Tijera")
elif eligePc == eligeUsuario:
    print("Empataron")