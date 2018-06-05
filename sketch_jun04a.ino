int boton = 12; //evitar usar pines 0 y 1
int boton2 = 13;
void setup() {
  //inicializa la comunicacion serial
  Serial.begin(9600); //9600 es la "velocidad", el mismo valor debe ser seleccionado en el monitor serial
  pinMode(boton, INPUT_PULLUP);//declaramos el pin como una entrada digital (HIGH o LOW, 0 o 5V), con resistencia Pullup
  pinMode(boton2, INPUT_PULLUP);//boton 2
}

void loop() {
  int estado = digitalRead(boton); //lee el estado del pin (0 o 1, 0 o 5v)
  int estado2 = digitalRead(boton2);
  if (estado == 0){
    Serial.println("paleta 1.1%");//Movimiento para la primera paleta
  }
  else if (estado2 == 0){
    Serial.println("paleta 1.2%");//Movimiento para la segunda paleta
  }
  else
  {
    Serial.println("corra%");
  }
  
  delay(130);        // espera para la siguiente lectura
}
