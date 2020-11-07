import random


random.seed(a=None, version=2)
print("Bienvenido al juego 'Piedra,Papel o Tijera'")

def usuario():
    turno_humano=input("Es su turno... Ingrese su eleccion, 'Piedra,Papel o Tijera'").lower()
    print("Usuario: ",turno_humano)
    return turno_humano

def maquina():
    eleccion=["piedra","papel","tijera"]
    numero=int(random.random()*3)
    for i in range(len(eleccion)):
        if i == numero:
            turno_maquina = eleccion[i]
    print("Maquina: ",turno_maquina)
    return turno_maquina


def desicion(humano, maquina):
    if humano == "piedra" and maquina == "tijera":
        print("Ganaste")
    elif humano == "papel" and maquina == "piedra":
        print("Ganaste")
    elif humano == "tijera" and maquina == "papel":
        print("Ganaste")
    elif humano == maquina:
        print("Empate")
    else:
        print("Perdiste")

humano=usuario()
maquina=maquina()
desicion(humano,maquina)