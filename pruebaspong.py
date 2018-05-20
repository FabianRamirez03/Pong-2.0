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
verde_oscuro = (0,144,0)
reloj = pygame.time.Clock()
FPS = 10 #define la velocidad del juego
borde_inferior1 = 16
borde1_1 = 10
borde2_1 = 10                       #posiciones en la matriz
borde_inferior2 = 991
borde_inferior2_2 = 990
borde_inferior1_2 = 13
seccion = 60
reacciona = 400
colores = [(0,0,0), "nada",(0,255,0)]
setclor = 1
tipografia_menor = pygame.font.Font("Comfortaa-Bold.ttf", 30)

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

'''La funcion boton se encarga de definir las variables que distinguen a cada modo de juego.
Esta funcion trabaja en el menu de inicio, de manera interna y el usuario escoge las opciones
del modo de juego. Al final llama al ciclo para correr el juego.'''
def boton(pos_x, pos_y, ancho, alto, opcion):

    P1_P2 = Game.getjugadores()
    modo_juego = Game.getmodo()
    dificultad = Game.getDificultad()
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



    if dificultad == 1:
        pygame.draw.rect(pantalla, negro, [tablero[538][0], tablero[538][1], 30, 30])
        pygame.draw.rect(pantalla, verde, [tablero[688][0], tablero[688][1], 30, 30])
        pygame.draw.rect(pantalla, verde, [tablero[863][0], tablero[863][1], 30, 30])
    if dificultad == 2:
        pygame.draw.rect(pantalla, verde, [tablero[538][0], tablero[538][1], 30, 30])
        pygame.draw.rect(pantalla, negro, [tablero[688][0], tablero[688][1], 30, 30])
        pygame.draw.rect(pantalla, verde, [tablero[863][0], tablero[863][1], 30, 30])
    if dificultad == 3:
        pygame.draw.rect(pantalla, verde, [tablero[538][0], tablero[538][1], 30, 30])
        pygame.draw.rect(pantalla, verde, [tablero[688][0], tablero[688][1], 30, 30])
        pygame.draw.rect(pantalla, negro, [tablero[863][0], tablero[863][1], 30, 30])
    if P1_P2 == True:
        pygame.draw.rect(pantalla, negro, [tablero[632][0], tablero[632][1], 30, 30])
        pygame.draw.rect(pantalla, verde, [tablero[932][0], tablero[932][1], 30, 30])
    if P1_P2 == False:
        pygame.draw.rect(pantalla, verde, [tablero[632][0], tablero[632][1], 30, 30])
        pygame.draw.rect(pantalla, negro, [tablero[932][0], tablero[932][1], 30, 30])
    if modo_juego == False:
        pygame.draw.rect(pantalla, verde, [tablero[535][0], tablero[535][1], 30, 30])
        pygame.draw.rect(pantalla, negro, [tablero[685][0], tablero[685][1], 30, 30])
    if modo_juego == True:
        pygame.draw.rect(pantalla, negro, [tablero[535][0], tablero[535][1], 30, 30])
        pygame.draw.rect(pantalla, verde, [tablero[685][0], tablero[685][1], 30, 30])

''' boton_texto crea botonoes con una funcion y un texto escrito'''    
def boton_texto(mensaje,pos_x,pos_y,ancho,alto,color_activo, color_inactivo, opcion):
    global tipografia_menor
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos_x + ancho > mouse[0] > pos_x and pos_y + alto > mouse[1] > pos_y:
        pygame.draw.rect(pantalla, color_activo, [pos_x,pos_y, ancho, alto])

        if click[0] == 1 and opcion == "Inicio":
            Menu()  
        if click[0] == 1 and opcion == "Ganador":
            GameLoop()
        if click[0] == 1 and opcion == "Aceptar":
            Game.aceptar()       
        if click[0] == 1 and opcion == "Again":
            GameLoop()  
        if click[0] == 1 and opcion == "Cerrar":
            pygame.quit()
            quit()     
    
    else:
        pygame.draw.rect(pantalla, color_inactivo, [pos_x,pos_y, ancho, alto])

    inicio_txt = tipografia_menor.render(mensaje, True, blanco)
    inicio_rect = inicio_txt.get_rect()
    inicio_rect.center = (pos_x + ancho/2, pos_y + alto/2)
    pantalla.blit(inicio_txt, inicio_rect)


tablero = matriz([],[],40,40) #define la matriz del tablero

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

    def aceptar(self): #Esta funcion esta ligada al boton aceptar y llama el ciclo del juego con las variables definidas por el usuario
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

Game = Juego(0,0,tablero,1,True, False) #Instancia de la clase Juego, define los argumentos de Pong.

