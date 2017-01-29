import RPi.GPIO as GPIO
import serial
import smbus


class SENSOR_CONFIG():
    serial_0 = serial.Serial("/dev/ttyS0", 2400)
    A = 1200

    address = 0x48
    A0 = 0x40
    A1 = 0x41
    A2 = 0x42
    A3 = 0x43

    bus = smbus.SMBus(1)

    GPIO.setmode(GPIO.BOARD)


sensor_config = SENSOR_CONFIG()


def read_pm25():
    result = -1
    Vout_H = 0
    Vout_L = 0
    Vret_H = 0
    Vret_L = 0
    check = 0
    waitlen = sensor_config.serial_0.inWaiting()
    # print "waitlen : sensor_api", waitlen
    if waitlen != 0:
        recv = sensor_config.serial_0.read(waitlen)
        listhex = [ord(i) for i in recv]
        # print listhex
        count = 0
        for i in range(len(listhex)):
            if count == 0:
                if listhex[i] == 170:
                    count += 1
                    Vout_H = 0
                    Vout_L = 0
                    Vret_H = 0
                    Vret_L = 0
                    check = 0
            else:
                count += 1
                if count == 2:
                    Vout_H = listhex[i]
                elif count == 3:
                    Vout_L = listhex[i]
                elif count == 4:
                    Vret_H = listhex[i]
                elif count == 5:
                    Vret_L = listhex[i]
                elif count == 6:
                    check = listhex[i]
                elif count == 7:
                    count = 0
                    if listhex[i] == 255:
                        if check == (Vout_H + Vout_L + Vret_H + Vret_L) % 256:
                            Vout = (Vout_H * 256 + Vout_L) * 1.0 / 1024 * 5
                            Ud = 1.0 * sensor_config.A * Vout
                            if Ud > 0:
                                result = Ud
                                break
    return result


def read_CO():
    sensor_config.bus.write_byte(sensor_config.address, sensor_config.A0)
    value_CO = sensor_config.bus.read_byte(sensor_config.address) * 1.0 / 256 * 1000
    if value_CO > 0:
        return value_CO
    else:
        return -1


def read_SO2():
    sensor_config.bus.write_byte(sensor_config.address, sensor_config.A1)
    value_SO2 = sensor_config.bus.read_byte(sensor_config.address) * 1.0 / 256 * 500
    if value_SO2 > 0:
        return value_SO2
    else:
        return -1


def read_O3():
    sensor_config.bus.write_byte(sensor_config.address, sensor_config.A2)
    value_O3 = sensor_config.bus.read_byte(sensor_config.address) * 1.0 / 256 * 1000
    if value_O3 > 0:
        return value_O3
    else:
        return -1
