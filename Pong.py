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
reloj = pygame.time.Clock()
FPS = 10
borde_inferior1 = 16
borde1_1 = 10
borde2_1 = 10
borde_inferior2 = 991
borde_inferior2_2 = 990
borde_inferior1_2 = 13
seccion = 60

pantalla = pygame.display.set_mode((ancho_display,largo_display))
pygame.display.set_caption("Pong")

#Posiciones
pos_bola = 268
pos_paleta1 = 13
pos_paleta2 = 988
pos_paletaDual1_1 = 1
pos_paletaDual1_2 = 12
pos_paletaDual2_1 = 976
pos_paletaDual2_2 = 987


#Textos
tipografia_juego = pygame.font.Font("Comfortaa-Bold.ttf", 30)

def matriz(A,B,a,b):
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


tablero = matriz([],[],40,40)

class Cuadrilateros:
    def __init__(self, largo, ancho, posicion):
        self.largo = largo
        self.ancho = ancho
        self.posicion = posicion

    def getLargo(self):
        return self.largo
    def getAncho(self):
        return self.ancho
    def getPosicion(self):
        return self.posicion



Bola = Cuadrilateros(grueso,grueso,tablero[pos_bola])
Borde_Superior = Cuadrilateros(grueso,ancho_bordes,tablero[0])
Borde_Inferior = Cuadrilateros(grueso,ancho_bordes,tablero[24])
Paleta_Player1 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paleta1])
Paleta_Player2 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paleta2])
Paleta1Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paletaDual1_1])
Paleta2Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paletaDual1_1])
Paleta1Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paletaDual2_1])
Paleta2Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,tablero[pos_paletaDual2_2])



class Juego:

    def __init__(self, marcador_1, marcador_2, tablero, dificultad, modo_juego):
    	self.marcador_1 = marcador_1
    	self.marcador_2 = marcador_2
    	self.tablero = tablero
    	self.dificultad = dificultad
    	self.modo_juego = modo_juego
	
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
    def gana_punto(self, posicion_x, posicion_y):
    	if posicion_x > 1119:
    		marcador_2 += 1
    	if posicion_x < 10:
    		marcador_1 += 1

    def ganador(self, marcador_1, marcador_2):
        while dificultad <= 3:
             if marcador_1 == 7 or marcador_2 == 7:
                posicion_y = 375
                posicion_x = 600
                marcador_1 = 0
                marcador_2 = 0
                dificultad += 1
                print ("Felicidades")
	
    def escoger_dificultad(self, dificultad):
    	print("Hola")

Game = Juego(0,0,tablero,1,True)

def GameLoop():
    global pos_bola
    global pos_paleta1
    global pos_paleta2
    global pos_paletaDual1_1
    global pos_paletaDual1_2
    global pos_paletaDual2_1
    global pos_paletaDual2_2
    score1 = Game.getmarcador_1()
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


    while not salir_juego:
        while not salir_juego and modo == True: #modo con solo una paleta y persona vs persona

            pygame.display.update()

            if dificultad == 1:
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

            if punto == True:
                time.sleep(1)
                punto = False

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
                        modo = False
                    if event.key == pygame.K_CAPSLOCK:
                        dificultad += 1



                if event.type == pygame.QUIT:
                    salir_juego = True



            if pos_paleta1 == 0:
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
                distancia_paletas = 4

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
            if pos_paletaDual1_2 == 17:
                pos_paletaDual1_2 = 16
                pos_paletaDual1_1 = 5
                move_p1 = 0
            if pos_paletaDual2_1 == 975:
                pos_paletaDual2_1 = 976
                pos_paletaDual2_2 = 986
                move_p1 = 0
            if pos_paletaDual2_2 == 992:
                pos_paletaDual2_2 = 991
                pos_paletaDual2_1 = 981
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
            if  tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and tablero[pos_paleta1][1]<tablero[pos_bola][1]< (tablero[pos_paleta1][1]+50):
                moveX_bola = 25
                moveY_bola = -1
            if tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and (tablero[pos_paleta1][1]+51) < tablero[pos_bola][1]<(tablero[pos_paleta1][1]+100):
                moveX_bola = 25
                moveY_bola = 0
            if tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and (tablero[pos_paleta1][1]+101) <tablero[pos_bola][1]<(tablero[pos_paleta1][1]+150):
                moveY_bola = 1
                moveX_bola = 25
            if  tablero[pos_bola+25][0] == tablero[pos_paleta2][0] and tablero[pos_paleta2][1]<tablero[pos_bola][1] < (tablero[pos_paleta2][1]+50):
                moveX_bola = -25
                moveY_bola = -1
            if tablero[pos_bola+25][0] == tablero[pos_paleta2 ][0] and (tablero[pos_paleta2][1]+50) < tablero[pos_bola][1]<(tablero[pos_paleta2][1]+100):
                moveX_bola = -25
                moveY_bola = 0
            if tablero[pos_bola+25][0] == tablero[pos_paleta2][0] and (tablero[pos_paleta2][1]+101) <tablero[pos_bola][1]<(tablero[pos_paleta2][1]+150):
                moveY_bola = 1
                moveX_bola = -25






            pos_bola += moveY_bola + moveX_bola #Suma de indices para movimiento sobre la matriz
            pos_paletaDual1_1 += move_p1
            pos_paletaDual1_2 = pos_paletaDual1_1 + distancia_paletas
            pos_paletaDual2_1 += move_p2
            pos_paletaDual2_2 = pos_paletaDual2_1 + distancia_paletas


            pantalla.fill(negro)
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual1_1][0],tablero[pos_paletaDual1_1][1],ancho_paletas,largo_paletas-30])#paleta 1.1
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual1_2][0],tablero[pos_paletaDual1_2][1],ancho_paletas,largo_paletas-30])#paleta 1.2

            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual2_1][0],tablero[pos_paletaDual2_1][1],ancho_paletas,largo_paletas-30])#paleta 2.1
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paletaDual2_2][0],tablero[pos_paletaDual2_2][1],ancho_paletas,largo_paletas-30])#paleta 2.2

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






GameLoop()


    







