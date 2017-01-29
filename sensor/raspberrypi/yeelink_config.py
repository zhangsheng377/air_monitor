apikey = "779bfd896876dc377d3ed78d0fa1dbf4"


class MYCONFIG():
    device_id = ''
    sensor_pm25_id = ''
    sensor_CO_id = ''
    sensor_SO2_id = ''


myconfig = MYCONFIG()


def init(myid):
    if myid == 0:
        myconfig.device_id = '353097'
        myconfig.sensor_pm25_id = '397985'
        myconfig.sensor_CO_id = '398391'
        myconfig.sensor_SO2_id = '400110'
    elif myid == 1:
        myconfig.device_id = '354298'
        myconfig.sensor_pm25_id = '400108'
        myconfig.sensor_CO_id = '400109'
        myconfig.sensor_SO2_id = '400111'


def device_id():
    result = myconfig.device_id
    print "device_id : ", result
    return result


def sensor_pm25_id():
    result = myconfig.sensor_pm25_id
    print "sensor_pm25_id : ", result
    return result


def sensor_CO_id():
    result = myconfig.sensor_CO_id
    print "sensor_CO_id : ", result
    return result


def sensor_SO2_id():
    result = myconfig.sensor_SO2_id
    print "sensor_SO2_id : ", result
    return result
