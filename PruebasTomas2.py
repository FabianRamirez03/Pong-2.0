import pygame
import time
import tkinter
from tkinter import *
import os
import random
import serial

pygame.init()
# Globales
ancho_display = 880
largo_display = 580
ancho_bordes = 800
grueso = 20
ancho_paletas = 20
largo_paletas = 180
salir_juego = False
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 255, 0)
verde_oscuro = (0, 144, 0)
reloj = pygame.time.Clock()
FPS = 10  # define la velocidad del juego
borde_inferior1 = 16
borde1_1 = 10
borde2_1 = 10  # posiciones en la matriz
borde_inferior2 = 991
borde_inferior2_2 = 990
borde_inferior1_2 = 13
seccion = 60
reacciona = 400
colores = [(0, 0, 0), "nada", (0, 255, 0)]
setclor = 1
tipografia_menor = pygame.font.Font("Comfortaa-Bold.ttf", 30)
tipografia = pygame.font.Font("Comfortaa-Bold.ttf", 60)  # tipografias para texto titulo
tipografia_enana = pygame.font.Font("Comfortaa-Bold.ttf", 15)
largo_trampolin = 60
ancho_trampolin = 40

lista = []

pantalla = pygame.display.set_mode((ancho_display, largo_display))  # pantalla del juego
pygame.display.set_caption("Pong")  # titulo de la ventana

# Posiciones
pos_bola = 268
pos_paleta1 = 13
pos_paleta2 = 988
pos_paletaDual1_1 = 1
pos_paletaDual1_2 = 12
pos_paletaDual2_1 = 976
pos_paletaDual2_2 = 987

# Textos
tipografia_juego = pygame.font.Font("Comfortaa-Bold.ttf", 30)  # fuente de texto para el juego

#Arduino
#ser = serial.Serial('COM3', 9600)


def matriz(A, B, a, b):  # funcion generadora de la matriz
    while a <= 820:
        while b <= 520:
            A += [[a, b]]
            b += 20
        a += 20
        b = 40
        B += A
        A = []
    return B


def conseguir_posicion(i, matriz, x, y):  # Para uso de consola, solamente
    if i < len(tablero):  # Consigue el indice de la matriz para un par ordenado

        if matriz[i][0] == x and matriz[i][1] == y:
            return i
        else:
            return conseguir_posicion(i + 1, matriz, x, y)
    else:
        return "Error"


'''La funcion boton se encarga de definir las variables que distinguen a cada modo de juego.
Esta funcion trabaja en el menu de inicio, de manera interna y el usuario escoge las opciones
del modo de juego. Al final llama al ciclo para correr el juego.'''


def boton(pos_x, pos_y, ancho, alto, opcion):

    P1_P2 = Game.getjugadores()
    modo_juego = Game.getmodo()
    dificultad = Game.getDificultad()
    trampolin1 = Game.getTrampolin1()
    trampolin2 = Game.getTrampolin2()
    trampolin3 = Game.getTrampolin3()

    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    if pos_x + ancho > mouse[0] > pos_x and pos_y + alto > mouse[1] > pos_y:
        if click[0] == 1:
            if opcion == "P1 vs P2":
                Game.setJugador(True)
            if opcion == "P1 vs PC":
                Game.setJugador(False)
            if opcion == "Sencillo":
                Game.setModo(True)
            if opcion == "Doble":
                Game.setModo(False)
            if opcion == "1":
                Game.setDificultad(1)
            if opcion == "2":
                Game.setDificultad(2)
            if opcion == "3":
                Game.setDificultad(3)
            if opcion == "Si":
                if dificultad == 1:
                    Game.setTrampolin1(True)
                    Game.setTrampolin2(False)
                    Game.setTrampolin3(False)
                if dificultad == 2:
                    Game.setTrampolin1(True)
                    Game.setTrampolin2(True)
                    Game.setTrampolin3(False)
                if dificultad == 3:
                    Game.setTrampolin1(True)
                    Game.setTrampolin2(True)
                    Game.setTrampolin3(True)
            if opcion == "No":
                if dificultad == 1:
                    Game.setTrampolin1(False)
                    Game.setTrampolin2(False)
                    Game.setTrampolin3(False)
                if dificultad == 2:
                    Game.setTrampolin1(False)
                    Game.setTrampolin2(False)
                    Game.setTrampolin3(False)
                if dificultad == 3:
                    Game.setTrampolin1(False)
                    Game.setTrampolin2(False)
                    Game.setTrampolin3(False)

    if dificultad == 1:
        pygame.draw.rect(pantalla, negro, [tablero[535][0], tablero[535][1], 30, 30])
        pygame.draw.rect(pantalla, blanco, [tablero[685][0], tablero[685][1], 30, 30])
        pygame.draw.rect(pantalla, blanco, [tablero[860][0], tablero[860][1], 30, 30])
    if dificultad == 2:
        pygame.draw.rect(pantalla, blanco, [tablero[535][0], tablero[535][1], 30, 30])
        pygame.draw.rect(pantalla, negro, [tablero[685][0], tablero[685][1], 30, 30])
        pygame.draw.rect(pantalla, blanco, [tablero[860][0], tablero[860][1], 30, 30])
    if dificultad == 3:
        pygame.draw.rect(pantalla, blanco, [tablero[535][0], tablero[535][1], 30, 30])
        pygame.draw.rect(pantalla, blanco, [tablero[685][0], tablero[685][1], 30, 30])
        pygame.draw.rect(pantalla, negro, [tablero[860][0], tablero[860][1], 30, 30])
    if P1_P2 == True:
        pygame.draw.rect(pantalla, negro, [tablero[629][0], tablero[629][1], 30, 30])
        pygame.draw.rect(pantalla, blanco, [tablero[929][0], tablero[929][1], 30, 30])
    if P1_P2 == False:
        pygame.draw.rect(pantalla, blanco, [tablero[629][0], tablero[629][1], 30, 30])
        pygame.draw.rect(pantalla, negro, [tablero[929][0], tablero[929][1], 30, 30])
    if modo_juego == False:
        pygame.draw.rect(pantalla, blanco, [tablero[532][0], tablero[532][1], 30, 30])
        pygame.draw.rect(pantalla, negro, [tablero[682][0], tablero[682][1], 30, 30])
    if modo_juego == True:
        pygame.draw.rect(pantalla, negro, [tablero[532][0], tablero[532][1], 30, 30])
        pygame.draw.rect(pantalla, blanco, [tablero[682][0], tablero[682][1], 30, 30])

    if trampolin1 == True or trampolin2 == True or trampolin3 == True:
        pygame.draw.rect(pantalla, negro, [tablero[538][0], tablero[538][1], 30, 30])
        pygame.draw.rect(pantalla, blanco, [tablero[688][0], tablero[688][1], 30, 30])

    if trampolin1 == False:
    	pygame.draw.rect(pantalla, blanco, [tablero[538][0], tablero[538][1], 30, 30])
    	pygame.draw.rect(pantalla, negro, [tablero[688][0], tablero[688][1], 30, 30])


''' boton_texto crea botonoes con una funcion y un texto escrito. El color activo aparece cuando
el boton tiene el mouse encima y el inactivo cuando no. La opcion indica la funcion que llama.'''


def boton_texto(mensaje,pos_x,pos_y,ancho,alto,color_activo, color_inactivo, opcion):
    global tipografia_menor
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos_x + ancho > mouse[0] > pos_x and pos_y + alto > mouse[1] > pos_y:
        pygame.draw.rect(pantalla, color_activo, [pos_x,pos_y, ancho, alto])

        if click[0] == 1 and opcion == "Inicio":
            Game.setTrampolin1(False)
            Game.setTrampolin2(False)
            Game.setTrampolin3(False)
            Game.setPractica(False)
            Menu()

        if click[0] == 1 and opcion == "Ganador":
            GameLoop()
        if click[0] == 1 and opcion == "Aceptar":
            Game.aceptar()       
        if click[0] == 1 and opcion == "Again":
            GameLoop()  
        if click[0] == 1 and opcion == "Cerrar":
            pygame.mixer.music.stop()
            pygame.quit()
            quit()   
        if click[0] == 1 and opcion == "Practica":
            Game.setPractica(True)
            GameLoop()
        if click[0] == 1 and opcion == "Puntajes":
            ingresar_marcador(None)


    
    else:
        pygame.draw.rect(pantalla, color_inactivo, [pos_x,pos_y, ancho, alto])

    inicio_txt = tipografia_menor.render(mensaje, True, blanco)
    inicio_rect = inicio_txt.get_rect()
    inicio_rect.center = (pos_x + ancho/2, pos_y + alto/2)
    pantalla.blit(inicio_txt, inicio_rect)



tablero = matriz([], [], 40, 40)  # define la matriz del tablero
posx_trampolin = random.randrange(tablero[360][0], tablero[640][0]) 
posx_trampolin2 = random.randrange(tablero[80][0], tablero[360][0])
posx_trampolin3 = random.randrange(tablero[640][0], tablero[920][0])


class Cuadrilateros:  # clase cuadrilateros, donde se definen las paletas, la bola y los bordes
    def __init__(self, largo, ancho, posicion):
        self.largo = largo
        self.ancho = ancho
        self.posicion = posicion

    def getLargo(self):  # funciones para obtener los atributos de cada instancia de la clase
        return self.largo

    def getAncho(self):
        return self.ancho

    def getPosicion(self):
        return self.posicion


