import pygame
import time
import random

pygame.init()
#Globales
ancho_display = 880
largo_display = 580
ancho_bordes = 800
grueso = 20
ancho_paletas = 20
largo_paletas = 180
salir_juego = False
blanco = (255,255,255)
negro = (0,0,0)
verde = (0, 255, 0)
reloj = pygame.time.Clock()
FPS = 10 #define la velocidad del juego
borde_inferior1 = 16
borde1_1 = 10
borde2_1 = 10                       #posiciones en la matriz
borde_inferior2 = 991
borde_inferior2_2 = 990
borde_inferior1_2 = 13
seccion = 60

pantalla = pygame.display.set_mode((ancho_display,largo_display)) #pantalla del juego
pygame.display.set_caption("Pong") #titulo de la ventana

#Posiciones
pos_bola = 268
pos_paleta1 = 13
pos_paleta2 = 988
pos_paletaDual1_1 = 1
pos_paletaDual1_2 = 12
pos_paletaDual2_1 = 976
pos_paletaDual2_2 = 987


#Textos
tipografia_juego = pygame.font.Font("Comfortaa-Bold.ttf", 30) #fuente de texto para el juego

def matriz(A,B,a,b): #funcion generadora de la matriz
    while a <= 820:
        while b <= 520:
            A += [[a,b]]
            b += 20
        a += 20
        b = 40
        B += A
        A = [] 
    return B


def conseguir_posicion(i, matriz, x, y):  #Para uso de consola, solamente
    if i < len(tablero):                        #Consigue el indice de la matriz para un par ordenado

        if matriz[i][0] == x and matriz[i][1] == y:
            return i
        else:
            return conseguir_posicion(i + 1, matriz, x, y)
    else:
        return "Error"

def boton(pos_x, pos_y, ancho, alto, color_activo, color_inactivo, opcion):
    P1_P2 = Game.getjugadores()
    modo_juego = Game.getmodo()
    dificultad = Game.getDificultad()
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if pos_x + ancho > mouse[0] > pos_x and pos_y + alto > mouse[1] > pos_y:
        pygame.draw.rect(pantalla, color_activo, [pos_x,pos_y, ancho, alto])
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
            if opcion == "Aceptar":
                Game.aceptar()

    else:
        pygame.draw.rect(pantalla, color_inactivo, [pos_x,pos_y, ancho, alto])


tablero = matriz([],[],40,40)

class Cuadrilateros: #clase cuadrilateros, donde se definen las paletas, la bola y los bordes
    def __init__(self, largo, ancho, posicion):
        self.largo = largo
        self.ancho = ancho
        self.posicion = posicion

    def getLargo(self):  #funciones para obtener los atributos de cada instancia de la clase
        return self.largo
    def getAncho(self):
        return self.ancho
    def getPosicion(self):
        return self.posicion



Bola = Cuadrilateros(grueso,grueso,tablero[pos_bola])  #instancias de la clase cuadrilateros
Borde_Superior = Cuadrilateros(grueso,ancho_bordes,tablero[0])
Borde_Inferior = Cuadrilateros(grueso,ancho_bordes,tablero[24])
Paleta_Player1 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paleta1])
Paleta_Player2 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paleta2])
Paleta1Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paletaDual1_1])
Paleta2Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paletaDual1_1]) #un total de 6 paletas
Paleta1Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paletaDual2_1])
Paleta2Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paletaDual2_2])



class Juego:

    def __init__(self, marcador_1, marcador_2, tablero, dificultad, modo_juego, jugadores):
        self.marcador_1 = marcador_1
        self.marcador_2 = marcador_2
        self.tablero = tablero
        self.dificultad = dificultad
        self.modo_juego = modo_juego
        self.jugadores = jugadores
    
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

    def aceptar(self):
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

Game = Juego(0,0,tablero,1,True, False)

def Menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      

        pantalla.fill(blanco)
        #pygame.draw.rect(pantalla,blanco,[tablero[0][0],tablero[0][1],800,500])

        tipografia = pygame.font.Font("Comfortaa-Bold.ttf", 60)

        titulo = tipografia.render("PONG", True, negro, blanco)
        titulo_rect = titulo.get_rect()
        titulo_rect.center = (tablero[453][0],tablero[453][1])
        pantalla.blit(titulo, titulo_rect)

        tipografia_menor = pygame.font.Font("Comfortaa-Bold.ttf", 30)

        modo_txt = tipografia_menor.render("Modo de juego:" + " "*13 + "P1 vs P2" + " "*13 + "P1 vs PC", True, negro, blanco)
        modo_rect = modo_txt.get_rect()
        modo_rect.center = (tablero[458][0], tablero[458][1])
        pantalla.blit(modo_txt, modo_rect)

        paletas_txt = tipografia_menor.render("Paletas:" + " "*26 + "1" + " "*13 + "2", True, negro, blanco)
        paletas_rect = paletas_txt.get_rect()
        paletas_rect.center = (tablero[336][0], tablero[336][1])
        pantalla.blit(paletas_txt, paletas_rect)

        dificultad_txt = tipografia_menor.render("Dificultad:" + " "*23 + "1" + " "*13 + "2" + " "*13 + "3", True, negro, blanco)
        dificultad_rect = dificultad_txt.get_rect()
        dificultad_rect.center = (tablero[414][0], tablero[414][1])
        pantalla.blit(dificultad_txt, dificultad_rect)

        aceptar_txt = tipografia_menor.render("Aceptar", True, blanco, negro)
        aceptar_rect = aceptar_txt.get_rect()
        aceptar_rect.center = (tablero[496][0], tablero[496][1])
        boton(tablero[394][0], tablero[394][1], 180, 80, verde, negro, "Aceptar")
        pantalla.blit(aceptar_txt, aceptar_rect)

        boton(tablero[632][0],tablero[632][1], 30, 30, negro, verde, "P1 vs P2")
        boton(tablero[932][0],tablero[932][1], 30, 30, negro, verde, "P1 vs PC")
        boton(tablero[535][0],tablero[535][1], 30, 30, negro, verde, "Sencillo")
        boton(tablero[685][0],tablero[685][1], 30, 30, negro, verde, "Doble")
        boton(tablero[538][0],tablero[538][1], 30, 30, negro, verde, "1")
        boton(tablero[688][0],tablero[688][1], 30, 30, negro, verde, "2")
        boton(tablero[863][0],tablero[863][1], 30, 30, negro, verde, "3")

        pygame.display.update()
        reloj.tick(FPS)

