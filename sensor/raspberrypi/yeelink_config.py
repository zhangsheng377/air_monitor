apikey = "779bfd896876dc377d3ed78d0fa1dbf4"

device_id = ''
sensor_pm25_id = ''
sensor_CO_id = ''
sensor_SO2_id = ''


def init(myid):
    if myid == 0:
        device_id = '353097'
        sensor_pm25_id = '397985'
        sensor_CO_id = '398391'
        sensor_SO2_id = '400110'
    elif myid == 1:
        device_id = '354298'
        sensor_pm25_id = '400108'
        sensor_CO_id = '400109'
        sensor_SO2_id = '400111'


def device_id():
    result = device_id
    print "device_id : ", result
    return result


def sensor_pm25_id():
    result = sensor_pm25_id
    print "sensor_pm25_id : ", result
    return result


def sensor_CO_id():
    result = sensor_CO_id
    print "sensor_CO_id : ", result
    return result


def sensor_SO2_id():
    result = sensor_SO2_id
    print "sensor_SO2_id : ", result
    return result
