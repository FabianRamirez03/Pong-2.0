# Pong-2.0
Segunda version de Pong

Día 1: 4/05/18. 3h.
Montamos el proyecto en GitHub  e investigamos sobre la aplicación. Dejamos las clases definidas.

Día 2: 5/05/18. 5h.
Se programaron las clases con los respectivos argumentos, además de dar inicio con la creación de la interfaz gráfica con la libreria Pygame.

Día 3: 5/05/18 Se Crea Pong 2.0 ya que se dieron multiples problemas con los archivos. Además de que las ramas locales estaban por encima de la rama master por varios commits. También se dieron varios conflictos que no se pudieron resolver.

Día 4: 6/05/18 Se crean los archivos de pruebas para poder editar el código allí y luego implementarlo al código principal cuando estemos seguros. Luego de trabajar en estos archivos auxiliares se agregaron los cambios realizados a Pong.py. Se crea la función generadora de la matriz a la cual corresponde el tablero del juego, además de una funcion que solo se utilizará a nivel de consola para conseguir el indice correcto dentro de la matriz de mil elementos. Se optimiza la clase juego. Se arreglan errores varios que afectaban el funcionamiento del juegoo. 

Día 3 7/05/18. 6h
Montaje del menú de inicio, interfaz. Se termina la sección de variables necesarias para el correcto funcionamiento del juego. Se inicia el montaje de los ciclos de los diferentes modos de juego. Además de la colocación de todos los elementos dentro de la pantalla del juego. 

Día 4 8/05/18. 3h
Agregué los rebotes de la bola en las paletas, incluyendo las secciones donde debe rebotar según la posición de la paleta donde colisiona. Además del movimiento de la paleta del jugador 2 con sus respectivos bordes. Por último, se crea la detección de puntos por cada jugador dependiendo de la zona que traspase la pelota.

Día 5 9/05/18.
Se crea el sistema de detección de puntos, donde luego de sobrepasar los limites, la pelota aparece en el centro de la pantalla, espera un segundo y luego comienza de nuevo. Tambien se optimiza la funcionalidad y el aspecto del menú del juego. 

Dia 6 13/05/18 3h.
Se definio un segundo loop para el menu de inicio que define las variables para el modo de juego, la dificultad y los jugadores. Ademas, se trabaja la interfaz del menu. Se crea el método getModo en la clase juego para solicitar si serán una o dos paletas. Además de agregado el modo dual con sus respectivas colisiones. Tambien se agrega la tipografía que utilizarán los textos dentro del juego. Con esto se agrega el titulo y los marcadores dentro del juego. Se crea la función botón para la selección de modalidades dentro del menú. Se arreglan diversos bugs relacionados con los bordes y sus respectivas colisiones. Se adelanta la documentación interna del código.

Día 7 17/05/18
Arreglada la bitacora gracias a los commits dentro de Git.

Dia 8 19/05/18
Se arreglan errores varios. Además de crear la pantalla que emerge una vez alguno de ambos jugadores alcancen la máxima puntuación que en este caso se fijó en 10.

Dia 7 14/05/18 4h.
Se continua el menu de inicio. Los botones aun no quedan de color diferente al ser seleccionados pero ya definen las funciones y llaman a la clase de juego indicada. Se junta el codigo del menu con el oficial. Se crean las funciones para los diferentes niveles de dificultad, incluyendo las colisiones dependiendo del tamaño de la paleta y su respectiva sección. Se hacen mejoras a las colisiones, al menú y arreglos de bugs varios. Arreglado error para que la distancia entre paletas del modo dual sea proporcional al tamaño de cada paleta. 

Día 8 15/05/18.
Hechas las colisiones de las paletas con los bordes en el modo dual, además de los rebotes de la bola con sus respectivas direcciones. Arreglo de algunos errores en el menú y diversas mejoras. Además de avanzar con la documentación interna del código. Se fusiona el código del juego junto con el código del menú. 

Día 9 16/05/18.
Se agrega la verificación en caso de que el usuario quiera jugar contra la computadora o contra otro jugador. Se agregan sonidos a los rebotes, tanto para cuando la pelota pega contra una paleta como cuando sucede con uno de los bordes.  Se comenta gran parte del código. Además de notables mejoras en la función botón.

Día 10 18/05/18 3h
El menú quedó listo, los botones funcionan bien. Cada pantalla tiene su propio botón que redirige al inicio de ser necesario.

Día 11 3h 19/05/18
Se definió una pantalla de inicio de juego. Se trabajó más la interfaz y se agregaron los botonees para las pantallas de jugar de nuevo. 

Día 12 20/05/18
Se le agregó música al juego, además de añadir el archivo .mp3, se finaliza con la documentacion externa e interna. 

________________________________________________________________________________________________________________________________________
                                                    Segunda parte del proyecto
Día 1 23/05/18
Agregado modo práctica para una y dos paletas, tomando en cuenta la dificultad. Falta por arreglar bug donde después de ingresar al modo práctica individual, sale e ingresa a la pantalla practica dual, solo aparece una paleta, además se deben agregar colisiones en modo práctica dual.  