def GameLoop(): #ciclo principal del juego que corra mientras el usuario quiera mantenerse dentro
    global pos_bola
    global pos_paleta1
    global pos_paleta2
    global pos_paletaDual1_1
    global pos_paletaDual1_2
    global pos_paletaDual2_1
    global pos_paletaDual2_2
    score1 = Game.getmarcador_1() #solicita el dato de los marcadores de la clase juego
    score2 = Game.getmarcador_2()
    dificultad = Game.getDificultad()
    global salir_juego
    modo = Game.getmodo() #Si modo es true, habra dos paletas, en False sera dual
    moveX_bola = 25
    moveY_bola = 1
    move_p1 = 0
    move_p2 = 0
    punto = False
    distancia_paletas = 0


    while not salir_juego:  #si no se cumple salir juego, sale y cierra la ventana
        while not salir_juego and modo == True: #modo con solo una paleta y persona vs persona

            pygame.display.update()

            if dificultad == 1:   #define las velocidades y los tamaños de las paletas segùn la dificultad
                FPS = 10
                largo_paletas = 180
                borde_inferior1 = 15
                borde_inferior2 = 990
                seccion = 60
            if dificultad == 2:
                FPS = 15
                largo_paletas = 120
                borde_inferior1 = 18
                borde_inferior2 = 993
                seccion = 40

            if dificultad == 3:
                FPS = 20
                largo_paletas = 60
                borde_inferior1 = 21
                borde_inferior2 = 996
                seccion = 20

            if punto == True: #le da una pausa al movimiento de la bola cada vez que se genera un punto
                time.sleep(1)
                punto = False

            for event in pygame.event.get(): #movimiento de los jugadores.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        move_p1 = 1
                    if event.key == pygame.K_w:
                        move_p1 = -1
                    if event.key == pygame.K_UP:
                        move_p2 = -1
                    if event.key == pygame.K_DOWN:
                        move_p2 = 1
                if event.type == pygame.KEYUP: #debe mantenerse presionado el boton para que el movimiento se de
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0
                    if event.key == pygame.K_DOWN:
                        move_p2 = 0
                    if event.key == pygame.K_UP:
                        move_p2 = 0
                    if event.key == pygame.K_SPACE:
                        modo = False
                    if event.key == pygame.K_CAPSLOCK:
                        dificultad += 1



                if event.type == pygame.QUIT:
                    salir_juego = True         #si el usuario sale de la ventana, se finaliza el programa



            if pos_paleta1 == 0: #rebotes de la bola
                pos_paleta1 = 1
                move_p1 = 0
            if pos_paleta1 == borde_inferior1:
                pos_paleta1 = borde_inferior1-1
                move_p1 = 0
            if pos_paleta2 == 975:
                pos_paleta2 = 976
                move_p1 = 0
            if pos_paleta2 == borde_inferior2:
                pos_paleta2 = borde_inferior2-1
                move_p1 = 0



            if tablero[pos_bola][1] == 60:
                moveY_bola = 1
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
            if tablero[pos_bola][0] == 40:
                score1 += 1
                pos_bola = 461
                punto = True
            if tablero[pos_bola][0] == 820:
                score2 += 1
                pos_bola = 461
                punto = True
                #moveX_bola =  random.choice([1,-1])
                #moveY_bola = random.choice([25,-25])
            if  tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and tablero[pos_paleta1][1]<=tablero[pos_bola][1]<(tablero[pos_paleta1][1]+seccion):
                moveX_bola = 25
                moveY_bola = -1
            if tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and (tablero[pos_paleta1][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paleta1][1]+seccion*2):
                moveX_bola = 25
                moveY_bola = 0
            if tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and (tablero[pos_paleta1][1]+seccion*2) <= tablero[pos_bola][1]<=(tablero[pos_paleta1][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = 25
            if  tablero[pos_bola+25][0] == tablero[pos_paleta2][0] and tablero[pos_paleta2][1]<=tablero[pos_bola][1] < (tablero[pos_paleta2][1]+seccion):
                moveX_bola = -25
                moveY_bola = -1
            if tablero[pos_bola+25][0] == tablero[pos_paleta2 ][0] and (tablero[pos_paleta2][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paleta2][1]+seccion*2):
                moveX_bola = -25
                moveY_bola = 0
            if tablero[pos_bola+25][0] == tablero[pos_paleta2][0] and (tablero[pos_paleta2][1]+seccion*2) <= tablero[pos_bola][1]<=(tablero[pos_paleta2][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = -25






            pos_bola += moveY_bola + moveX_bola
            pos_paleta1 += move_p1
            pos_paleta2 += move_p2
            pantalla.fill(negro)
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paleta1][0],tablero[pos_paleta1][1],ancho_paletas,largo_paletas])#paleta 1
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paleta2][0],tablero[pos_paleta2][1],ancho_paletas,largo_paletas])#paleta 2
            pygame.draw.rect(pantalla,blanco,[tablero[pos_bola][0],tablero[pos_bola][1],grueso,grueso]) #Bola
            pygame.draw.rect(pantalla,blanco,[tablero[0][0],tablero[0][1],ancho_bordes,grueso]) #Borde superior
            pygame.draw.rect(pantalla, blanco, [tablero[24][0], tablero[24][1], ancho_bordes, grueso]) #borde inferior

            title = tipografia_juego.render("PONG", True, blanco, negro)
            title_rect = title.get_rect()
            title_rect.center = (420, 20)
            pantalla.blit(title, title_rect)

            marcador_1 = tipografia_juego.render(str(score1), True, blanco, negro)
            Marc1_rect = marcador_1.get_rect()
            Marc1_rect.center = (150, 20)
            pantalla.blit(marcador_1, Marc1_rect)

            marcador_2 = tipografia_juego.render(str(score2), True, blanco, negro)
            Marc2_rect = marcador_2.get_rect()
            Marc2_rect.center = (680, 20)
            pantalla.blit(marcador_2, Marc2_rect)






            pygame.display.update()
            reloj.tick(FPS)

