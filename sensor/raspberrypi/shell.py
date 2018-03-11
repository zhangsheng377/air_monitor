# coding=utf-8
import sensor_api
from time import time
import os
import sys

path_BEIDOU = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "beidou")
sys.path.append(path_BEIDOU)
from beidou import TXA

serial_BEIDOU = serial.Serial("/dev/ttyUSB1", 115200)
txa = TXA(user_address='0247718', serial=serial_BEIDOU, transfer_method='1')
txa.read()

_DEBUG_ = False

time_old = time()

values = {}
names = ['PM2.5', 'CO', 'SO2', 'O3', 'HCHO', 'MQ2']

while True:

    value_pm25 = sensor_api.read_value('PM2.5')
    if value_pm25 > 0:
        # print("\t\tpm2.5 :", value_pm25)
        values['PM2.5'] = value_pm25

    value_CO = sensor_api.read_value('CO')
    if value_CO > 0:
        # print("\t\tCO :", value_CO)
        values['CO'] = value_CO

    value_SO2 = sensor_api.read_value('SO2')
    if value_SO2 > 0:
        # print("\t\tSO2 :", value_SO2)
        values['SO2'] = value_SO2

    value_O3 = sensor_api.read_value('O3')
    if value_O3 > 0:
        # print("\t\tO3 :", value_O3)
        values['O3'] = value_O3

    value_HCHO = sensor_api.read_value('HCHO')
    if value_HCHO > 0:
        # print("\t\tHCHO :", value_HCHO)
        values['HCHO'] = value_HCHO

    value_MQ2 = sensor_api.read_value('MQ2')
    if value_MQ2 > 0:
        # print("\t\tMQ2 :", value_MQ2)
        values['MQ2'] = value_MQ2

    time_now = time()
    if time_now - time_old > 60:
        time_old = time_now
        content = "PM2.5:" + values['PM2.5'] + ",CO:" + values['CO'] + ",SO2:" + values['SO2'] + ",O3:" + values[
            'O3'] + ",HCHO:" + values['HCHO'] + ",MQ2:" + values['MQ2']
        message = txa.message(content=content)
        print("\t\t", message)
        txa.send(message=message)

    time.sleep(1)
