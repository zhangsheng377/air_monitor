# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import smbus

_DEBUG_ = False


class SENSOR_CONFIG():
    serial_0 = serial.Serial("/dev/ttyUSB0", 9600)
    value_pm = -1
    value_CO = -1
    value_SO2 = -1
    value_O3 = -1
    value_HCHO = -1
    value_MQ2 = -1


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
                    continue
                if value > 0:
                    if name == "PM2.5":
                        sensor_config.value_pm = value
                    elif name == "CO":
                        sensor_config.value_CO = value
                    elif name == "SO2":
                        sensor_config.value_SO2 = value
                    elif name == "O3":
                        if value < 500:
                            sensor_config.value_O3 = value
                    elif name == "HCHO":
                        sensor_config.value_HCHO = value
                    elif name == "MQ2":
                        sensor_config.value_MQ2 = value
    if sensor_name == "PM2.5":
        return sensor_config.value_pm
    elif sensor_name == "CO":
        return sensor_config.value_CO
    elif sensor_name == "SO2":
        return sensor_config.value_SO2
    elif sensor_name == "O3":
        return sensor_config.value_O3
    elif sensor_name == "HCHO":
        return sensor_config.value_HCHO
    else:
        return sensor_config.value_MQ2
