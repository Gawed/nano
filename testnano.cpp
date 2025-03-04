#include <Wire.h>

#define I2C_ADDRESS 0x08  // Arduino 的 I2C 地址
#define BUZZER_PIN 10

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
  Wire.begin(I2C_ADDRESS);  // 设定 Arduino 作为 I²C 从设备
  Wire.onReceive(receiveEvent);
}

void loop() {
  
}


void receiveEvent(int numBytes) {
  while (Wire.available()) {
    char c = Wire.read();
    if (c == 'O') {
      digitalWrite(BUZZER_PIN, HIGH);
      delay(1000);
      digitalWrite(BUZZER_PIN, LOW);
    }
  }
}
