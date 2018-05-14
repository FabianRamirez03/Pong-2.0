import pygame
import time
import random

pygame.init()
#Globales
ancho_display = 880
largo_display = 580
ancho_bordes = 780
grueso = 20
ancho_paletas = 20
largo_paletas = 150
salir_juego = False
blanco = (255,255,255)
negro = (0,0,0)
verde = (0, 255, 0)
reloj = pygame.time.Clock()
FPS = 15

pantalla = pygame.display.set_mode((ancho_display,largo_display))
pygame.display.set_caption("Pong")

#Posiciones
pos_bola = 268
pos_paleta1 = 13
pos_paleta2 = 988
pos_paletaDual1_1 = 1
pos_paletaDual1_2 = 16
pos_paletaDual2_1 = 976
pos_paletaDual2_2 = 991


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
    if i < len(a):                        #Consigue el indice de la matriz para un par ordenado

        if matriz[i][0] == x and matriz[i][1] == y:
            return i
        else:
            return conseguir_posicion(i + 1, matriz, x, y)
    else:
        return "Error"

def boton(pos_x, pos_y, ancho, alto, color_activo, color_inactivo):
	mouse = pygame.mouse.get_pos()
	if pos_x + ancho > mouse[0] > pos_x and pos_y + alto > mouse[1] > pos_y:
		pygame.draw.rect(pantalla, color_activo, [pos_x,pos_y, ancho, alto])
	else:
		pygame.draw.rect(pantalla, color_inactivo, [pos_x,pos_y, ancho, alto])

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

Menu = Cuadrilateros(860, 560, tablero[1])



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
    moveX_bola = 25
    moveY_bola = 1
    move_p1 = 0



    while not salir_juego:
        while dificultad == 1 and not salir_juego:
            

            pygame.display.update()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        move_p1 = 1
                    if event.key == pygame.K_w:
                        move_p1 = -1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0



                if event.type == pygame.QUIT:
                    salir_juego = True



            if pos_paleta1 == 0:
                pos_paleta1 = 1
                move_p1 = 0
            if pos_paleta1 == 16:
                pos_paleta1 = 15
                move_p1 = 0
            if tablero[pos_bola][1] == 60:
                moveY_bola = 1
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
            if tablero[pos_bola][0] == 40:
                moveX_bola = 25
            if tablero[pos_bola][0] == 820:
                moveX_bola = -25



            pos_bola += moveY_bola + moveX_bola
            pos_paleta1 += move_p1
            pantalla.fill(negro)
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paleta1][0],tablero[pos_paleta1][1],ancho_paletas,largo_paletas])
            pygame.draw.rect(pantalla,blanco,[tablero[pos_paleta2][0],tablero[pos_paleta2][1],ancho_paletas,largo_paletas])
            pygame.draw.rect(pantalla,blanco,[tablero[pos_bola][0],tablero[pos_bola][1],grueso,grueso])
            pygame.draw.rect(pantalla,blanco,[tablero[0][0],tablero[0][1],ancho_bordes,grueso])
            pygame.draw.rect(pantalla, blanco, [tablero[24][0], tablero[24][1], ancho_bordes, grueso])
           
            pygame.draw.rect(pantalla,blanco,[tablero[0][0],tablero[0][1],800,500])
            
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
            pantalla.blit(aceptar_txt, aceptar_rect)

            #pygame.draw.rect(pantalla, verde, [tablero[632][0],tablero[632][1], 30, 30])
            #pygame.draw.circle(pantalla, verde, (tablero[933][0],tablero[933][1]), 15, 0)
            #pygame.draw.circle(pantalla, verde, (tablero[536][0],tablero[536][1]), 15, 0)
            #pygame.draw.circle(pantalla, verde, (tablero[686][0],tablero[686][1]), 15, 0)
            #pygame.draw.circle(pantalla, verde, (tablero[539][0],tablero[539][1]), 15, 0)
            #pygame.draw.circle(pantalla, verde, (tablero[689][0],tablero[689][1]), 15, 0)
            #pygame.draw.circle(pantalla, verde, (tablero[864][0],tablero[864][1]), 15, 0)
            #pygame.draw.rect(pantalla, negro, [tablero[24][0], tablero[24][1], 50, 30])


            boton(tablero[632][0],tablero[632][1], 30, 30, negro, verde)
            boton(tablero[932][0],tablero[932][1], 30, 30, negro, verde)
            boton(tablero[535][0],tablero[535][1], 30, 30, negro, verde)
            boton(tablero[685][0],tablero[685][1], 30, 30, negro, verde)
            boton(tablero[538][0],tablero[538][1], 30, 30, negro, verde)
            boton(tablero[688][0],tablero[688][1], 30, 30, negro, verde)
            boton(tablero[863][0],tablero[863][1], 30, 30, negro, verde)
            
            
            '''for event in pygame.event.get():
            	if event.type == pygame.MOUSEBUTTONDOWN((525,85),1):
		            pygame.draw.circle(pantalla, blanco, (tablero[633][0],tablero[633][1]), 15, 0)'''



            pygame.display.update()
            reloj.tick(FPS)


    exit()






GameLoop()
		