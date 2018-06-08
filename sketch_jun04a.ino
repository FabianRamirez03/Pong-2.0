// Puertos analogos
int arriba_1 = 3; //Movimiento arriba del jugador 
int abajo_1 = 2; //Movimiento abajo del jugador 1
int arriba_2 = 4; // Movimiento arriba del jugador 2
int abajo_2 = 5; //Movimiento abajo del jugador 2
int volumen = 6; //Boton que retorna a la pantalla de inicio
int inspector = 7; //Abre la ventana inspector para revisar el estado de la matriz

//Variables del display
//int a = 2;  //For displaying segment "a"
//int b = 3;  //For displaying segment "b"
//int c = 4;  //For displaying segment "c"
//int d = 5;  //For displaying segment "d"
//int e = 6;  //For displaying segment "e"
//int f = 8;  //For displaying segment "f"
//int g = 9;  //For displaying segment "g"
//int digito = 2;

//Puertos digitales
int fondo = 8; //Cambia el color del fondo 

void setup() {
  //inicializa la comunicacion serial
  Serial.begin(9600); //9600 es la "velocidad", el mismo valor debe ser seleccionado en el monitor serial
  pinMode(arriba_1, INPUT);//declaramos el pin como una entrada digital (HIGH o LOW, 0 o 5V), con resistencia Pullup
  pinMode(abajo_1, INPUT_PULLUP);
  pinMode(arriba_2,INPUT_PULLUP);
  pinMode(abajo_2, INPUT_PULLUP); 
  pinMode(volumen, INPUT_PULLUP);
  pinMode(inspector, INPUT_PULLUP);
  pinMode(fondo, INPUT_PULLUP);  
  //pines del display
  //pinMode(a, OUTPUT);  //A
  //pinMode(b, OUTPUT);  //B
  //pinMode(c, OUTPUT);  //C
  //pinMode(d, OUTPUT);  //D
  //pinMode(e, OUTPUT);  //E
  //pinMode(f, OUTPUT);  //F
  //pinMode(g, OUTPUT);  //G

}
/*
void displayDigit(int digit)
{
  Serial.println(digit);
 //Conditions for displaying segment a
 if(digit!=1 && digit != 4){
 digitalWrite(a,HIGH);}
 
 //Conditions for displaying segment b
 if(digit != 5 && digit != 6){
 digitalWrite(b,HIGH);}
 
 //Conditions for displaying segment c
 if(digit !=2){
 digitalWrite(c,HIGH);}
 
 //Conditions for displaying segment d
 if(digit != 1 && digit !=4 && digit !=7){
 digitalWrite(d,HIGH);}
 
 //Conditions for displaying segment e 
 if(digit == 2 || digit ==6 || digit == 8 || digit==0){
 digitalWrite(e,HIGH);}
 
 //Conditions for displaying segment f
 if(digit != 1 && digit !=2 && digit!=3 && digit !=7){
 digitalWrite(f,HIGH);}
 if (digit!=0 && digit!=1 && digit !=7){
 digitalWrite(g,HIGH);}
 
}

void turnOff()
{
  digitalWrite(a,LOW);
  digitalWrite(b,LOW);
  digitalWrite(c,LOW);
  digitalWrite(d,LOW);
  digitalWrite(e,LOW);
  digitalWrite(f,LOW);
  digitalWrite(g,LOW);
}

*/
void loop() {
  int estado_Abajo1 = digitalRead(abajo_1); //lee el estado del pin (0 o 1, 0 o 5v)
  int estado_Arriba1 = digitalRead(arriba_1);
  int estado_Abajo2 = digitalRead(abajo_2);
  int estado_Arriba2 = digitalRead(arriba_2);
  int estado_volumen = digitalRead(volumen);
  int estado_inspector = digitalRead(inspector);
  int estado_fondo = digitalRead(fondo);
/*  
  if (Serial.available ()) {
  int score = Serial.read ();
  switch (score) {
    case 48: // do something
    displayDigit(0);
    break;
    case 49: // do something else
    displayDigit(1);
    break;
    case 50: // do something
    displayDigit(2);
    break;
    case 51: // do something else
    displayDigit(3);
    break;
    case 52: // do something
    displayDigit(4);
    break;
    case 53: // do something else
    displayDigit(5);
    break;
    case 54: // do something else
    displayDigit(6);
    break;
    case 55: // do something else
    displayDigit(7);
    break;
    case 56: // do something else
    displayDigit(8);
    break;
    case 57: // do something else
    displayDigit(9);
    break;
    default: // do something completely else
    displayDigit(4);
  }
}
*/
  if (estado_Abajo1 == 0){
    Serial.println("paleta 1.1#");//Movimiento para la primera paleta, abajo
  }
  else if (estado_Arriba1 == 0){
    Serial.println("paleta 1.2#");//Movimiento para la primera paleta, arriba
  }
  else if (estado_Abajo2 == 0){
    Serial.println("paleta 2.1#");//Movimiento para la segunda paleta, abajo
  }
  c//Movimiento para la segunda paleta, arriba
  }
  else if (estado_Arriba1 == 0){
    Serial.println("paleta 1.2#");//Movimiento para la segunda paleta
  }
  else if (estado_volumen == 0){
    Serial.println("volumen#");//Movimiento para la segunda paleta
  }
  else if (estado_inspector == 0){
    Serial.println("inspector#");//Movimiento para la segunda paleta
  }
  else if (estado_fondo == 0){
    Serial.println("fondo#");//Movimiento para la segunda paleta
  }
  else
  {
    Serial.println("corriendo#");
  }


  
  delay(130);        // espera para la siguiente lectura

  

}
