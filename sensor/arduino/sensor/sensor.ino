#include <SoftwareSerial.h>

#define pm25_RX 10
#define pm25_TX 11
#define CO A0
#define SO2 A1
#define O3 A2

SoftwareSerial mySerial_pm(pm25_RX, pm25_TX);
float A = 1000.0;

float value_pm25 = 0.0;
float value_CO = 0.0;
float value_SO2 = 0.0;
float value_O3 = 0.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  mySerial_pm.begin(2400);
  pinMode(CO, INPUT);
  pinMode(SO2, INPUT);
  pinMode(O3, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println("start");
  int temp;
  temp = read_pm(pm25_RX, pm25_TX);
  if (temp > 0) {
    value_pm25 = temp;
  }
  Serial.print("PM2.5:"); Serial.println(value_pm25);

  value_CO = map(analogRead(CO), 0, 1023, 0, 1000);
  Serial.print("CO:"); Serial.println(value_CO);

  value_SO2 = map(analogRead(SO2), 0, 1023, 0, 500);
  Serial.print("SO2:"); Serial.println(value_SO2);

  value_O3 = map(analogRead(O3), 0, 1023, 0, 1000);
  Serial.print("O3:"); Serial.println(value_O3);

 //Serial.println("");
  //delay(500);
}

float read_pm(int RX, int TX) {
  int Vout_H, Vout_L, Vret_H, Vret_L, check, temp;
  float Vout, Ud = 0.0;


  int count = 0;
  int need_read = mySerial_pm.available();
  //Serial.print("need_read : "); Serial.println(need_read);
  for (int i = 0; i < need_read; i++) {
    temp = mySerial_pm.read();
    if (temp == -1) {
      continue;
    }
    //Serial.print(temp);
    if (count == 0) {
      if (temp != 170) {
        continue;
      }
      count++;
    }
    else if (count == 1) {
      Vout_H = temp;
      count++;
    }
    else if (count == 2) {
      Vout_L = temp;
      count++;
    }
    else if (count == 3) {
      Vret_H = temp;
      count++;
    }
    else if (count == 4) {
      Vret_L = temp;
      count++;
    }
    else if (count == 5) {
      check = temp;
      count++;
    }
    else if (count == 6) {
      if (temp == 255) {
        if (check == (Vout_H + Vout_L + Vret_H + Vret_L) % 256) {
          Vout = (Vout_H * 256 + Vout_L) * 1.0 / 1024 * 8;
          Ud = 1.0 * A * Vout;
          if (Ud > 0) {
            break;
          }
          else {
            count = 0;
          }
        }
      }
    }
  }
  return Ud;

  /*
    SoftwareSerial mySerial_pm(RX, TX);
    mySerial_pm.begin(2400);
    //mySerial_pm.flush();
    //Serial.println("read_pm");
    while (true) {
      temp = -1;
      while (temp == -1) {
        temp = mySerial_pm.read();
        Serial.print(temp);
      }
      Serial.println(temp);
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
  */
}
