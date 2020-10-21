def juego(j1="",j2=""):
    estados={"piedra":0,"papel":1,"tijera":2}
    if(estados[j1]==estados[j2]):
        print("Empate")
    else:
        d=estados[j1] - estados[j2]
        if(abs(d)==2):
            if(d<0):
                print("Gana jugador 1")
            else:
                print ("Gana jugador 2")
        elif(abs(d)==1):
            if(d<0):
                print ("Gana jugador 2")
            else:
                print("Gana jugador 1")