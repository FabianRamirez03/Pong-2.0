import pygame
import time
import random

pygame.init()
#Globales
ancho_display = 860
largo_display = 560
ancho_bordes = 820
grueso = 20
ancho_paletas = 20
largo_paletas = 150
salir_juego = False
blanco = (255,255,255)
negro = (0,0,0)
reloj = pygame.time.Clock()
FPS = 60

#Posiciones
pos_bola = 268
pos_paleta1 = 13
pos_paleta2 = 988


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


tablero = matriz([],[],0,0)

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
Paleta1Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP1,250)
Paleta2Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP1,350)
Paleta1Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP2,250)
Paleta2Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP2,350)



class Juego:
    marcador_1 = 0
    marcador_2 = 0
    global tablero
    dificultad = 1
    modo_juego = True

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

def GameLoop():
    global pos_bola
    global pos_paleta1
    while

GameLoop()
