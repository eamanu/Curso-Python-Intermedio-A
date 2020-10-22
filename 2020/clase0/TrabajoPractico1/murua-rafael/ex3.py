#EJERCICIO 3

import random 
from time import sleep


print('!Bienvenidos Hoy Jugaremos Piedra, Papel o Tijera!')
flag = True
while flag: 
    valUser = input('Ingrese piedra, papel o tijera: ')
    valMin = valUser.lower()   
    li =  ['piedra', 'papel', 'tijera']
    valRandom = random.choice(li)
    print('Su eleccion fue:', valMin, 'y la maquina escogio:', valRandom)
    if valRandom == valMin:
        print('En esta ronda hubo un empate')
    elif valMin == 'tijera' and valRandom == 'papel':
        print('Ganaste esta ronda')
    elif valRandom == 'tijera' and valMin == 'papel':
        print('La maquina gano esta ronda')
    elif valRandom == 'papel' and valMin == 'piedra':
        print('La maquina gano esta ronda')
    elif valMin == 'papel' and valRandom == 'piedra':
        print('Ganaste esta ronda')
    elif valMin == 'piedra' and valRandom == 'tijera':
        print('Ganaste esta ronda')
    elif valRandom == 'piedra' and valMin == 'tijera':
        print('La maquina gano esta ronda')
    option = input('Desea continuar jugando? s/n: ')
    optMin = option.lower()
    if optMin == 's':
        pass
    else:
        flag = False
        print('!Gracias por Jugar!')
        sleep(3)