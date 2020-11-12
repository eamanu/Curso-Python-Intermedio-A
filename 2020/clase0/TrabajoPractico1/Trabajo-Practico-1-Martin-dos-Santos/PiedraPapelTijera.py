import getpass
from enum import Enum,auto

class Jugador:
    def __init__(self):
        self.puntaje=0
        self.seleccion=0
        self.estado=""
     
    def cargar_estado(self):
        if(self.seleccion==0):
            self.estado=Estados.PIEDRA
        elif(self.seleccion==1):
            self.estado=Estados.PAPEL
        elif(self.seleccion==2):
            self.estado=Estados.TIJERA

class Estados(Enum):
    PIEDRA=0
    PAPEL=1
    TIJERA=2
    MENU_PRINCIPAL=auto()
    JUGANDO=auto()
    FINALIZO=auto()
    
class Juego:
    def __init__(self):
        self.game_state=Estados.MENU_PRINCIPAL
        self.j1=Jugador()
        self.j2=Jugador()
        self.seleccion=0
        self.contador_rondas=0
    
    def logica(self):
        
        if(self.j1.estado==self.j2.estado):
            print("Empate")
        else:
            d=self.j1.estado.value - self.j2.estado.value
            if(abs(d)==2):
                if(d<0):
                    self.j1.puntaje+=1
                    self.panel_ganador(1)
                else:
                    self.j2.puntaje+=1
                    self.panel_ganador(2)
            elif(abs(d)==1):
                if(d<0):
                    self.j2.puntaje+=1
                    self.panel_ganador(2)
                else:
                    self.j1.puntaje+=1
                    self.panel_ganador(1)
            self.game_state=Estados.FINALIZO
                
    def menus(self):
        self.seleccion=0
        if(self.game_state==Estados.MENU_PRINCIPAL):
            
            self.panel_menu_principal()
            
            #esta variable sirve para corroborar la seleccion del usuario
            rango=(1,2)
            self.seleccion=int(input('Selección: '))
            self.seleccion=self.check_eleccion(self.seleccion,rango)
            
            if(self.seleccion!=2):
                self.game_state=Estados.JUGANDO
                self.loop_juego()                
        elif(self.game_state==Estados.JUGANDO):            
            self.panel_juego()
            rango=(1,4)
            self.j1.seleccion=self.players_input(rango)
            
            if(self.j1.seleccion!=4):                
                self.panel_juego("2")                
                self.j2.seleccion=self.players_input(rango)    
                
                if(self.j2.seleccion!=4):   
                    self.j1.seleccion-=1
                    self.j2.seleccion-=1
                    self.j1.cargar_estado()
                    self.j2.cargar_estado()
            else:
                self.seleccion=2
                return
    
    def panel_juego(self,turno="1"):
        self.panel_informacion()
        print(" ")
        print("Jugador ",turno)
        print("1.Piedra")
        print("2.Papel")
        print("3.Tijera")
        print("4.Abandonar")
        
    def panel_menu_principal(self):
        print("Bienvenidos a otra copia más de Piedra, papel o tijeras")
        print("\t\t###Este juego necesita 2 jugadores minimo")
        print("1. Comenzar a jugar")
        print("2. Salir")
        
    def panel_informacion(self):
        print("###RONDA ",self.contador_rondas,"###")
        print("###Puntaje###")
        print("Jugador 1: ",self.j1.puntaje)
        print("Jugador 2: ",self.j2.puntaje)
    
    def panel_ganador(self,j_numero):
        print("####################")
        print(self.j1.estado.name + " vs " + self.j2.estado.name)
        print(" ")
        print("El Ganador es: Jugador",j_numero)
        self.panel_informacion()
    
    def players_input(self,rango):
        inputt= None
        inputt=getpass.getpass('Selección: ')
        inputt=self.check_eleccion(int(inputt),rango)
        return inputt
    
    def check_eleccion(self,eleccion,rango):
        if(eleccion <rango[0] or eleccion >rango[1]):
            while(eleccion < rango[0] or eleccion > rango[1]):
                print("Solo se permiten los numeros que indica el menu")
                eleccion=int(input('Intente de nuevo: '))
        return eleccion
    
    def volver_jugar(self):
        print("\n\n")
        print("¿Volver a jugar?")
        print("1. Si")
        print("2. No")
        rango=(1,2)
        s=int(input())
        return (self.check_eleccion(s,rango))
   
    def loop_juego(self):
        while(self.seleccion!=2):
            self.menus()
            if(self.j1.seleccion == 4):
                print("Jugador 1 Abandonó")
            elif(self.j2.seleccion == 4):
                print("Jugador 2 Abandonó")
            else:
                if(self.seleccion!=2):
                    self.logica()
                    self.seleccion=self.volver_jugar()
                
    def iniciar_juego(self):
        self.loop_juego()