Bola = Cuadrilateros(grueso, grueso, tablero[pos_bola])  # instancias de la clase cuadrilateros
Borde_Superior = Cuadrilateros(grueso, ancho_bordes, tablero[0])
Borde_Inferior = Cuadrilateros(grueso, ancho_bordes, tablero[24])
Paleta_Player1 = Cuadrilateros(largo_paletas, ancho_paletas, tablero[pos_paleta1])
Paleta_Player2 = Cuadrilateros(largo_paletas, ancho_paletas, tablero[pos_paleta2])
Paleta1Dual_player1 = Cuadrilateros(largo_paletas, ancho_paletas, tablero[pos_paletaDual1_1])
Paleta2Dual_player1 = Cuadrilateros(largo_paletas, ancho_paletas, tablero[pos_paletaDual1_1])  # un total de 6 paletas
Paleta1Dual_player2 = Cuadrilateros(largo_paletas, ancho_paletas, tablero[pos_paletaDual2_1])
Paleta2Dual_player2 = Cuadrilateros(largo_paletas, ancho_paletas, tablero[pos_paletaDual2_2])


class Juego:

    def __init__(self, marcador_1, marcador_2, tablero, dificultad, modo_juego, jugadores,practica, inspector, fondo, trampolin1, trampolin2, trampolin3, sonido):
        self.marcador_1 = marcador_1
        self.marcador_2 = marcador_2
        self.tablero = tablero
        self.dificultad = dificultad
        self.modo_juego = modo_juego
        self.jugadores = jugadores
        self.practica = practica
        self.inspector = inspector
        self.fondo = fondo
        self.trampolin1 = trampolin1
        self.trampolin2 = trampolin2
        self.trampolin3 = trampolin3
        self.sonido = sonido


    def gettablero(self):
        return self.tablero

    def getmarcador_1(self):
        return self.marcador_1

    def getmarcador_2(self):
        return self.marcador_2

    def getDificultad(self):
        return self.dificultad

    def getmodo(self):
        return self.modo_juego

    def getjugadores(self):
        return self.jugadores

    def getpractica(self):
        return self.practica

    def getInspector(self):
        return self.inspector

    def getFondo(self):
        return self.fondo
    
    def getTrampolin1(self):
    	return self.trampolin1

    def getTrampolin2(self):
    	return self.trampolin2

    def getTrampolin3(self):
    	return self.trampolin3
    def getSonido(self):
        return self.sonido




    def aceptar(self):  # Esta funcion esta ligada al boton aceptar y llama el ciclo del juego con las variables definidas por el usuario
        print(Game.getmodo())
        print(Game.getjugadores())
        print(Game.getDificultad())
        GameLoop()

    def setJugador(self, boolean):
        self.jugadores = boolean

    def setDificultad(self, nuevaDificultad):
        self.dificultad = nuevaDificultad

    def setModo(self, nuevoModo):
        self.modo_juego = nuevoModo

    def setPractica(self, nuevaPractica):
        self.practica = nuevaPractica

    def setInspector(self, nuevoInspector):
        self.inspector = nuevoInspector

    def setFondo(self, nuevoFondo):
        self.fondo = nuevoFondo
        
    def setTrampolin1(self, nuevaTrampolines):
    	self.trampolin1 = nuevaTrampolines

    def setTrampolin2(self, nuevaTrampolines):
    	self.trampolin2 = nuevaTrampolines

    def setTrampolin3(self, nuevaTrampolines):
    	self.trampolin3 = nuevaTrampolines

    def fondo_random(self):
        lista = [(0,0,0),(235,0,0),(0,235,0),(0,0,235),(253,100,0), (124, 0, 59), (124, 125, 154), (252, 0, 254), (0, 121, 122), (70, 0, 27), (0, 59, 82)]
        color = random.choice(lista)
        return self.setFondo(color)
    def cambiarSonido(self):
        if self.sonido == True:
            self.sonido = False
        else:
            self.sonido = True

"""def getArduino():
    entrada = str(ser.readline())
    datos = entrada[entrada.index("") + 1: entrada.index("\\")]
    comando = datos[:datos.index("%")]
    return comando"""





Game = Juego(0, 0, tablero, 1, True, False, False, False, (0,0,0), False, False, False, True) # Instancia de la clase Juego, define los argumentos de Pong.

def ingresar_marcador(tiempo):
    green = "#00ff00"    
    ventana = Tk()
    ventana.title("HighScores")
    ventana.minsize(ancho_display - 390, largo_display - 150)
    ventana.resizable(width=NO, height=NO)
    # ventana.geometry("880x850+500+100")
    canvas = Canvas(ventana, width= ancho_display - 390, height=largo_display - 150, bg="black")
    canvas.place(x=-1, y=-1)

    def invertir_separar(matriz):  # Invierte las funciones de separar para la modificación del archivo txt
        if matriz == []:
            return []
        else:
            return ["|".join(matriz[0])] + invertir_separar(matriz[1:])

    def open_file(path, mode):
        file = open(path, mode)  # Funciòn para abrir los archivos txt
        return file

    def separa_ganadores(i):
        if i == len(ganadores):  # Hace una matriz con los datos del txt de vendedores
            return  # Cada elemento de esta matriz es una sublista con todos los datos de cada vendedor
        ganadores[i] = ganadores[i].replace("\n", "").split("|")  # Elimina los saltos de linea y hace que cada elemento entre | sea un elemento de cada sublista
        separa_ganadores(i + 1)

    listaGan = open_file("marcadores.txt", "r")
    ganadores = listaGan.readlines()
    separa_ganadores(0)
    listaGan.close()





    def invertir_separar(matriz):  # Invierte las funciones de separar para la modificación del archivo txt
        if matriz == []:
            return []
        else:
            return ["|".join(matriz[0])] + invertir_separar(matriz[1:])

    def verificar_aux():
        nombre = entrada_nombre.get()
        if nombre != "" and tiempo != None:
            if nombre != ganadores[0][0] and tiempo != ganadores[0][1]:
                if nombre != ganadores[1][0] and tiempo != ganadores[1][1]:
                    if nombre != ganadores[2][0] and tiempo != ganadores[2][1]:
                        return verificar_ganadores(tiempo, nombre)
            else:
                return "repetido"
        else:
            return "Ingrese su nombre"
    def verificar_ganadores(dato, nombre):
        if dato < int(ganadores[2][1]):
            hacer = True
            if nombre != "":
                if dato <= int(ganadores[0][1]) and hacer:
                    ganadores[2][0] = ganadores[1][0]
                    ganadores[2][1] = ganadores[1][1]
                    ganadores[1][0] = ganadores[0][0]
                    ganadores[1][1] = ganadores[0][1]
                    ganadores[0][0] = nombre
                    ganadores[0][1] = str(dato)
                    hacer = False
                if dato <= int(ganadores[1][1]) and dato > int(ganadores[0][1]) and hacer:
                    ganadores[2][0] = ganadores[1][0]
                    ganadores[2][1] = ganadores[1][1]
                    ganadores[1][0] = nombre
                    ganadores[1][1] = str(dato)
                    hacer = False
                if dato < int(ganadores[2][1] and dato > int(ganadores[1][1])) and hacer:
                    ganadores[2][0] = nombre
                    ganadores[2][1] = str(dato)


        nuevo_texto = "\n".join(invertir_separar(ganadores))
        archivo_ganadores = open_file("marcadores.txt", "w")
        archivo_ganadores.write((str(nuevo_texto)))
        #listaGan = open_file("marcadores.txt", "r")
        #ganadores = listaGan.readlines()
        #separa_ganadores(0)
        lb_primero.config(text = ganadores[0][0] + "        " + str(ganadores[0][1]))
        lb_segundo.config(text=ganadores[1][0] + "        " + str(ganadores[1][1]))
        lb_tercero.config(text= ganadores[2][0] + "        " + str(ganadores[2][1]))
        archivo_ganadores.close()


    entrada_nombre = Entry(canvas, fg="black", font=("Comfortaa-Bold.ttf", 18), width=15)
    entrada_nombre.place(x=150, y=270)



    bt_ingresar = Button(canvas, bg = "white", fg = "black", text = "INGRESAR", relief = FLAT, command = verificar_aux, activebackground = green, font = ("Comfortaa-Bold.ttf", 18), width = 10)
    bt_ingresar.place(x = 300, y = 350)


    lb_titulo = Label(canvas, text = "GAME OVER", bg = "black", font = ("Comfortaa-Bold.ttf", 35), fg = "white")
    lb_titulo.place(x = 120, y = 10)

    lb_ingresar = Label(canvas, text = "NOMBRE:", bg = "black", font = ("Comfortaa-Bold.ttf", 18), fg = "white")
    lb_ingresar.place(x = 20, y = 270)



    lb_highscore = Label(canvas, fg = "white", font = ("Comfortaa-Bold.ttf", 18), bg = "black", text = "HIGHSCORES:")
    lb_highscore.place(x = 20, y = 100)

    lb_primero = Label(canvas, fg = "White", font = ("Comfortaa-Bold.ttf", 18), bg = "Black", text = ganadores[0][0] + "        " + str(ganadores[0][1]))
    lb_primero.place(x = 130, y = 150)

    lb_segundo = Label(canvas, fg="White", font=("Comfortaa-Bold.ttf",18), bg="Black", text=ganadores[1][0] + "        " + str(ganadores[1][1]))
    lb_segundo.place(x=130, y=180)

    lb_tercero = Label(canvas, fg="White", font=("Comfortaa-Bold.ttf",18), bg="Black", text= ganadores[2][0] + "        " + str(ganadores[2][1]))
    lb_tercero.place(x=130, y=210)

    def volver():
        Game.setPractica(False)
        ventana.destroy()


    bt_volver = Button(canvas, bg="white", fg="black", font=("Comfortaa-Bold.ttf", 18), text="VOLVER", activebackground = green, relief = FLAT, command= volver, width = 10)
    bt_volver.place(x=75, y=350)

    ventana.mainloop()


