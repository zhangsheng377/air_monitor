# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import smbus

_DEBUG_ = False


class SENSOR_CONFIG():
    serial_0 = serial.Serial("/dev/ttyUSB0", 9600)


GPIO.setmode(GPIO.BOARD)

sensor_config = SENSOR_CONFIG()


def read_value(sensor_name):
    waitlen = sensor_config.serial_0.inWaiting()
    if waitlen != 0:
        recv = sensor_config.serial_0.read(waitlen)
        recv_split = recv.split('\n')
        for message in recv_split:
            message_split = message.split(':')
            if len(message_split) > 1:
                name = message_split[0]
                value_str = message_split[1]
                try:
                    value = float(value_str)
                    # print name, "--", value
                except:
                    return -1.0
                if name == sensor_name:
                    return value