def Menu(): #Este es el ciclo de inicio para que el usuario defina las variables.
    pantalla.blit(pygame.image.load('Fondo.png'), [0, 0])
    global tipografia_menor
    menu = True
    dificultad = Game.getDificultad()
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      

        #pantalla.fill(blanco)

        tipografia = pygame.font.Font("Comfortaa-Bold.ttf", 60) #tipografias para texto titulo

        titulo = tipografia.render("PONG", True, blanco) #bloques de definicion de texto
        titulo_rect = titulo.get_rect()
        titulo_rect.center = (tablero[453][0],tablero[453][1])
        pantalla.blit(titulo, titulo_rect)


        modo_txt = tipografia_menor.render("Modo de juego:" + " "*13 + "P1 vs P2" + " "*13 + "P1 vs PC", True, blanco)
        modo_rect = modo_txt.get_rect()
        modo_rect.center = (tablero[458][0], tablero[458][1])
        pantalla.blit(modo_txt, modo_rect)

        paletas_txt = tipografia_menor.render("Paletas:" + " "*26 + "1" + " "*13 + "2", True, blanco)
        paletas_rect = paletas_txt.get_rect()
        paletas_rect.center = (tablero[336][0], tablero[336][1])
        pantalla.blit(paletas_txt, paletas_rect)

        dificultad_txt = tipografia_menor.render("Dificultad:" + " "*23 + "1" + " "*13 + "2" + " "*13 + "3", True, blanco)
        dificultad_rect = dificultad_txt.get_rect()
        dificultad_rect.center = (tablero[414][0], tablero[414][1])
        pantalla.blit(dificultad_txt, dificultad_rect)
 
        boton_texto("ACEPTAR",tablero[394][0],tablero[394][1],200,40,verde, verde_oscuro, "Aceptar")

        intro_txt = tipografia_menor.render("SELECCIONE MODOS DE JUEGO Y DE CLICK EN ACEPTAR", True, blanco)
        intro_rect = dificultad_txt.get_rect()
        intro_rect.center = (tablero[375][0],tablero[375][1])
        pantalla.blit(intro_txt, intro_rect)

        '''Botones del menu inicio para definir las variables del juego'''
        boton(tablero[632][0],tablero[632][1], 30, 30, "P1 vs P2")
        boton(tablero[932][0],tablero[932][1], 30, 30, "P1 vs PC")
        boton(tablero[535][0],tablero[535][1], 30, 30, "Sencillo")
        boton(tablero[685][0],tablero[685][1], 30, 30, "Doble")
        boton(tablero[538][0],tablero[538][1], 30, 30, "1")
        boton(tablero[688][0],tablero[688][1], 30, 30, "2")
        boton(tablero[863][0],tablero[863][1], 30, 30, "3")

        pygame.display.update()
        reloj.tick(FPS)