#_____________________________________________________________________________________________________________________________________________________________________________________

        while not salir_juego and modo == False: #modo dual con dificultad minima
            pygame.display.update()

            if punto == True:
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
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0
                    if event.key == pygame.K_DOWN:
                        move_p2 = 0
                    if event.key == pygame.K_UP:
                        move_p2 = 0
                    if event.key == pygame.K_SPACE:
                        modo = True

                if event.type == pygame.QUIT:
                    salir_juego = True



            if pos_paletaDual1_1 == 0:
                pos_paletaDual1_1 = 1
                pos_paletaDual1_2 = 11
                move_p1 = 0
            if pos_paletaDual1_2 == borde_inferior1:
                pos_paletaDual1_2 = borde_inferior1 - 1
                pos_paletaDual1_1 = pos_paletaDual1_2 - distancia_paletas
                move_p1 = 0
            if pos_paletaDual2_1 == borde_inferior2:
                pos_paletaDual2_1 = 976
                pos_paletaDual2_2 = 986
                move_p1 = 0
            if pos_paletaDual2_2 == borde_inferior2:
                pos_paletaDual2_2 = borde_inferior2 -1
                pos_paletaDual2_1 = pos_paletaDual2_2 - distancia_paletas
                move_p1 = 0



            if tablero[pos_bola][1] == 60:
                moveY_bola = 1
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
            if tablero[pos_bola][0] == 40:
                print("Punto 1")
                pos_bola = 461
                punto = True
            if tablero[pos_bola][0] == 820:
                print("Punto 2")
                pos_bola = 461
                punto = True
                #moveX_bola =  random.choice([1,-1])
                #moveY_bola = random.choice([25,-25])

            if  tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and tablero[pos_paletaDual1_1][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual1_1][1]+seccion):
                moveX_bola = 25
                moveY_bola = -1
            if  tablero[pos_bola][0] == tablero[pos_paletaDual1_2+25][0] and tablero[pos_paletaDual1_2][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual1_2][1]+seccion):
                moveX_bola = 25
                moveY_bola = -1


            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and (tablero[pos_paletaDual1_1][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual1_1][1]+seccion*2):
                moveX_bola = 25
                moveY_bola = 0
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2+25][0] and (tablero[pos_paletaDual1_2][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual1_2][1]+seccion*2):
                moveX_bola = 25
                moveY_bola = 0


            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and (tablero[pos_paletaDual1_1][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual1_1][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = 25
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2+25][0] and (tablero[pos_paletaDual1_2][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual1_2][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = 25




            if  tablero[pos_bola+25][0] == tablero[pos_paletaDual2_1][0] and tablero[pos_paletaDual2_1][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual2_1][1]+seccion):
                moveX_bola = -25
                moveY_bola = -1
            if  tablero[pos_bola+25][0] == tablero[pos_paletaDual2_2][0] and tablero[pos_paletaDual2_2][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual2_2][1]+seccion):
                moveX_bola = -25
                moveY_bola = -1


            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_1][0] and (tablero[pos_paletaDual2_1][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual2_1][1]+seccion*2):
                moveX_bola = -25
                moveY_bola = 0
            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_2][0] and (tablero[pos_paletaDual2_2][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual2_2][1]+seccion*2):
                moveX_bola = -25
                moveY_bola = 0


            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_1][0] and (tablero[pos_paletaDual2_1][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual2_1][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = -25
            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_2][0] and (tablero[pos_paletaDual2_2][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual2_2][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = -25






            pos_bola += moveY_bola + moveX_bola #Suma de indices para movimiento sobre la matriz
            pos_paletaDual1_1 += move_p1
            pos_paletaDual1_2 = pos_paletaDual1_1 + distancia_paletas
            pos_paletaDual2_1 += move_p2
            pos_paletaDual2_2 = pos_paletaDual2_1 + distancia_paletas


            pantalla.fill(negro)
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual1_1][0],tablero[pos_paletaDual1_1][1],ancho_paletas,largo_paletas])#paleta 1.1
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual1_2][0],tablero[pos_paletaDual1_2][1],ancho_paletas,largo_paletas])#paleta 1.2

            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual2_1][0],tablero[pos_paletaDual2_1][1],ancho_paletas,largo_paletas])#paleta 2.1
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual2_2][0],tablero[pos_paletaDual2_2][1],ancho_paletas,largo_paletas])#paleta 2.2

            pygame.draw.rect(pantalla,blanco,[tablero[pos_bola][0],tablero[pos_bola][1],grueso,grueso]) #Bola
            pygame.draw.rect(pantalla,blanco,[tablero[0][0],tablero[0][1],ancho_bordes,grueso]) #Borde superior
            pygame.draw.rect(pantalla, blanco, [tablero[24][0], tablero[24][1], ancho_bordes, grueso]) #borde inferior

            title = tipografia_juego.render("PONG", True, blanco, negro) #funciones que generan los textos dentro de la ventana del juego
            title_rect = title.get_rect()
            title_rect.center = (420, 20)
            pantalla.blit(title, title_rect)

            marcador_1 = tipografia_juego.render(str(score1), True, blanco, negro)
            Marc1_rect = marcador_1.get_rect()
            Marc1_rect.center = (150, 20)
            pantalla.blit(marcador_1, Marc1_rect)

            marcador_2 = tipografia_juego.render(str(score2), True, blanco, negro)
            Marc2_rect = marcador_2.get_rect()
            Marc2_rect.center = (680, 20)
            pantalla.blit(marcador_2, Marc2_rect)

            pygame.display.update()
            reloj.tick(FPS)
            


#___________________________________________________________________________________________________________________________________________________________________________________        

    exit()






Menu()

