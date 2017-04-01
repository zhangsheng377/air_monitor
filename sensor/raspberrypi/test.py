import serial
import time

serial_0 = serial.Serial("/dev/ttyUSB0", 9600)

while True:
    waitlen = serial_0.inWaiting()
    if waitlen != 0:
        recv = serial_0.read(waitlen)
        recv_split = recv.split('\n')
        for message in recv_split:
            message_split = message.split(':')
            if len(message_split) > 1:
                name = message_split[0]
                value_str = message_split[1]
                value = float(value_str)
                print name, "--", value
    time.sleep(0.1)