def modoInspector(lista ):
    global tablero
    matriz = tablero
    ventana = Tk()
    ventana.title("Modo Inspector")
    ventana.minsize(ancho_display-70, largo_display-28)
    ventana.resizable(width= NO, height= NO)
    #ventana.geometry("880x850+500+100")
    canvas = Canvas(ventana, width=ancho_display-70, height=largo_display-28, bg="black")
    canvas.place(x=-1, y=-1)


    def verificar(lista, matriz):
        columnas = 550
        cont = 0
        xpos = 10
        ypos = 50

        for i in matriz:
            pivot = esta_aux(cont, lista)
            if pivot == True:
                item = Entry(canvas, text="", justify=CENTER, width=2,  bg = "#000fff000", font = ("arial", 8), fg = "Green")
                item.place(x=xpos, y = ypos)
            if pivot == False:
                item = Entry(canvas, text="", justify=CENTER, width=2, bg = "white", font = ("arial", 8), fg = "White")
                item.place(x=xpos, y=ypos)
            if ypos != columnas:
                ypos += 20
            if ypos == columnas:
                ypos = 50
                xpos += 20

            cont += 1

    def esta_aux(indice, lista):
        result = False
        for i in lista:
            if indice == i:
                result = True
                break
        return result

    def volver():
        ventana.destroy()

    verificar(lista, matriz)

    lb_inspector = Label(canvas, font = ("Arial",24), text = "Modo Inspector", bg = "black", fg = "White")
    lb_inspector.place(x=310, y=5)

    bt_volver = Button(canvas, bd = 1, bg = "black", fg = "white", font = ("Arial",12), text = "Volver", command = volver)
    bt_volver.place(x=10, y=10)

    ventana.mainloop()

def PantallaInicio(): #Ciclo para la pantalla de inicio
    global tipografia
    Iniciar = True
    pantalla.blit(pygame.image.load('Fondo.png'), [0, 0])
    while Iniciar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
        titulo = tipografia.render("PONG", True, blanco) #bloques de definicion de texto
        titulo_rect = titulo.get_rect()
        titulo_rect.center = (tablero[478][0],tablero[478][1])
        pantalla.blit(titulo, titulo_rect)
        boton_texto("INICIO",300,240,300,50, verde, negro, "Inicio")
        boton_texto("CERRAR",300,300,300,50, verde, negro, "Cerrar")
        pygame.display.update()


def Menu(): #Este es el ciclo de inicio para que el usuario defina las variables.
    pantalla.blit(pygame.image.load('Fondo.png'), [0, 0])
    global tipografia_menor
    global tipografia_enana
    global tipografia
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      

        titulo = tipografia.render("PONG", True, blanco) #bloques de definicion de texto
        titulo_rect = titulo.get_rect()
        titulo_rect.center = (tablero[450][0],tablero[450][1])
        pantalla.blit(titulo, titulo_rect)


        modo_txt = tipografia_menor.render("Modo de juego:" + " "*13 + "P1 vs P2" + " "*13 + "P1 vs PC", True, blanco)
        modo_rect = modo_txt.get_rect()
        modo_rect.center = (tablero[455][0], tablero[455][1])
        pantalla.blit(modo_txt, modo_rect)

        paletas_txt = tipografia_menor.render("Paletas:" + " "*26 + "1" + " "*13 + "2", True, blanco)
        paletas_rect = paletas_txt.get_rect()
        paletas_rect.center = (tablero[333][0], tablero[333][1])
        pantalla.blit(paletas_txt, paletas_rect)

        dificultad_txt = tipografia_menor.render("Dificultad:" + " "*23 + "1" + " "*13 + "2" + " "*13 + "3", True, blanco)
        dificultad_rect = dificultad_txt.get_rect()
        dificultad_rect.center = (tablero[411][0], tablero[411][1])
        pantalla.blit(dificultad_txt, dificultad_rect)

        paletas_txt = tipografia_menor.render("Trampolines:" + " "*20 + "Si" + " "*10 + "No", True, blanco)
        paletas_rect = paletas_txt.get_rect()
        paletas_rect.center = (tablero[339][0], tablero[339][1])
        pantalla.blit(paletas_txt, paletas_rect)
 
        boton_texto("ACEPTAR",tablero[244][0],tablero[444][1],200,50,verde, negro, "Aceptar")
        boton_texto("CERRAR",tablero[244][0],tablero[247][1],200,50,verde, negro, "Cerrar")
        boton_texto("PRACTICA",tablero[544][0],tablero[544][1],200,50,verde, negro, "Practica")
        boton_texto("PUNTAJES",tablero[544][0],tablero[547][1],200,50,verde, negro, "Puntajes")

        instrucciones_txt = tipografia_enana.render("DE CLICK EN LOS CUADRADOS BLANCOS PARA SELECCIONAR.", True, blanco)
        instrucciones_rect = instrucciones_txt.get_rect()
        instrucciones_rect.center = (tablero[517][0],tablero[517][1])
        pantalla.blit(instrucciones_txt, instrucciones_rect)

        instrucciones1_txt = tipografia_enana.render("LAS PALETAS SE MUEVEN CON LAS TECLAS DE LAS FLECHAS Y w Y s.", True, blanco)
        instrucciones1_rect = instrucciones1_txt.get_rect()
        instrucciones1_rect.center = (tablero[518][0],tablero[518][1])
        pantalla.blit(instrucciones1_txt, instrucciones1_rect)

        '''Botones del menu inicio para definir las variables del juego'''
        boton(tablero[629][0],tablero[629][1], 30, 30, "P1 vs P2")
        boton(tablero[929][0],tablero[929][1], 30, 30, "P1 vs PC")
        boton(tablero[532][0],tablero[532][1], 30, 30, "Sencillo")
        boton(tablero[682][0],tablero[682][1], 30, 30, "Doble")
        boton(tablero[535][0],tablero[535][1], 30, 30, "1")
        boton(tablero[685][0],tablero[685][1], 30, 30, "2")
        boton(tablero[860][0],tablero[860][1], 30, 30, "3")
        boton(tablero[538][0],tablero[538][1], 30, 30, "Si")
        boton(tablero[688][0],tablero[688][1], 30, 30, "No")

        pygame.display.update()
        reloj.tick(FPS)


def playAgain(ganador):  # Ciclo para las pantallas cuando algun marcador indica 10 puntos.
    otra_vez = True
    while otra_vez:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pantalla.fill(colorFondo)
        volver_font = pygame.font.Font("Comfortaa-Bold.ttf", 75)

        titulo = volver_font.render(ganador, True, blanco, negro)  # bloques de definicion de texto
        titulo_rect = titulo.get_rect()
        titulo_rect.center = (tablero[505][0], tablero[505][1])
        pantalla.blit(titulo, titulo_rect)
        boton_texto("VOLVER AL JUEGO", 300, 240, 300, 50, verde, verde_oscuro, "Again")
        boton_texto("INICIO", 300, 300, 300, 50, verde, verde_oscuro, "Inicio")
        boton_texto("CERRAR", 300, 360, 300, 50, verde, verde_oscuro, "Cerrar")

        pygame.display.update()
        reloj.tick(FPS)


