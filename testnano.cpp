#include <Wire.h>

#define I2C_ADDRESS 0x08
#define BUZZER_PIN 10

volatile bool buzzerOn = false;  //  volatile pour I²C  signal
void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
  Serial.begin(9600); 
  Wire.begin(I2C_ADDRESS);
  Serial.print("I2C address est: ");
  Serial.println(I2C_ADDRESS, HEX);
  Wire.onReceive(receiveEvent);
  Serial.println("Arduino I2C Initialized");
}

void loop() {
  if (buzzerOn) {
    Serial.println("Buzzer Activated!");  
    digitalWrite(BUZZER_PIN, HIGH);
    delay(1000);
    digitalWrite(BUZZER_PIN, LOW);
    Serial.println("Buzzer Deactivated!"); 
    buzzerOn = false;
  }
}

void receiveEvent(int numBytes) {
  Serial.print("Received I2C data: ");
  while (Wire.available()) {
    char c = Wire.read();
    Serial.println(c);  
    if (c == 'O') {
      buzzerOn = true;
    }
  }
}
