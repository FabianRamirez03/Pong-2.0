#<<<<<<< HEAD
print("Hola")
#Comentario
print (2*2)
 
def hola(a):
	print ("hola")

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


#=======
import pygame, sys
from pygame.locals import *
import time
import random

#Dimensiones display (1200, 750)

class Cuadrilateros:
    def __init__(self, largo, ancho, movimiento_x, movimiento_y, posicion_x, posicion_y):
        self.largo = largo
        self.ancho = ancho
        self.movimiento_x = movimiento_x
        self.movimiento_y = movimiento_y
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y



Bola = Cuadrilateros(20,20,0,0,200,200)
Borde_Superior = Cuadrilateros(20,1000,0,0,10,10)
Borde_Inferior = Cuadrilateros(20,1000,0,0,10,650)
Paleta_Player1 = Cuadrilateros(150,25,0,0,50,300)
Paleta_Player2 = Cuadrilateros(150,25,0,0,1000,300)
Paleta1Dual_player1 = Cuadrilateros(150,25,0,0,50,250)
Paleta2Dual_player1 = Cuadrilateros(150,25,0,0,50,350)
Paleta1Dual_player2 = Cuadrilateros(150,25,0,0,1000,250)
Paleta2Dual_player2 = Cuadrilateros(150,25,0,0,1000,350)
#>>>>>>> d74292591db05aeb73d798bc817e65db4b406982

pygame.init()

pantalla = pygame.display.set_mode((1200,750), 0, 32)
pygame.display.set_caption("Pong")

white = (255,255,255)
green = (0,255,0)
pantalla.fill(green)
pygame.draw.rect(pantalla, white, (585, 0, 30, 30))




running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			break
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				break
			py.display.flip()

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
