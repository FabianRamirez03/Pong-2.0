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




Bola = Cuadrilateros(grueso,grueso,0,0,200,200)
Borde_Superior = Cuadrilateros(grueso,ancho_bordes,0,0,10,10)
Borde_Inferior = Cuadrilateros(grueso,ancho_bordes,0,0,10,650)
Paleta_Player1 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP1,300)
Paleta_Player2 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP2,300)
Paleta1Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP1,250)
Paleta2Dual_player1 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP1,350)
Paleta1Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP2,250)
Paleta2Dual_player2 = Cuadrilateros(largo_paletas,ancho_paletas,0,0,X_paletaP2,350)


pantalla = pygame.display.set_mode((ancho_display, largo_display))
pygame.display.set_caption("PONG")
pygame.display.update()




def gameLoop():
    global salir_juego
    pantalla.fill(negro)
    pygame.display.update()

    y_paleta2 = Paleta_Player1.getPosY()
    y_paleta1 = Paleta_Player1.getPosY()
    move1 = Paleta_Player1.getMovY()
    move2 = Paleta_Player2.getMovY()
    borde_superior = Borde_Superior.getPosY()
    borde_inferior = Borde_Inferior.getPosY()

    while not salir_juego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir_juego = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    move2 = 2
                if event.key == pygame.K_s:
                    move1 = 2
                if event.key == pygame.K_UP:
                    move2 = -2
                if event.key == pygame.K_w:
                    move1 = -2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    move2 = 0
                if event.key == pygame.K_UP:
                    move2 = 0
                if event.key == pygame.K_s:
                    move1 = 0
                if event.key == pygame.K_w:
                    move1 = 0


        pygame.draw.rect(pantalla, blanco,[X_paletaP1, y_paleta1, largo_paletas,ancho_paletas]) #Paleta jugador 1
        pygame.draw.rect(pantalla, blanco, [X_paletaP2, y_paleta2, largo_paletas, ancho_paletas]) #Paleta jugador 2
        pygame.draw.rect(pantalla, blanco, [ancho_display//2, largo_display//2, grueso, grueso]) #Bola
        pygame.draw.rect(pantalla, blanco, [50, 20, ancho_bordes, grueso]) #Borde superior
        pygame.draw.rect(pantalla, blanco, [50, 710, ancho_bordes, grueso])  #Borde inferior

        pygame.display.update()
        reloj.tick(FPS)
        pantalla.fill(negro)

        if y_paleta1 + largo_paletas > largo_display:
            move1 = 0
        if y_paleta2 + largo_paletas == borde_inferior:
            move2 = 0


        print(y_paleta1 + largo_paletas)



        y_paleta1 += move1
        y_paleta2 += move2

    pygame.quit()

gameLoop()