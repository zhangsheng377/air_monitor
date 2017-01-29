apikey = "779bfd896876dc377d3ed78d0fa1dbf4"


def init(myid):
    if myid == 0:
        self.device_id = '353097'
        self.sensor_pm25_id = '397985'
        self.sensor_CO_id = '398391'
        self.sensor_SO2_id = '400110'
    elif myid == 1:
        self.device_id = '354298'
        self.sensor_pm25_id = '400108'
        self.sensor_CO_id = '400109'
        self.sensor_SO2_id = '400111'


def device_id():
    return self.device_id


def sensor_pm25_id():
    return self.sensor_pm25_id


def sensor_CO_id():
    return self.sensor_CO_id


def sensor_SO2_id():
    return self.sensor_SO2_id
