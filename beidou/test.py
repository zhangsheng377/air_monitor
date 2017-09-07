import serial
import time
import _thread


def read_serial(ser):
    while True:
        line = ser.readline()
        print(line)


ser = serial.Serial('COM3', 115200)
print(ser)
_thread.start_new_thread(read_serial, (ser,))
for i in range(5):
    # ser.write(b'$CCICA,0,00*7B\r\n')
    ser.write(b'$CCICI,0,00*83\r\n')  # 貌似校验不是83
    # line = ser.readline()
    # print(line)
    time.sleep(1)

while True:
    ser.write(b'$CCTXA,0247718,1,1,3132333435*70\r\n')
    time.sleep(80)

ser.close()
