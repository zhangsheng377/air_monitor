#include <SoftwareSerial.h>

#define CO A0
#define NONE A1

float A = 1000.0;
#define pm25_RX 10
#define pm25_TX 11

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(CO, INPUT);
  pinMode(NONE, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println("start");
  float value_pm25 = read_pm(pm25_RX, pm25_TX);
  Serial.print("pm2.5 : "); Serial.print(value_pm25); Serial.println("ppm");

  float value_CO = map(analogRead(CO) - analogRead(NONE), 0, 1023, 0, 1000);
  Serial.print("CO : "); Serial.print(value_CO); Serial.println("ppm");

  Serial.println("");
  delay(500);
}

float read_pm(int RX, int TX) {
  SoftwareSerial mySerial_pm(RX, TX);
  mySerial_pm.begin(2400);
  int Vout_H, Vout_L, Vret_H, Vret_L, check, temp;
  float Vout, Ud = 0.0;
  mySerial_pm.flush();
  //Serial.println("read_pm");
  while (true) {
    temp = -1;
    while (temp == -1) {
      temp = mySerial_pm.read();
      //Serial.println(temp);
    }
    //Serial.println(temp);
    if (temp == 170) {
      //Serial.println(temp);
      temp = -1;
      while (temp == -1) {
        temp = mySerial_pm.read();
      }
      Vout_H = temp;

      temp = -1;
      while (temp == -1) {
        temp = mySerial_pm.read();
      }
      Vout_L = temp;

      temp = -1;
      while (temp == -1) {
        temp = mySerial_pm.read();
      }
      Vret_H = temp;

      temp = -1;
      while (temp == -1) {
        temp = mySerial_pm.read();
      }
      Vret_L = temp;

      temp = -1;
      while (temp == -1) {
        temp = mySerial_pm.read();
      }
      check = temp;

      temp = -1;
      while (temp == -1) {
        temp = mySerial_pm.read();
      }
      if (temp == 255) {
        //Serial.print(Vout_H);Serial.print(" ");Serial.print(Vout_L);Serial.print(" ");Serial.print(Vret_H);Serial.print(" ");Serial.print(Vret_L);Serial.print(" ");Serial.println(check);
        if (check == (Vout_H + Vout_L + Vret_H + Vret_L) % 256) {
          Vout = (Vout_H * 256 + Vout_L) * 1.0 / 1024 * 8;
          Ud = 1.0 * A * Vout;
          //Serial.println(Ud);
          if (Ud > 0) {
            //Serial.println("Ud>0");
            //Serial.print(Vout_H);Serial.print(" ");Serial.print(Vout_L);Serial.print(" ");Serial.print(Vret_H);Serial.print(" ");Serial.print(Vret_L);Serial.print(" ");Serial.println(check);
            break;
          }
        }
      }
      temp = -1;
    }
  }
  return Ud;
}
