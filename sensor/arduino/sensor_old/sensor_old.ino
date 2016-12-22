#include <SoftwareSerial.h>

#define LED 12
#define CO A0

int Vout_H, Vout_L, Vret_H, Vret_L, check, temp;
float Vout, Ud;

int A = 1000;

SoftwareSerial mySerial(10, 11);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  mySerial.begin(2400);
  pinMode(LED, OUTPUT);
  pinMode(CO, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  temp = -1;
  while (temp == -1) {
    temp = mySerial.read();
  }
  if (temp == 170) {
    temp = -1;
    while (temp == -1) {
      temp = mySerial.read();
    }
    Vout_H = temp;

    temp = -1;
    while (temp == -1) {
      temp = mySerial.read();
    }
    Vout_L = temp;

    temp = -1;
    while (temp == -1) {
      temp = mySerial.read();
    }
    Vret_H = temp;

    temp = -1;
    while (temp == -1) {
      temp = mySerial.read();
    }
    Vret_L = temp;

    temp = -1;
    while (temp == -1) {
      temp = mySerial.read();
    }
    check = temp;

    temp = -1;
    while (temp == -1) {
      temp = mySerial.read();
    }
    if (temp == 255) {
      if (check == (Vout_H + Vout_L + Vret_H + Vret_L) % 256) {
        Vout = (Vout_H * 256 + Vout_L) * 1.0 / 1024 * 8;
        Ud = 1.0 * A * Vout;
        if (Ud > 0) {
          Serial.print("pm2.5 : ");
          Serial.print(Ud); Serial.println("ppm");

          Serial.print("CO : ");
          Serial.print(map(analogRead(CO), 0, 255, 10, 1000));
          Serial.println("ppm");

          Serial.println("");
          delay(500);
        }
      }
    }
    temp = -1;
  }
}
