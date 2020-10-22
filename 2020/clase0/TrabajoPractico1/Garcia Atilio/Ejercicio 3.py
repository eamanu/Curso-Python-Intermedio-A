"""Juego de Piedra papel y tijeras."""

from random import randint

lista = ["piedra","papel","tijeras"]
rnd = randint(0,2)
pc = lista[rnd]

player = (input("Elige piedra, papel o tijeras: "))

if (pc == player):
    print("Empate!!")
    print("Yo tambien tenia", pc)

if(player == "piedra"):
    if (pc == "papel"):
        print("Perdiste!!!! Yo tenia ",pc)
    if (pc == "tijeras"):
        print("Ganaste!!! Yo tenia ",pc)

if (player == "tijeras"):
    if (pc == "papel"):
        print("Ganaste!!!! Yo tenia ",pc)
    if (pc == "piedra"):
        print("Perdiste!!! Yo tenia ", pc)

if (player =="papel"):
    if (pc == "piedra"):
        print("Ganaste!!! Yo tenia ", pc)
    if (pc == "tijeras"):
        print("Perdiste!!! Yo tenia ",pc)



