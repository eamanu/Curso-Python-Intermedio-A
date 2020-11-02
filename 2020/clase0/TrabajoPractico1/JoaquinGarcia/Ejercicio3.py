#Ejercicio 3
#Juego de Piedra papel y tijeras.
import os
import random
random.seed()
jugadas=('Piedra','Papel','Tijeras')
puntos_usuario = 0
puntos_python = 0
jugada_python = 0
jugada_usuario = 0
nJuegos = 0
result = 0

def ppt (jugada1,jugada2):
    """Recibe jugadas codificadas como numero
        0 - Piedra
        1 - Papel
        2 - Tijeras
        Devuelve 1 si la jugada 1 es ganadora, 2 si es la segunda y 0, en caso de Empate o entrada invalida"""
    if (jugada1 == 0):
        if(jugada2 == 1):
            return 2
        elif(jugada2 == 2):
            return 1
        else:
            return 0
    elif(jugada1 == 1):
        if(jugada2 == 0):
            return 1
        elif(jugada2 == 2):
            return 2
        else:
            return 0
    elif(jugada1 == 2):
        if(jugada2 == 0):
            return 2
        elif(jugada2 == 1):
            return 1
        else:
            return 0
    else:
        return 0
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   
def scores(ptsUsuario,ptsPython,nJuegos,jUsuario,jPython,result):
    print ("************************************************************")
    print ("************************************************************")
    print ("**************** PIEDRA PAPEL O TIJERAS ********************")
    print ("************************************************************")
    print ("************************************************************")
    if(nJuegos==0): 
        return
    resultados=("EMPATE","¡Usted Gana!","¡Python Gana!")
    print (f"\nJugadas: {nJuegos} Puntuacion: Usuario: {ptsUsuario} | Python: {ptsPython}\n")
    print(f"\nUsted-> {jugadas[jUsuario]}    |    {jugadas[jPython]} <- Python\n")
    print (resultados[result])
    

while True:
    screen_clear()
    scores(puntos_usuario,puntos_python,nJuegos,jugada_usuario,jugada_python,result)
    inp = input ("Elija PIEDRA (0), PAPEL (1), o TIJERAS (2). O 'x' para salir.\n")
    if(inp.lower() == 'x'):
        break
    try:
        inp=int(inp)
    except:
        continue
    if(inp>2 or inp<0):
        continue
    jugada_usuario=inp
    jugada_python = random.randrange(0,3,1)
    result = ppt(jugada_python,jugada_usuario)
    nJuegos +=1   
    if result == 1 :
        puntos_python+=1
    elif result == 2:
        puntos_usuario+=1
    
    
