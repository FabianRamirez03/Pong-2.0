import pygame
import time
import random

pygame.init()
#Globales
ancho_display = 1200
largo_display = 750
ancho_bordes = 1100
grueso = 20
ancho_paletas = 150
largo_paletas = 25
X_paletaP2 = 1150
X_paletaP1 = 50
salir_juego = False
blanco = (255,255,255)
negro = (0,0,0)
reloj = pygame.time.Clock()
FPS = 60

class Cuadrilateros:
    def __init__(self, largo, ancho, movimiento_x, movimiento_y, posicion_x, posicion_y):
        self.largo = largo
        self.ancho = ancho
        self.movimiento_x = movimiento_x
        self.movimiento_y = movimiento_y
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y

    def getLargo(self):
        return self.largo
    def getAncho(self):
        return self.ancho
    def getMovX(self):
        return self.movimiento_x
    def getMovY(self):
        return self.movimiento_y
    def getPosX(self):
        return self.posicion_x
    def getPosY(self):
        return self.posicion_y
    def moveUP(self, movimiento_y):
        movimiento_y = 2
        return movimiento_y
    def crash():
    if ancho_bola + ancho_paleta + espacio_paleta_pantalla <= posicion_x_bola:
      if posicion_y_bola + ancho_bola <= posicion_y_paleta + largo_paleta and posicion_y_bola > = posicion_y_paleta:
        rebote()

   def rebote():
    if (posicion_y_bola + ancho_bola) <= (posicion_y_paleta + largo_paleta/3) and (posicion_y_bola) > (posicion_y_paleta - ancho_bola):
      velocidad_y = 3
      velocidad_x += 1
    if (posicion_y_bola + ancho_bola) <= (posicion_y_paleta + (largo_paleta/3)*2) and (posicion_y_bola) > (posicion_y_paleta + largo_paleta/3):
      velocidad_y = por definir
      velocidad_x += 1
    if (posicion_y_bola) <= (posicion_y_paleta + largo_paleta) and (posicion_y_bola) > (posicion_y_paleta + 2*(largo_paleta)):
      velocidad_y = -3
      velocidad_x += 1



Bola = Cuadrilateros(grueso,grueso,0,0,200,200)
Borde_Superior = Cuadrilateros(grueso,ancho_bordes,0,0,10,10)
Borde_Inferior = Cuadrilateros(grueso,ancho_bordes,0,0,10,650)
Paleta_Player1 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP1,300)
Paleta_Player2 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP2,300)
Paleta1Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP1,250)
Paleta2Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP1,350)
Paleta1Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP2,250)
Paleta2Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP2,350)



class Juego:
	marcador_1 = 0
	marcador_2 = 0
	tablero = []
	dificultad = 1
	modo_juego = True

	def __init__(self, marcador_1, marcador_2, tablero, dificultad, modo_juego):
		self.marcador_1 = marcador_1
		self.marcador_2 = marcador_2
		self.tablero = tablero
		self.dificultad = dificultad
		self.modo_juego = modo_juego

	def gana_punto(self, posicion_x, posicion_y):
		if posicion_x > 1119:
			marcador_2 += 1
		if posicion_x < 10:
			marcador_1 += 1

	def ganador(self, marcador_1, marcador_2):
		if marcador_1 == 7 or marcador_2 == 7:
			posicion_y = 375
			posicion_x = 600
			marcador_1 = 0
			marcador_2 = 0
			dificultad = 2
			print ("Felicidades")
	
	def escoger_dificultad(self, dificultad):
		dificultad = dificultad
    
    