def GameLoop():  # ciclo principal del juego que corra mientras el usuario quiera mantenerse dentro
    global pos_bola
    global pos_paleta1
    global pos_paleta2
    global pos_paletaDual1_1
    global pos_paletaDual1_2
    global pos_paletaDual2_1
    global pos_paletaDual2_2
    
    global posx_trampolin
    global posx_trampolin2
    global posx_trampolin3
    global posy_trampolin
    global ancho_trampolin
    global largo_trampolin
    trampolin1 = Game.getTrampolin1()
    trampolin2 = Game.getTrampolin2()
    trampolin3 = Game.getTrampolin3()
    move_trampolin = 1
    
    score1 = Game.getmarcador_1()  # solicita el dato de los marcadores de la clase juego
    score2 = Game.getmarcador_2()
    dificultad = Game.getDificultad()
    global salir_juego
    global reacciona
    jugador = Game.getjugadores()
    modo = Game.getmodo()  # Si modo es true, habra dos paletas, en False sera dual
    moveX_bola = 25
    moveY_bola = 1
    move_p1 = 0
    move_p2 = 0
    punto = False
    distancia_paletas = 0
    sound_paletas = pygame.mixer.Sound('sonido_paletas.wav')
    sound_bordes = pygame.mixer.Sound('sonido_bordes.wav')
    practica = Game.getpractica()
    mute = Game.getSonido()

    ser = serial.Serial('COM3', 9600)




    while not salir_juego:  # si no se cumple salir juego, sale y cierra la ventana
        pygame.mixer.music.load('RaymanTheme.mp3')
        pygame.mixer.music.play(-1)
        pygame.display.update()
        tiempo1 = time.time()
        colorFondo = Game.getFondo()

        def getArduino():
            entrada = str(ser.readline())
            datos = entrada[entrada.index("") + 1: entrada.index("\\")]
            comando = datos[:datos.index("#")]
            return comando

        while not salir_juego and modo == True and jugador == True and practica == False:  # modo con solo una paleta y persona vs persona

            pygame.display.update()

            lista = [pos_paleta1, pos_paleta2, pos_bola, 0, 24]

            if dificultad == 1:  # define las velocidades y los tamaños de las paletas segùn la dificultad
                FPS = 10
                largo_paletas = 180
                borde_inferior1 = 15
                borde_inferior2 = 990
                seccion = 60
            if dificultad == 2:
                FPS = 15
                largo_paletas = 120  # En caso de aumentar los fps aumentan, haciendo que visualmente sea más rapido
                borde_inferior1 = 18
                borde_inferior2 = 993
                seccion = 40

            if dificultad == 3:
                FPS = 20
                largo_paletas = 60
                borde_inferior1 = 21
                borde_inferior2 = 996
                seccion = 20

            if punto == True:  # le da una pausa al movimiento de la bola cada vez que se genera un punto
                if score1 == 9 or score2 == 9:
                    tiempo2  = time.time()
                    tiempo = tiempo2 - tiempo1
                    if score1 > score2:
                        tiempo = int(tiempo)
                        ingresar_marcador(tiempo)
                        return Menu()
                    else:
                        tiempo = int(tiempo)
                        ingresar_marcador(tiempo)
                        return Menu()
                time.sleep(1)
                punto = False

            for event in pygame.event.get():  # movimiento de los jugadores.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        move_p1 = 1
                    if event.key == pygame.K_w:
                        move_p1 = -1

                    if event.key == pygame.K_UP:
                        move_p2 = -1
                    if event.key == pygame.K_DOWN:
                        move_p2 = 1

                    if event.key == pygame.K_SPACE:
                        modoInspector(lista)
                    if event.key == pygame.K_ESCAPE:
                        Game.fondo_random()
                        colorFondo = Game.getFondo()
                    if event.key == pygame.K_CAPSLOCK:
                        Game.cambiarSonido()
                        mute = Game.getSonido()
                        if not mute:
                            pygame.mixer.music.set_volume(1)
                        if mute:
                            pygame.mixer.music.set_volume(0)
                        print(mute)
                if event.type == pygame.KEYUP:  # debe mantenerse presionado el boton para que el movimiento se de
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0
                    if event.key == pygame.K_DOWN:
                        move_p2 = 0
                    if event.key == pygame.K_UP:
                        move_p2 = 0

                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    salir_juego = True  # si el usuario sale de la ventana, se finaliza el programa

            arduino = getArduino()
            print(arduino)
            if arduino != "'corriendo":
                print(arduino)
                if arduino ==  "'paleta 2.1":
                    move_p2 = -1
                if arduino == "'paleta 2.2":
                    move_p2 = 1
                if arduino == "'paleta 1.1":
                    print("buuu")
                    move_p1 = -1
                if arduino == "'paleta 1.2":
                    move_p1 = 1
                if arduino == "'volumen":
                    Game.cambiarSonido()
                    mute = Game.getSonido()
                    if not mute:
                        pygame.mixer.music.set_volume(1)
                    if mute:
                        pygame.mixer.music.set_volume(0)
                    print(mute)

                if arduino == "'fondo":
                    Game.fondo_random()
                    colorFondo = Game.getFondo()
                if arduino ==  "'inspector":
                    ser.close()
                    Menu()
            if arduino == "'corriendo":
                move_p1 = 0
                move_p2 = 0

                    #modoInspector(lista)









            if pos_paleta1 == 0:  # rebotes de las paletas
                pos_paleta1 = 1
                move_p1 = 0

            if pos_paleta1 == borde_inferior1:
                pos_paleta1 = borde_inferior1 - 1
                move_p1 = 0

            if pos_paleta2 == 975:
                pos_paleta2 = 976
                move_p1 = 0

            if pos_paleta2 == borde_inferior2:
                pos_paleta2 = borde_inferior2 - 1
                move_p1 = 0

            if tablero[pos_bola][1] == 60:
                moveY_bola = 1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == 40:
                score2 += 1
                pos_bola = 461
                punto = True
            if tablero[pos_bola][0] == 820:
                score1 += 1
                pos_bola = 461
                punto = True

            if tablero[pos_bola][0] == tablero[pos_paleta1 + 25][0] and tablero[pos_paleta1][1] <= tablero[pos_bola][
                1] < (tablero[pos_paleta1][1] + seccion):
                moveX_bola = 25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == tablero[pos_paleta1 + 25][0] and (tablero[pos_paleta1][1] + seccion) <= \
                    tablero[pos_bola][1] < (tablero[pos_paleta1][1] + seccion * 2):
                moveX_bola = 25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == tablero[pos_paleta1 + 25][0] and (tablero[pos_paleta1][1] + seccion * 2) <= \
                    tablero[pos_bola][1] <= (tablero[pos_paleta1][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = 25
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paleta2][0] and tablero[pos_paleta2][1] <= tablero[pos_bola][
                1] < (tablero[pos_paleta2][1] + seccion):
                moveX_bola = -25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paleta2][0] and (tablero[pos_paleta2][1] + seccion) <= \
                    tablero[pos_bola][1] < (tablero[pos_paleta2][1] + seccion * 2):
                moveX_bola = -25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paleta2][0] and (tablero[pos_paleta2][1] + seccion * 2) <= \
                    tablero[pos_bola][1] <= (tablero[pos_paleta2][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = -25
                if not mute:
                    sound_bordes.play()
            
            pantalla.fill(colorFondo)
               
            if trampolin1:
            	#print("hola")
            	if tablero[posx_trampolin][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin][1] +=10
            		if tablero[posx_trampolin][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin][1] -= 10
            		if tablero[posx_trampolin][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin][0] and tablero[pos_bola][0] <= tablero[posx_trampolin][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin][1] and tablero[pos_bola][1] <= tablero[posx_trampolin][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin][0],tablero[posx_trampolin][1],ancho_trampolin,largo_trampolin])

            if trampolin2:
            	if tablero[posx_trampolin2][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin2][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin2][1] +=10
            		if tablero[posx_trampolin2][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin2][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin2][1] -= 10
            		if tablero[posx_trampolin2][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin2][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin2][0] and tablero[pos_bola][0] <= tablero[posx_trampolin2][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin2][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin2][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin2][1] and tablero[pos_bola][1] <= tablero[posx_trampolin2][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin2][0],tablero[posx_trampolin2][1],ancho_trampolin,largo_trampolin])

            if trampolin3:
            	#print("hola")
            	if tablero[posx_trampolin3][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin3][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin3][1] +=10
            		if tablero[posx_trampolin3][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin3][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin3][1] -= 10
            		if tablero[posx_trampolin3][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin3][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin3][0] and tablero[pos_bola][0] <= tablero[posx_trampolin3][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin3][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin3][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin3][1] and tablero[pos_bola][1] <= tablero[posx_trampolin3][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin3][0],tablero[posx_trampolin3][1],ancho_trampolin,largo_trampolin])

            pos_bola += moveY_bola + moveX_bola
            pos_paleta1 += move_p1
            pos_paleta2 += move_p2
            pygame.draw.rect(pantalla, blanco, [tablero[pos_paleta1][0], tablero[pos_paleta1][1], ancho_paletas,
                                                largo_paletas])  # paleta 1
            pygame.draw.rect(pantalla, blanco, [tablero[pos_paleta2][0], tablero[pos_paleta2][1], ancho_paletas,
                                                largo_paletas])  # paleta 2
            pygame.draw.rect(pantalla, blanco, [tablero[pos_bola][0], tablero[pos_bola][1], grueso, grueso])  # Bola
            pygame.draw.rect(pantalla, blanco, [tablero[0][0], tablero[0][1], ancho_bordes, grueso])  # Borde superior
            pygame.draw.rect(pantalla, blanco, [tablero[24][0], tablero[24][1], ancho_bordes, grueso])  # borde inferior

            title = tipografia_juego.render("PONG", True, blanco, colorFondo)
            title_rect = title.get_rect()
            title_rect.center = (420, 20)
            pantalla.blit(title, title_rect)

            marcador_1 = tipografia_juego.render(str(score1), True, blanco, colorFondo)
            Marc1_rect = marcador_1.get_rect()
            Marc1_rect.center = (150, 20)
            pantalla.blit(marcador_1, Marc1_rect)


            marcador_2 = tipografia_juego.render(str(score2), True, blanco, colorFondo)
            Marc2_rect = marcador_2.get_rect()
            Marc2_rect.center = (680, 20)
            pantalla.blit(marcador_2, Marc2_rect)



            pygame.display.update()
            reloj.tick(FPS)

        # _____________________________________________________________________________________________________________________________________________________________________________________

        while not salir_juego and modo == False and jugador == True and practica == False:  # modo dual, PvP
            pygame.display.update()

            lista = [pos_paletaDual1_1, pos_paletaDual1_2, pos_paletaDual2_1, pos_paletaDual2_2, pos_bola, 0, 24,posx_trampolin, posx_trampolin2, posx_trampolin3]

            if punto == True:
                if score1 == 10 or score2 == 10:
                    tiempo2 = time.time()
                    tiempo = tiempo2 - tiempo1
                    if score1 > score2:
                        tiempo = int(tiempo)
                        ingresar_marcador(tiempo)
                        return Menu()
                    else:
                        tiempo = int(tiempo)
                        ingresar_marcador(tiempo)
                        return Menu()
                time.sleep(1)
                punto = False

            if dificultad == 1:
                FPS = 10
                largo_paletas = 180
                borde_inferior1 = 15
                borde_inferior2 = 990
                seccion = 60
                distancia_paletas = 11

            if dificultad == 2:
                FPS = 15
                largo_paletas = 120
                borde_inferior1 = 18
                borde_inferior2 = 993
                seccion = 40
                distancia_paletas = 8

            if dificultad == 3:
                FPS = 20
                largo_paletas = 60
                borde_inferior1 = 21
                borde_inferior2 = 996
                seccion = 20
                distancia_paletas = 6

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        move_p1 = 1
                    if event.key == pygame.K_w:
                        move_p1 = -1
                    if event.key == pygame.K_UP:
                        move_p2 = -1
                    if event.key == pygame.K_DOWN:
                        move_p2 = 1
                    if event.key == pygame.K_SPACE:
                        modoInspector(lista)
                    if event.key == pygame.K_ESCAPE:
                        Game.fondo_random()
                        colorFondo = Game.getFondo()
                    if event.key == pygame.K_CAPSLOCK:
                        Game.cambiarSonido()
                        mute = Game.getSonido()
                        if not mute:
                            pygame.mixer.music.set_volume(1)
                        if mute:
                            pygame.mixer.music.set_volume(0)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0
                    if event.key == pygame.K_DOWN:
                        move_p2 = 0
                    if event.key == pygame.K_UP:
                        move_p2 = 0

                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    salir_juego = True



            if pos_paletaDual1_1 == 0:
                pos_paletaDual1_1 = 1
                pos_paletaDual1_2 = 11
                move_p1 = 0
            if pos_paletaDual1_2 == borde_inferior1:
                pos_paletaDual1_2 = borde_inferior1 - 1
                pos_paletaDual1_1 = pos_paletaDual1_2 - distancia_paletas
                move_p1 = 0
            if pos_paletaDual2_1 == 975:
                pos_paletaDual2_1 = 976
                pos_paletaDual2_2 = 986
                move_p1 = 0
            if pos_paletaDual2_2 == borde_inferior2:
                pos_paletaDual2_2 = borde_inferior2 - 1
                pos_paletaDual2_1 = pos_paletaDual2_2 - distancia_paletas
                move_p1 = 0

            if tablero[pos_bola][1] == 60:
                moveY_bola = 1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == 40:
                #print("Punto 1")
                pos_bola = 461
                punto = True
                score2 += 1

            if tablero[pos_bola][0] == 820:
                #print("Punto 2")
                pos_bola = 461
                punto = True
                score1 += 1
                # moveX_bola =  random.choice([1,-1])
                # moveY_bola = random.choice([25,-25])

            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1 + 25][0] and tablero[pos_paletaDual1_1][1] <= \
                    tablero[pos_bola][1] < (tablero[pos_paletaDual1_1][1] + seccion):
                moveX_bola = 25
                moveY_bola = -1
                sound_paletas.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2 + 25][0] and tablero[pos_paletaDual1_2][1] <= \
                    tablero[pos_bola][1] < (tablero[pos_paletaDual1_2][1] + seccion):
                moveX_bola = 25
                moveY_bola = -1
                sound_paletas.play()

            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1 + 25][0] and (
                    tablero[pos_paletaDual1_1][1] + seccion) <= tablero[pos_bola][1] < (
                    tablero[pos_paletaDual1_1][1] + seccion * 2):
                moveX_bola = 25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2 + 25][0] and (
                    tablero[pos_paletaDual1_2][1] + seccion) <= tablero[pos_bola][1] < (
                    tablero[pos_paletaDual1_2][1] + seccion * 2):
                moveX_bola = 25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1 + 25][0] and (
                    tablero[pos_paletaDual1_1][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                    tablero[pos_paletaDual1_1][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = 25
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2 + 25][0] and (
                    tablero[pos_paletaDual1_2][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                    tablero[pos_paletaDual1_2][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = 25
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_1][0] and tablero[pos_paletaDual2_1][1] <= \
                    tablero[pos_bola][1] < (tablero[pos_paletaDual2_1][1] + seccion):
                moveX_bola = -25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_2][0] and tablero[pos_paletaDual2_2][1] <= \
                    tablero[pos_bola][1] < (tablero[pos_paletaDual2_2][1] + seccion):
                moveX_bola = -25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_1][0] and (
                    tablero[pos_paletaDual2_1][1] + seccion) <= tablero[pos_bola][1] < (
                    tablero[pos_paletaDual2_1][1] + seccion * 2):
                moveX_bola = -25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_2][0] and (
                    tablero[pos_paletaDual2_2][1] + seccion) <= tablero[pos_bola][1] < (
                    tablero[pos_paletaDual2_2][1] + seccion * 2):
                moveX_bola = -25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_1][0] and (
                    tablero[pos_paletaDual2_1][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                    tablero[pos_paletaDual2_1][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = -25
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_2][0] and (
                    tablero[pos_paletaDual2_2][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                    tablero[pos_paletaDual2_2][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = -25
                if not mute:
                    sound_bordes.play()

            arduino = getArduino()
            print(arduino)
            if arduino != "'corriendo":
                print(arduino)
                if arduino == "'paleta 2.1":
                    move_p2 = -1
                if arduino == "'paleta 2.2":
                    move_p2 = 1
                if arduino == "'paleta 1.1":
                    print("buuu")
                    move_p1 = -1
                if arduino == "'paleta 1.2":
                    move_p1 = 1
                if arduino == "'volumen":
                    Game.cambiarSonido()
                    mute = Game.getSonido()
                    if not mute:
                        pygame.mixer.music.set_volume(1)
                    if mute:
                        pygame.mixer.music.set_volume(0)
                    print(mute)

                if arduino == "'fondo":
                    Game.fondo_random()
                    colorFondo = Game.getFondo()
                if arduino == "'inspector":
                    ser.close()
                    Menu()
            if arduino == "'corriendo":
                move_p1 = 0
                move_p2 = 0

            pos_bola += moveY_bola + moveX_bola  # Suma de indices para movimiento sobre la matriz
            pos_paletaDual1_1 += move_p1
            pos_paletaDual1_2 = pos_paletaDual1_1 + distancia_paletas
            pos_paletaDual2_1 += move_p2
            pos_paletaDual2_2 = pos_paletaDual2_1 + distancia_paletas

            pantalla.fill(colorFondo)
            
            if trampolin1:
            	#print("hola")
            	if tablero[posx_trampolin][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin][1] +=10
            		if tablero[posx_trampolin][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin][1] -= 10
            		if tablero[posx_trampolin][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin][0] and tablero[pos_bola][0] <= tablero[posx_trampolin][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin][1] and tablero[pos_bola][1] <= tablero[posx_trampolin][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin][0],tablero[posx_trampolin][1],ancho_trampolin,largo_trampolin])

            if trampolin2:
            	if tablero[posx_trampolin2][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin2][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin2][1] +=10
            		if tablero[posx_trampolin2][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin2][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin2][1] -= 10
            		if tablero[posx_trampolin2][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin2][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin2][0] and tablero[pos_bola][0] <= tablero[posx_trampolin2][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin2][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin2][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin2][1] and tablero[pos_bola][1] <= tablero[posx_trampolin2][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin2][0],tablero[posx_trampolin2][1],ancho_trampolin,largo_trampolin])

            if trampolin3:
            	#print("hola")
            	if tablero[posx_trampolin3][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin3][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin3][1] +=10
            		if tablero[posx_trampolin3][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin3][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin3][1] -= 10
            		if tablero[posx_trampolin3][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin3][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin3][0] and tablero[pos_bola][0] <= tablero[posx_trampolin3][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin3][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin3][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin3][1] and tablero[pos_bola][1] <= tablero[posx_trampolin3][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin3][0],tablero[posx_trampolin3][1],ancho_trampolin,largo_trampolin])
            pygame.draw.rect(pantalla, blanco,
                             [tablero[pos_paletaDual1_1][0], tablero[pos_paletaDual1_1][1], ancho_paletas,
                              largo_paletas])  # paleta 1.1
            pygame.draw.rect(pantalla, blanco,
                             [tablero[pos_paletaDual1_2][0], tablero[pos_paletaDual1_2][1], ancho_paletas,
                              largo_paletas])  # paleta 1.2

            pygame.draw.rect(pantalla, blanco,
                             [tablero[pos_paletaDual2_1][0], tablero[pos_paletaDual2_1][1], ancho_paletas,
                              largo_paletas])  # paleta 2.1
            pygame.draw.rect(pantalla, blanco,
                             [tablero[pos_paletaDual2_2][0], tablero[pos_paletaDual2_2][1], ancho_paletas,
                              largo_paletas])  # paleta 2.2

            pygame.draw.rect(pantalla, blanco, [tablero[pos_bola][0], tablero[pos_bola][1], grueso, grueso])  # Bola
            pygame.draw.rect(pantalla, blanco, [tablero[0][0], tablero[0][1], ancho_bordes, grueso])  # Borde superior
            pygame.draw.rect(pantalla, blanco, [tablero[24][0], tablero[24][1], ancho_bordes, grueso])  # borde inferior

            title = tipografia_juego.render("PONG", True, blanco,colorFondo)  # funciones que generan los textos dentro de la ventana del juego
            title_rect = title.get_rect()
            title_rect.center = (420, 20)
            pantalla.blit(title, title_rect)

            marcador_1 = tipografia_juego.render(str(score1), True, blanco, colorFondo)
            Marc1_rect = marcador_1.get_rect()
            Marc1_rect.center = (150, 20)
            pantalla.blit(marcador_1, Marc1_rect)

            marcador_2 = tipografia_juego.render(str(score2), True, blanco, colorFondo)
            Marc2_rect = marcador_2.get_rect()
            Marc2_rect.center = (680, 20)
            pantalla.blit(marcador_2, Marc2_rect)



            pygame.display.update()
            reloj.tick(FPS)

        # ___________________________________________________________________________________________________________________________________________________________________________________

        while not salir_juego and modo == True and jugador == False and practica == False:  # modo con solo una paleta y persona vs computador

            pygame.display.update()

            lista = [pos_paleta1, pos_bola, pos_paleta2, 0, 24]

            if dificultad == 1:  # define las velocidades y los tamaños de las paletas segùn la dificultad
                FPS = 10
                largo_paletas = 180
                borde_inferior1 = 15
                borde_inferior2 = 990
                seccion = 60
                reacciona = 650
            if dificultad == 2:
                FPS = 15
                largo_paletas = 120
                borde_inferior1 = 18
                borde_inferior2 = 993
                seccion = 40
                reacciona = 510

            if dificultad == 3:
                FPS = 20
                largo_paletas = 60
                borde_inferior1 = 21
                borde_inferior2 = 996
                seccion = 20
                reacciona = 420

            if punto == True:  # le da una pausa al movimiento de la bola cada vez que se genera un punto
                if score1 == 10 or score2 == 10:
                    tiempo2 = time.time()
                    tiempo = tiempo2 - tiempo1
                    if score1 > score2:
                        tiempo = int(tiempo)
                        ingresar_marcador(tiempo)
                        return Menu()
                    else:
                        tiempo = int(tiempo)
                        ingresar_marcador(tiempo)
                        return Menu()

                time.sleep(1)
                punto = False

            for event in pygame.event.get():  # movimiento de los jugadores.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        move_p1 = 1

                    if event.key == pygame.K_w:
                        move_p1 = -1

                    if event.key == pygame.K_SPACE:
                        modoInspector(lista)
                    if event.key == pygame.K_ESCAPE:
                        Game.fondo_random()
                        colorFondo = Game.getFondo()
                    if event.key == pygame.K_CAPSLOCK:
                        Game.cambiarSonido()
                        mute = Game.getSonido()
                        if not mute:
                            pygame.mixer.music.set_volume(1)
                        if mute:
                            pygame.mixer.music.set_volume(0)

                if event.type == pygame.KEYUP:  # debe mantenerse presionado el boton para que el movimiento se de
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0

                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    salir_juego = True  # si el usuario sale de la ventana, se finaliza el programa

            if pos_paleta1 == 0:  # rebotes de las paletas con los bordes
                pos_paleta1 = 1
                move_p1 = 0
            if pos_paleta1 == borde_inferior1:
                pos_paleta1 = borde_inferior1 - 1
                move_p1 = 0
            if pos_paleta2 == 975:
                pos_paleta2 = 976
                move_p1 = 0
            if pos_paleta2 == borde_inferior2:
                pos_paleta2 = borde_inferior2 - 1
                move_p1 = 0

            if tablero[pos_bola][1] == 60:  # rebotes de bola en los bordes
                moveY_bola = 1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == 40:
                score2 += 1
                pos_bola = 461
                punto = True
            if tablero[pos_bola][0] == 820:
                score1 += 1
                pos_bola = 461
                punto = True
                # moveX_bola =  random.choice([1,-1])
                # moveY_bola = random.choice([25,-25])
            if tablero[pos_bola][0] == tablero[pos_paleta1 + 25][0] and tablero[pos_paleta1][1] <= tablero[pos_bola][
                1] < (tablero[pos_paleta1][1] + seccion):
                moveX_bola = 25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola][0] == tablero[pos_paleta1 + 25][0] and (tablero[pos_paleta1][1] + seccion) <= \
                    tablero[pos_bola][1] < (tablero[pos_paleta1][1] + seccion * 2):
                moveX_bola = 25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola][0] == tablero[pos_paleta1 + 25][0] and (tablero[pos_paleta1][1] + seccion * 2) <= \
                    tablero[pos_bola][1] <= (tablero[pos_paleta1][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = 25
                if not mute:
                    sound_bordes.play()


            if tablero[pos_bola + 25][0] == tablero[pos_paleta2][0] and tablero[pos_paleta2][1] <= tablero[pos_bola][
                1] < (tablero[pos_paleta2][1] + seccion):
                moveX_bola = -25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paleta2][0] and (tablero[pos_paleta2][1] + seccion) <= \
                    tablero[pos_bola][1] < (tablero[pos_paleta2][1] + seccion * 2):
                moveX_bola = -25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paleta2][0] and (tablero[pos_paleta2][1] + seccion * 2) <= \
                    tablero[pos_bola][1] <= (tablero[pos_paleta2][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = -25
                if not mute:
                    sound_bordes.play()

            arduino = getArduino()
            print(arduino)
            if arduino != "'corriendo":
                print(arduino)
                if arduino == "'paleta 2.1":
                    move_p2 = -1
                if arduino == "'paleta 2.2":
                    move_p2 = 1
                if arduino == "'paleta 1.1":
                    print("buuu")
                    move_p1 = -1
                if arduino == "'paleta 1.2":
                    move_p1 = 1
                if arduino == "'volumen":
                    Game.cambiarSonido()
                    mute = Game.getSonido()
                    if not mute:
                        pygame.mixer.music.set_volume(1)
                    if mute:
                        pygame.mixer.music.set_volume(0)
                    print(mute)

                if arduino == "'fondo":
                    Game.fondo_random()
                    colorFondo = Game.getFondo()
                if arduino == "'inspector":
                    ser.close()
                    Menu()
            if arduino == "'corriendo":
                move_p1 = 0
                move_p2 = 0


            pos_bola += moveY_bola + moveX_bola
            pos_paleta1 += move_p1

            if moveX_bola > 0 and tablero[pos_bola][0] > reacciona:
                if moveY_bola == 0 and tablero[pos_bola][1] != tablero[pos_paleta2][1] and tablero[pos_bola][0] > 500:
                    if tablero[pos_bola][1] < tablero[pos_paleta2][1]:
                        pos_paleta2 += -1
                    if tablero[pos_bola][1] > tablero[pos_paleta2][1]:
                        pos_paleta2 += 1
                else:
                    pos_paleta2 += moveY_bola

            if moveX_bola < 0:
                if pos_paleta2 > 983:
                    pos_paleta2 += -1
                if pos_paleta2 < 983:
                    pos_paleta2 += 1

            pantalla.fill(colorFondo)
            
            if trampolin1:
            	#print("hola")
            	if tablero[posx_trampolin][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin][1] +=10
            		if tablero[posx_trampolin][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin][1] -= 10
            		if tablero[posx_trampolin][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin][0] and tablero[pos_bola][0] <= tablero[posx_trampolin][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin][1] and tablero[pos_bola][1] <= tablero[posx_trampolin][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin][0],tablero[posx_trampolin][1],ancho_trampolin,largo_trampolin])

            if trampolin2:
            	if tablero[posx_trampolin2][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin2][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin2][1] +=10
            		if tablero[posx_trampolin2][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin2][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin2][1] -= 10
            		if tablero[posx_trampolin2][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin2][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin2][0] and tablero[pos_bola][0] <= tablero[posx_trampolin2][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin2][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin2][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin2][1] and tablero[pos_bola][1] <= tablero[posx_trampolin2][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin2][0],tablero[posx_trampolin2][1],ancho_trampolin,largo_trampolin])

            if trampolin3:
            	#print("hola")
            	if tablero[posx_trampolin3][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin3][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin3][1] +=10
            		if tablero[posx_trampolin3][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin3][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin3][1] -= 10
            		if tablero[posx_trampolin3][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin3][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin3][0] and tablero[pos_bola][0] <= tablero[posx_trampolin3][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin3][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin3][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin3][1] and tablero[pos_bola][1] <= tablero[posx_trampolin3][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin3][0],tablero[posx_trampolin3][1],ancho_trampolin,largo_trampolin])
            
            pygame.draw.rect(pantalla, blanco, [tablero[pos_paleta1][0], tablero[pos_paleta1][1], ancho_paletas,
                                                largo_paletas])  # paleta 1
            pygame.draw.rect(pantalla, blanco, [tablero[pos_paleta2][0], tablero[pos_paleta2][1], ancho_paletas,
                                                largo_paletas])  # paleta 2
            pygame.draw.rect(pantalla, blanco, [tablero[pos_bola][0], tablero[pos_bola][1], grueso, grueso])  # Bola
            pygame.draw.rect(pantalla, blanco, [tablero[0][0], tablero[0][1], ancho_bordes, grueso])  # Borde superior
            pygame.draw.rect(pantalla, blanco, [tablero[24][0], tablero[24][1], ancho_bordes, grueso])  # borde inferior

            title = tipografia_juego.render("PONG", True, blanco, colorFondo)
            title_rect = title.get_rect()
            title_rect.center = (420, 20)
            pantalla.blit(title, title_rect)

            marcador_1 = tipografia_juego.render(str(score1), True, blanco, colorFondo)
            Marc1_rect = marcador_1.get_rect()
            Marc1_rect.center = (150, 20)
            pantalla.blit(marcador_1, Marc1_rect)

            marcador_2 = tipografia_juego.render(str(score2), True, blanco, colorFondo)
            Marc2_rect = marcador_2.get_rect()
            Marc2_rect.center = (680, 20)
            pantalla.blit(marcador_2, Marc2_rect)



            pygame.display.update()
            reloj.tick(FPS)

        # _____________________________________________________________________________________________________________________________________________________________________________________________

        while not salir_juego and modo == False and jugador == False and practica == False:  # modo dual, Persona contra computador
            pygame.display.update()

            lista = [pos_paletaDual1_1, pos_paletaDual1_2, pos_paletaDual2_1, pos_paletaDual2_2, pos_bola,0,24]
            if punto == True:
                if score1 == 10 or score2 == 10:
                    tiempo2 = time.time()
                    tiempo = tiempo2 - tiempo1
                    if score1 > score2:
                        tiempo = int(tiempo)
                        ingresar_marcador(tiempo)
                        return Menu()
                    else:
                        tiempo = int(tiempo)
                        ingresar_marcador(tiempo)
                        return Menu()
                time.sleep(1)
                punto = False

            if dificultad == 1:
                FPS = 10
                largo_paletas = 180
                borde_inferior1 = 15
                borde_inferior2 = 990
                seccion = 60
                distancia_paletas = 11
                reacciona = 640

            if dificultad == 2:
                FPS = 15
                largo_paletas = 120
                borde_inferior1 = 18
                borde_inferior2 = 993
                seccion = 40
                distancia_paletas = 8
                reacciona = 540

            if dificultad == 3:
                FPS = 20
                largo_paletas = 60
                borde_inferior1 = 21
                borde_inferior2 = 996
                seccion = 20
                distancia_paletas = 6
                reacciona = 420

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        move_p1 = 1
                    if event.key == pygame.K_w:
                        move_p1 = -1
                    if event.key == pygame.K_SPACE:
                        modoInspector(lista)
                    if event.key == pygame.K_ESCAPE:
                        Game.fondo_random()
                        colorFondo = Game.getFondo()
                    if event.key == pygame.K_CAPSLOCK:
                        Game.cambiarSonido()
                        mute = Game.getSonido()
                        if not mute:
                            pygame.mixer.music.set_volume(1)
                        if mute:
                            pygame.mixer.music.set_volume(0)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0

                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    salir_juego = True

            if pos_paletaDual1_1 == 0:
                pos_paletaDual1_1 = 1
                pos_paletaDual1_2 = 11
                move_p1 = 0
            if pos_paletaDual1_2 == borde_inferior1:
                pos_paletaDual1_2 = borde_inferior1 - 1
                pos_paletaDual1_1 = pos_paletaDual1_2 - distancia_paletas
                move_p1 = 0
            if pos_paletaDual2_1 == 975:
                pos_paletaDual2_1 = 976
                pos_paletaDual2_2 = 986
                move_p1 = 0
            if pos_paletaDual2_2 == borde_inferior2:
                pos_paletaDual2_2 = borde_inferior2 - 1
                pos_paletaDual2_1 = pos_paletaDual2_2 - distancia_paletas
                move_p1 = 0

            if tablero[pos_bola][1] == 60:
                moveY_bola = 1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == 40:
                #print("Punto 1")
                pos_bola = 461
                punto = True
                score2 += 1

            if tablero[pos_bola][0] == 820:
                #print("Punto 2")
                pos_bola = 461
                punto = True
                score1 += 1

            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1 + 25][0] and tablero[pos_paletaDual1_1][1] <= \
                    tablero[pos_bola][1] < (tablero[pos_paletaDual1_1][1] + seccion):
                moveX_bola = 25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2 + 25][0] and tablero[pos_paletaDual1_2][1] <= \
                    tablero[pos_bola][1] < (tablero[pos_paletaDual1_2][1] + seccion):
                moveX_bola = 25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1 + 25][0] and (
                    tablero[pos_paletaDual1_1][1] + seccion) <= tablero[pos_bola][1] < (
                    tablero[pos_paletaDual1_1][1] + seccion * 2):
                moveX_bola = 25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2 + 25][0] and (
                    tablero[pos_paletaDual1_2][1] + seccion) <= tablero[pos_bola][1] < (
                    tablero[pos_paletaDual1_2][1] + seccion * 2):
                moveX_bola = 25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1 + 25][0] and (
                    tablero[pos_paletaDual1_1][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                    tablero[pos_paletaDual1_1][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = 25
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2 + 25][0] and (
                    tablero[pos_paletaDual1_2][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                    tablero[pos_paletaDual1_2][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = 25
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_1][0] and tablero[pos_paletaDual2_1][1] <= \
                    tablero[pos_bola][1] < (tablero[pos_paletaDual2_1][1] + seccion):
                moveX_bola = -25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_2][0] and tablero[pos_paletaDual2_2][1] <= \
                    tablero[pos_bola][1] < (tablero[pos_paletaDual2_2][1] + seccion):
                moveX_bola = -25
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_1][0] and (
                    tablero[pos_paletaDual2_1][1] + seccion) <= tablero[pos_bola][1] < (
                    tablero[pos_paletaDual2_1][1] + seccion * 2):
                moveX_bola = -25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_2][0] and (
                    tablero[pos_paletaDual2_2][1] + seccion) <= tablero[pos_bola][1] < (
                    tablero[pos_paletaDual2_2][1] + seccion * 2):
                moveX_bola = -25
                moveY_bola = 0
                if not mute:
                    sound_bordes.play()

            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_1][0] and (
                    tablero[pos_paletaDual2_1][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                    tablero[pos_paletaDual2_1][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = -25
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola + 25][0] == tablero[pos_paletaDual2_2][0] and (
                    tablero[pos_paletaDual2_2][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                    tablero[pos_paletaDual2_2][1] + seccion * 3):
                moveY_bola = 1
                moveX_bola = -25
                if not mute:
                    sound_bordes.play()

            arduino = getArduino()
            print(arduino)
            if arduino != "'corriendo":
                print(arduino)
                if arduino == "'paleta 2.1":
                    move_p2 = -1
                if arduino == "'paleta 2.2":
                    move_p2 = 1
                if arduino == "'paleta 1.1":
                    print("buuu")
                    move_p1 = -1
                if arduino == "'paleta 1.2":
                    move_p1 = 1
                if arduino == "'volumen":
                    Game.cambiarSonido()
                    mute = Game.getSonido()
                    if not mute:
                        pygame.mixer.music.set_volume(1)
                    if mute:
                        pygame.mixer.music.set_volume(0)
                    print(mute)

                if arduino == "'fondo":
                    Game.fondo_random()
                    colorFondo = Game.getFondo()
                if arduino == "'inspector":
                    ser.close()
                    Menu()
            if arduino == "'corriendo":
                move_p1 = 0
                move_p2 = 0

            pos_bola += moveY_bola + moveX_bola  # Suma de indices para movimiento sobre la matriz
            pos_paletaDual1_1 += move_p1
            pos_paletaDual1_2 = pos_paletaDual1_1 + distancia_paletas

            if moveX_bola > 0 and tablero[pos_bola][0] > reacciona:
                if moveY_bola == 0 and tablero[pos_bola][1] != tablero[pos_paleta2][1] and tablero[pos_bola][0] > 500:
                    if tablero[pos_bola][1] < tablero[pos_paleta2][1]:
                        pos_paletaDual2_1 += -1
                    if tablero[pos_bola][1] > tablero[pos_paleta2][1]:
                        pos_paletaDual2_1 += 1
                else:
                    pos_paletaDual2_1 += moveY_bola

            if moveX_bola < 0:
                if pos_paletaDual2_1 > 983:
                    pos_paletaDual2_1 += -1
                if pos_paletaDual2_1 < 983:
                    pos_paletaDual2_1 += 1

            pos_paletaDual2_2 = pos_paletaDual2_1 + distancia_paletas

            pantalla.fill(colorFondo)
            
            if trampolin1:
            	#print("hola")
            	if tablero[posx_trampolin][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin][1] +=10
            		if tablero[posx_trampolin][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin][1] -= 10
            		if tablero[posx_trampolin][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin][0] and tablero[pos_bola][0] <= tablero[posx_trampolin][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin][1] and tablero[pos_bola][1] <= tablero[posx_trampolin][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin][0],tablero[posx_trampolin][1],ancho_trampolin,largo_trampolin])

            if trampolin2:
            	if tablero[posx_trampolin2][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin2][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin2][1] +=10
            		if tablero[posx_trampolin2][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin2][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin2][1] -= 10
            		if tablero[posx_trampolin2][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin2][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin2][0] and tablero[pos_bola][0] <= tablero[posx_trampolin2][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin2][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin2][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin2][1] and tablero[pos_bola][1] <= tablero[posx_trampolin2][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin2][0],tablero[posx_trampolin2][1],ancho_trampolin,largo_trampolin])

            if trampolin3:
            	#print("hola")
            	if tablero[posx_trampolin3][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin3][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin3][1] +=10
            		if tablero[posx_trampolin3][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin3][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin3][1] -= 10
            		if tablero[posx_trampolin3][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin3][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin3][0] and tablero[pos_bola][0] <= tablero[posx_trampolin3][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin3][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin3][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin3][1] and tablero[pos_bola][1] <= tablero[posx_trampolin3][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin3][0],tablero[posx_trampolin3][1],ancho_trampolin,largo_trampolin])
            
            pygame.draw.rect(pantalla, blanco,
                             [tablero[pos_paletaDual1_1][0], tablero[pos_paletaDual1_1][1], ancho_paletas,
                              largo_paletas])  # paleta 1.1
            pygame.draw.rect(pantalla, blanco,
                             [tablero[pos_paletaDual1_2][0], tablero[pos_paletaDual1_2][1], ancho_paletas,
                              largo_paletas])  # paleta 1.2

            pygame.draw.rect(pantalla, blanco,
                             [tablero[pos_paletaDual2_1][0], tablero[pos_paletaDual2_1][1], ancho_paletas,
                              largo_paletas])  # paleta 2.1
            pygame.draw.rect(pantalla, blanco,
                             [tablero[pos_paletaDual2_2][0], tablero[pos_paletaDual2_2][1], ancho_paletas,
                              largo_paletas])  # paleta 2.2

            pygame.draw.rect(pantalla, blanco, [tablero[pos_bola][0], tablero[pos_bola][1], grueso, grueso])  # Bola
            pygame.draw.rect(pantalla, blanco, [tablero[0][0], tablero[0][1], ancho_bordes, grueso])  # Borde superior
            pygame.draw.rect(pantalla, blanco, [tablero[24][0], tablero[24][1], ancho_bordes, grueso])  # borde inferior

            title = tipografia_juego.render("PONG", True, blanco,colorFondo)  # funciones que generan los textos dentro de la ventana del juego
            title_rect = title.get_rect()
            title_rect.center = (420, 20)
            pantalla.blit(title, title_rect)

            marcador_1 = tipografia_juego.render(str(score1), True, blanco, colorFondo)
            Marc1_rect = marcador_1.get_rect()
            Marc1_rect.center = (150, 20)
            pantalla.blit(marcador_1, Marc1_rect)

            marcador_2 = tipografia_juego.render(str(score2), True, blanco, colorFondo)
            Marc2_rect = marcador_2.get_rect()
            Marc2_rect.center = (680, 20)
            pantalla.blit(marcador_2, Marc2_rect)



            pygame.display.update()
            reloj.tick(FPS)

        # _____________________________________________________________________________________________________________________________________________________________________________________________

        while practica == True and not salir_juego: #modo practica

            lista = [pos_paletaDual1_2, pos_paletaDual1_1, pos_bola, pos_paletaDual2_1, 0, 24]

            if punto == True:
                time.sleep(1)
                moveX_bola = 25

                punto = False

            if dificultad == 1:
                FPS = 10
                largo_paletas = 180
                borde_inferior1 = 15
                borde_inferior2 = 990
                seccion = 60
                distancia_paletas = 11
                reacciona = 640

            if dificultad == 2:
                FPS = 15
                largo_paletas = 120
                borde_inferior1 = 18
                borde_inferior2 = 993
                seccion = 40
                distancia_paletas = 8
                reacciona = 540

            if dificultad == 3:
                FPS = 20
                largo_paletas = 60
                borde_inferior1 = 21
                borde_inferior2 = 996
                seccion = 20
                distancia_paletas = 6
                reacciona = 420

            if modo == True:
                pos_paletaDual1_2 = 978


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        move_p1 = 1
                    if event.key == pygame.K_w:
                        move_p1 = -1
                    if event.key == pygame.K_SPACE:
                        modoInspector(lista)
                    if event.key == pygame.K_ESCAPE:
                        Game.fondo_random()
                        colorFondo = Game.getFondo()
                    if event.key == pygame.K_CAPSLOCK:
                        Game.cambiarSonido()
                        mute = Game.getSonido()
                        if not mute:
                            pygame.mixer.music.set_volume(1)
                        if mute:
                            pygame.mixer.music.set_volume(0)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0

                if event.type == pygame.QUIT:
                    salir_juego = True

            if pos_paletaDual1_1 == 0:
                pos_paletaDual1_1 = 1

                move_p1 = 0

            if modo == False: #colisiones de paletas con los bordes
                if pos_paletaDual1_2 == borde_inferior1:
                    pos_paletaDual1_2 = borde_inferior1 - 1
                    pos_paletaDual1_1 = pos_paletaDual1_2 - distancia_paletas
                    move_p1 = 0

            if modo == True:
                if pos_paletaDual1_1 == borde_inferior1:
                    pos_paletaDual1_1 = borde_inferior1 - 1
                    move_p1 = 0





            pos_paletaDual1_1 += move_p1

            if pos_paletaDual1_2 != 978:
                pos_paletaDual1_2 = pos_paletaDual1_1 + distancia_paletas



            if tablero[pos_bola][1] == 60:
                moveY_bola = 1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
                if not mute:
                    sound_bordes.play()
            if tablero[pos_bola][0] == 40:
                pos_bola = 461
                punto = True


            if tablero[pos_bola][0] == 800:
                moveX_bola = -25



            if modo == True:
                if tablero[pos_bola][0]==tablero[pos_paletaDual1_1+25][0] and tablero[pos_paletaDual1_1][1] <=tablero[pos_bola][1]<(tablero[pos_paletaDual1_1][1]+seccion):
                    moveX_bola = 25
                    moveY_bola = -1
                    if not mute:
                        sound_bordes.play()
                if tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and (tablero[pos_paletaDual1_1][1] + seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual1_1][1]+seccion*2):
                    moveX_bola = 25
                    moveY_bola = 0
                    if not mute:
                        sound_bordes.play()
                if tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and (tablero[pos_paletaDual1_1][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual1_1][1]+seccion*3):
                    moveY_bola = 1
                    moveX_bola = 25
                    if not mute:
                        sound_bordes.play()

            if modo == False:
                if tablero[pos_bola][0] == tablero[pos_paletaDual1_1 + 25][0] and tablero[pos_paletaDual1_1][1] <= \
                        tablero[pos_bola][1] < (tablero[pos_paletaDual1_1][1] + seccion):
                    moveX_bola = 25
                    moveY_bola = -1
                    if not mute:
                        sound_bordes.play()
                if tablero[pos_bola][0] == tablero[pos_paletaDual1_2 + 25][0] and tablero[pos_paletaDual1_2][1] <= \
                        tablero[pos_bola][1] < (tablero[pos_paletaDual1_2][1] + seccion):
                    moveX_bola = 25
                    moveY_bola = -1
                    if not mute:
                        sound_bordes.play()

                if tablero[pos_bola][0] == tablero[pos_paletaDual1_1 + 25][0] and (
                        tablero[pos_paletaDual1_1][1] + seccion) <= tablero[pos_bola][1] < (
                        tablero[pos_paletaDual1_1][1] + seccion * 2):
                    moveX_bola = 25
                    moveY_bola = 0
                    if not mute:
                        sound_bordes.play()
                if tablero[pos_bola][0] == tablero[pos_paletaDual1_2 + 25][0] and (
                        tablero[pos_paletaDual1_2][1] + seccion) <= tablero[pos_bola][1] < (
                        tablero[pos_paletaDual1_2][1] + seccion * 2):
                    moveX_bola = 25
                    moveY_bola = 0
                    if not mute:
                        sound_bordes.play()

                if tablero[pos_bola][0] == tablero[pos_paletaDual1_1 + 25][0] and (
                        tablero[pos_paletaDual1_1][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                        tablero[pos_paletaDual1_1][1] + seccion * 3):
                    moveY_bola = 1
                    moveX_bola = 25
                    if not mute:
                        sound_bordes.play()
                if tablero[pos_bola][0] == tablero[pos_paletaDual1_2 + 25][0] and (
                        tablero[pos_paletaDual1_2][1] + seccion * 2) <= tablero[pos_bola][1] <= (
                        tablero[pos_paletaDual1_2][1] + seccion * 3):
                    moveY_bola = 1
                    moveX_bola = 25
                    if not mute:
                        sound_bordes.play()

            arduino = getArduino()
            print(arduino)
            if arduino != "'corriendo":
                print(arduino)
                if arduino == "'paleta 2.1":
                    move_p2 = -1
                if arduino == "'paleta 2.2":
                    move_p2 = 1
                if arduino == "'paleta 1.1":
                    print("buuu")
                    move_p1 = -1
                if arduino == "'paleta 1.2":
                    move_p1 = 1
                if arduino == "'volumen":
                    Game.cambiarSonido()
                    mute = Game.getSonido()
                    if not mute:
                        pygame.mixer.music.set_volume(1)
                    if mute:
                        pygame.mixer.music.set_volume(0)
                    print(mute)

                if arduino == "'fondo":
                    Game.fondo_random()
                    colorFondo = Game.getFondo()
                if arduino == "'inspector":
                    ser.close()
                    Menu()
            if arduino == "'corriendo":
                move_p1 = 0
                move_p2 = 0


            pos_bola += moveY_bola + moveX_bola




            pantalla.fill(colorFondo)
            
            if trampolin1:
            	#print("hola")
            	if tablero[posx_trampolin][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin][1] +=10
            		if tablero[posx_trampolin][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin][1] -= 10
            		if tablero[posx_trampolin][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin][0] and tablero[pos_bola][0] <= tablero[posx_trampolin][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin][1] and tablero[pos_bola][1] <= tablero[posx_trampolin][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin][0],tablero[posx_trampolin][1],ancho_trampolin,largo_trampolin])

            if trampolin2:
            	if tablero[posx_trampolin2][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin2][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin2][1] +=10
            		if tablero[posx_trampolin2][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin2][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin2][1] -= 10
            		if tablero[posx_trampolin2][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin2][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin2][0] and tablero[pos_bola][0] <= tablero[posx_trampolin2][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin2][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin2][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin2][1] and tablero[pos_bola][1] <= tablero[posx_trampolin2][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin2][0],tablero[posx_trampolin2][1],ancho_trampolin,largo_trampolin])

            if trampolin3:
            	#print("hola")
            	if tablero[posx_trampolin3][1] > tablero[949][1] - largo_trampolin:
            		tablero[posx_trampolin3][1] -= 80
            	if move_trampolin == 1:
            		tablero[posx_trampolin3][1] +=10
            		if tablero[posx_trampolin3][1] == tablero[949][1] - largo_trampolin:
            			move_trampolin = -1
            			tablero[posx_trampolin3][1] -= 10
            	if move_trampolin == -1:
            		tablero[posx_trampolin3][1] -= 10
            		if tablero[posx_trampolin3][1] <= tablero[75][1]:
            			move_trampolin = 1
            			tablero[posx_trampolin3][1] += 10
            	if tablero[pos_bola][0] + grueso >= tablero[posx_trampolin3][0] and tablero[pos_bola][0] <= tablero[posx_trampolin3][0] + ancho_trampolin:
            		if tablero[pos_bola][1] + grueso == tablero[posx_trampolin3][1]:
            			if moveY_bola == 0:
            				moveY_bola -= 1
            			else:
            				moveY_bola = -1
            		if tablero[pos_bola][1] == tablero[posx_trampolin3][1] + largo_trampolin:
            			if moveY_bola == 0:
            				moveY_bola += 1
            			else:
            				moveY_bola = +1
            				moveX_bola *= (-1)
            		if tablero[pos_bola][1] + grueso >= tablero[posx_trampolin3][1] and tablero[pos_bola][1] <= tablero[posx_trampolin3][1] + largo_trampolin:
            			moveX_bola *= -1

            	pygame.draw.rect(pantalla,blanco,[tablero[posx_trampolin3][0],tablero[posx_trampolin3][1],ancho_trampolin,largo_trampolin])
            
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual1_1][0],tablero[pos_paletaDual1_1][1],ancho_paletas,largo_paletas])#paleta1.1
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual1_2][0],tablero[pos_paletaDual1_2][1],ancho_paletas,largo_paletas])#paleta1.2

            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual2_1][0],tablero[pos_paletaDual2_1][1],ancho_paletas,480])#pared

            pygame.draw.rect(pantalla,blanco,[tablero[pos_bola][0],tablero[pos_bola][1],grueso,grueso])  # Bola
            pygame.draw.rect(pantalla,blanco,[tablero[0][0],tablero[0][1],ancho_bordes,grueso])  # Borde superior
            pygame.draw.rect(pantalla,blanco,[tablero[24][0],tablero[24][1],ancho_bordes,grueso])  # borde inferior





            title = tipografia_juego.render("PONG",True, blanco, colorFondo)#funciones que generan los textos dentro de la ventana del juego
            title_rect = title.get_rect()
            title_rect.center = (420, 20)
            pantalla.blit(title, title_rect)



            pygame.display.update()
            reloj.tick(FPS)

    ser.close()
        # ____________________________________________________________________________________________________________________________________________________________________________________________
    exit()


PantallaInicio()
