import pycurl
import json


# import StringIO

def send_value(apikey, device_id, sensor_id, value):
    # print device_id, sensor_id, value
    mycurl = pycurl.Curl()
    mycurl.setopt(mycurl.URL,
                  'http://api.yeelink.net/v1.0/device/' + device_id + '/sensor/' + sensor_id + '/datapoints')
    mycurl.setopt(mycurl.HTTPHEADER, ["U-ApiKey:" + apikey])
    mycurl.setopt(mycurl.POSTFIELDS, json.dumps({"value": value}))
    try:
        mycurl.perform()
    except Exception, e:
        # print Exception, ":", e
        print ""
    mycurl.close()