def playAgain(ganador):
    otra_vez = True
    while otra_vez:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pantalla.fill(negro)
        volver_font = pygame.font.Font("Comfortaa-Bold.ttf", 75)

        titulo = volver_font.render(ganador, True, blanco, negro)  # bloques de definicion de texto
        titulo_rect = titulo.get_rect()
        titulo_rect.center = (tablero[505][0], tablero[505][1])
        pantalla.blit(titulo, titulo_rect)
        boton_texto("VOLVER AL JUEGO",300,240,300,50, verde, verde_oscuro, "Again")
        boton_texto("INICIO",300,300,300,50, verde, verde_oscuro, "Inicio")
        boton_texto("CERRAR",300,360,300,50, verde, verde_oscuro, "Cerrar")



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
    global reacciona
    jugador = Game.getjugadores()
    modo = Game.getmodo() #Si modo es true, habra dos paletas, en False sera dual
    moveX_bola = 25
    moveY_bola = 1
    move_p1 = 0
    move_p2 = 0
    punto = False
    distancia_paletas = 0
    sound_paletas =  pygame.mixer.Sound('sonido_paletas.wav')
    sound_bordes = pygame.mixer.Sound('sonido_bordes.wav')


    while not salir_juego:  #si no se cumple salir juego, sale y cierra la ventana
        while not salir_juego and modo == True and jugador == True: #modo con solo una paleta y persona vs persona

            pygame.display.update()

            if dificultad == 1:   #define las velocidades y los tamaños de las paletas segùn la dificultad
                FPS = 10
                largo_paletas = 180
                borde_inferior1 = 15
                borde_inferior2 = 990
                seccion = 60
            if dificultad == 2:
                FPS = 15
                largo_paletas = 120  #En caso de aumentar los fps aumentan, haciendo que visualmente sea más rapido
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
                if score1 == 10 or score2 == 10:
                    if score1 > score2:
                        return playAgain("¡Felicidades jugador 1!")
                    else:
                        return playAgain("¡Felicidades jugador 2!")
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




                if event.type == pygame.QUIT:
                    salir_juego = True         #si el usuario sale de la ventana, se finaliza el programa



            if pos_paleta1 == 0: #rebotes de las paletas
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
                sound_bordes.play()
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
                sound_bordes.play()
            if tablero[pos_bola][0] == 40:
                score2 += 1
                pos_bola = 461
                punto = True
            if tablero[pos_bola][0] == 820:
                score1 += 1
                pos_bola = 461
                punto = True


            if  tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and tablero[pos_paleta1][1]<=tablero[pos_bola][1]<(tablero[pos_paleta1][1]+seccion):
                moveX_bola = 25
                moveY_bola = -1
                sound_paletas.play()
            if tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and (tablero[pos_paleta1][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paleta1][1]+seccion*2):
                moveX_bola = 25
                moveY_bola = 0
                sound_paletas.play()
            if tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and (tablero[pos_paleta1][1]+seccion*2) <= tablero[pos_bola][1]<=(tablero[pos_paleta1][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = 25
                sound_paletas.play()
            if  tablero[pos_bola+25][0] == tablero[pos_paleta2][0] and tablero[pos_paleta2][1]<=tablero[pos_bola][1] < (tablero[pos_paleta2][1]+seccion):
                moveX_bola = -25
                moveY_bola = -1
                sound_paletas.play()
            if tablero[pos_bola+25][0] == tablero[pos_paleta2 ][0] and (tablero[pos_paleta2][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paleta2][1]+seccion*2):
                moveX_bola = -25
                moveY_bola = 0
                sound_paletas.play()
            if tablero[pos_bola+25][0] == tablero[pos_paleta2][0] and (tablero[pos_paleta2][1]+seccion*2) <= tablero[pos_bola][1]<=(tablero[pos_paleta2][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = -25
                sound_paletas.play()

                
                



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

            boton_texto("INICIO",740,2,100,35,verde, verde_oscuro, "Inicio")




            pygame.display.update()
            reloj.tick(FPS)

#_____________________________________________________________________________________________________________________________________________________________________________________

        while not salir_juego and modo == False and jugador == True: #modo dual, PvP
            pygame.display.update()

            if punto == True:
                if score1 == 10 or score2 == 10:
                    if score1 > score2:
                        return playAgain("¡Felicidades jugador 1!")
                    else:
                        return playAgain("¡Felicidades jugador 2!")
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
            if pos_paletaDual2_1 == 975:
                pos_paletaDual2_1 = 976
                pos_paletaDual2_2 = 986
                move_p1 = 0
            if pos_paletaDual2_2 == borde_inferior2:
                pos_paletaDual2_2 = borde_inferior2 -1
                pos_paletaDual2_1 = pos_paletaDual2_2 - distancia_paletas
                move_p1 = 0



            if tablero[pos_bola][1] == 60:
                moveY_bola = 1
                sound_bordes.play()
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
                sound_bordes.play()
            if tablero[pos_bola][0] == 40:
                print("Punto 1")
                pos_bola = 461
                punto = True
                score2 += 1

            if tablero[pos_bola][0] == 820:
                print("Punto 2")
                pos_bola = 461
                punto = True
                score1 += 1
                #moveX_bola =  random.choice([1,-1])
                #moveY_bola = random.choice([25,-25])

            if  tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and tablero[pos_paletaDual1_1][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual1_1][1]+seccion):
                moveX_bola = 25
                moveY_bola = -1
                sound_paletas.play()
            if  tablero[pos_bola][0] == tablero[pos_paletaDual1_2+25][0] and tablero[pos_paletaDual1_2][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual1_2][1]+seccion):
                moveX_bola = 25
                moveY_bola = -1
                sound_paletas.play()


            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and (tablero[pos_paletaDual1_1][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual1_1][1]+seccion*2):
                moveX_bola = 25
                moveY_bola = 0
                sound_paletas.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2+25][0] and (tablero[pos_paletaDual1_2][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual1_2][1]+seccion*2):
                moveX_bola = 25
                moveY_bola = 0
                sound_paletas.play()


            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and (tablero[pos_paletaDual1_1][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual1_1][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = 25
                sound_paletas.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2+25][0] and (tablero[pos_paletaDual1_2][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual1_2][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = 25
                sound_paletas.play()




            if  tablero[pos_bola+25][0] == tablero[pos_paletaDual2_1][0] and tablero[pos_paletaDual2_1][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual2_1][1]+seccion):
                moveX_bola = -25
                moveY_bola = -1
                sound_paletas.play()
            if  tablero[pos_bola+25][0] == tablero[pos_paletaDual2_2][0] and tablero[pos_paletaDual2_2][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual2_2][1]+seccion):
                moveX_bola = -25
                moveY_bola = -1
                sound_paletas.play()


            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_1][0] and (tablero[pos_paletaDual2_1][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual2_1][1]+seccion*2):
                moveX_bola = -25
                moveY_bola = 0
                sound_paletas.play()
            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_2][0] and (tablero[pos_paletaDual2_2][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual2_2][1]+seccion*2):
                moveX_bola = -25
                moveY_bola = 0
                sound_paletas.play()


            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_1][0] and (tablero[pos_paletaDual2_1][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual2_1][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = -25
                sound_paletas.play()
            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_2][0] and (tablero[pos_paletaDual2_2][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual2_2][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = -25
                sound_paletas.play()






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

            boton_texto("INICIO",740,2,100,35,verde, verde_oscuro, "Inicio")

            pygame.display.update()
            reloj.tick(FPS)

#___________________________________________________________________________________________________________________________________________________________________________________        

        while not salir_juego and modo == True and jugador == False: #modo con solo una paleta y persona vs computador

            pygame.display.update()

            if dificultad == 1:   #define las velocidades y los tamaños de las paletas segùn la dificultad
                FPS = 10
                largo_paletas = 180
                borde_inferior1 = 15
                borde_inferior2 = 990
                seccion = 60
                reacciona =  650
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

            if punto == True: #le da una pausa al movimiento de la bola cada vez que se genera un punto
                if score1 == 10 or score2 == 10:
                    if score1 > score2:
                        return playAgain("¡Felicidades jugador 1!")
                    else:
                        return playAgain("¡Has perdido!")

                time.sleep(1)
                punto = False



            for event in pygame.event.get(): #movimiento de los jugadores.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        move_p1 = 1

                    if event.key == pygame.K_w:
                        move_p1 = -1


                if event.type == pygame.KEYUP: #debe mantenerse presionado el boton para que el movimiento se de
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0





                if event.type == pygame.QUIT:
                    salir_juego = True         #si el usuario sale de la ventana, se finaliza el programa



            if pos_paleta1 == 0: #rebotes de las paletas con los bordes
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



            if tablero[pos_bola][1] == 60: #rebotes de bola en los bordes
                moveY_bola = 1
                sound_bordes.play()
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
                sound_bordes.play()
            if tablero[pos_bola][0] == 40:
                score2 += 1
                pos_bola = 461
                punto = True
            if tablero[pos_bola][0] == 820:
                score1 += 1
                pos_bola = 461
                punto = True
                #moveX_bola =  random.choice([1,-1])
                #moveY_bola = random.choice([25,-25])
            if  tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and tablero[pos_paleta1][1]<=tablero[pos_bola][1]<(tablero[pos_paleta1][1]+seccion):
                moveX_bola = 25
                moveY_bola = -1
                sound_paletas.play()
                print("rebota1")
            if tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and (tablero[pos_paleta1][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paleta1][1]+seccion*2):
                moveX_bola = 25
                moveY_bola = 0
                sound_paletas.play()
                print("rebota2")
            if tablero[pos_bola][0] == tablero[pos_paleta1+25][0] and (tablero[pos_paleta1][1]+seccion*2) <= tablero[pos_bola][1]<=(tablero[pos_paleta1][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = 25
                sound_paletas.play()
                print("rebota3")

            if  tablero[pos_bola+25][0] == tablero[pos_paleta2][0] and tablero[pos_paleta2][1]<=tablero[pos_bola][1] < (tablero[pos_paleta2][1]+seccion):
                moveX_bola = -25
                moveY_bola = -1
                sound_paletas.play()
            if tablero[pos_bola+25][0] == tablero[pos_paleta2 ][0] and (tablero[pos_paleta2][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paleta2][1]+seccion*2):
                moveX_bola = -25
                moveY_bola = 0
                sound_paletas.play()
            if tablero[pos_bola+25][0] == tablero[pos_paleta2][0] and (tablero[pos_paleta2][1]+seccion*2) <= tablero[pos_bola][1]<=(tablero[pos_paleta2][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = -25
                sound_paletas.play()




            pos_bola += moveY_bola + moveX_bola
            pos_paleta1 += move_p1

            if moveX_bola > 0 and tablero[pos_bola][0]>reacciona:
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

            boton_texto("INICIO",740,2,100,35,verde, verde_oscuro, "Inicio")

            pygame.display.update()
            reloj.tick(FPS)
#_____________________________________________________________________________________________________________________________________________________________________________________________
        while not salir_juego and modo == False and jugador == False: #modo dual, Persona contra computador
            pygame.display.update()

            if punto == True:
                if score1 == 10 or score2 == 10:
                    if score1 > score2:
                        return playAgain("¡Felicidades jugador 1!")
                    else:
                        return playAgain("¡Has perdido!")
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

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        move_p1 = 0
                    if event.key == pygame.K_w:
                        move_p1 = 0


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
            if pos_paletaDual2_1 == 975:
                pos_paletaDual2_1 = 976
                pos_paletaDual2_2 = 986
                move_p1 = 0
            if pos_paletaDual2_2 == borde_inferior2:
                pos_paletaDual2_2 = borde_inferior2 -1
                pos_paletaDual2_1 = pos_paletaDual2_2 - distancia_paletas
                move_p1 = 0



            if tablero[pos_bola][1] == 60:
                moveY_bola = 1
                sound_bordes.play()
            if tablero[pos_bola][1] == 500:
                moveY_bola = -1
                sound_bordes.play()
            if tablero[pos_bola][0] == 40:
                print("Punto 1")
                pos_bola = 461
                punto = True
                score2 += 1

            if tablero[pos_bola][0] == 820:
                print("Punto 2")
                pos_bola = 461
                punto = True
                score1 += 1


            if  tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and tablero[pos_paletaDual1_1][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual1_1][1]+seccion):
                moveX_bola = 25
                moveY_bola = -1
                sound_paletas.play()
            if  tablero[pos_bola][0] == tablero[pos_paletaDual1_2+25][0] and tablero[pos_paletaDual1_2][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual1_2][1]+seccion):
                moveX_bola = 25
                moveY_bola = -1
                sound_paletas.play()


            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and (tablero[pos_paletaDual1_1][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual1_1][1]+seccion*2):
                moveX_bola = 25
                moveY_bola = 0
                sound_paletas.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2+25][0] and (tablero[pos_paletaDual1_2][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual1_2][1]+seccion*2):
                moveX_bola = 25
                moveY_bola = 0
                sound_paletas.play()


            if tablero[pos_bola][0] == tablero[pos_paletaDual1_1+25][0] and (tablero[pos_paletaDual1_1][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual1_1][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = 25
                sound_paletas.play()
            if tablero[pos_bola][0] == tablero[pos_paletaDual1_2+25][0] and (tablero[pos_paletaDual1_2][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual1_2][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = 25
                sound_paletas.play()




            if  tablero[pos_bola+25][0] == tablero[pos_paletaDual2_1][0] and tablero[pos_paletaDual2_1][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual2_1][1]+seccion):
                moveX_bola = -25
                moveY_bola = -1
                sound_paletas.play()
            if  tablero[pos_bola+25][0] == tablero[pos_paletaDual2_2][0] and tablero[pos_paletaDual2_2][1]<=tablero[pos_bola][1]< (tablero[pos_paletaDual2_2][1]+seccion):
                moveX_bola = -25
                moveY_bola = -1
                sound_paletas.play()


            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_1][0] and (tablero[pos_paletaDual2_1][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual2_1][1]+seccion*2):
                moveX_bola = -25
                moveY_bola = 0
                sound_paletas.play()
            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_2][0] and (tablero[pos_paletaDual2_2][1]+seccion) <= tablero[pos_bola][1]<(tablero[pos_paletaDual2_2][1]+seccion*2):
                moveX_bola = -25
                moveY_bola = 0
                sound_paletas.play()


            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_1][0] and (tablero[pos_paletaDual2_1][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual2_1][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = -25
                sound_paletas.play()
            if tablero[pos_bola+25][0] == tablero[pos_paletaDual2_2][0] and (tablero[pos_paletaDual2_2][1]+seccion*2)<=tablero[pos_bola][1]<=(tablero[pos_paletaDual2_2][1]+seccion*3):
                moveY_bola = 1
                moveX_bola = -25
                sound_paletas.play()






            pos_bola += moveY_bola + moveX_bola #Suma de indices para movimiento sobre la matriz
            pos_paletaDual1_1 += move_p1
            pos_paletaDual1_2 = pos_paletaDual1_1 + distancia_paletas



            if moveX_bola > 0 and tablero[pos_bola][0]>reacciona:
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

            boton_texto("INICIO",740,2,100,35,verde, verde_oscuro, "Inicio")

            pygame.display.update()
            reloj.tick(FPS)


        #_____________________________________________________________________________________________________________________________________________________________________________________________
    exit()






Menu()

