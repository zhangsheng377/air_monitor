import pycurl
import json
import StringIO

apikey = ''


def init(apikey):
    apikey = apikey


def send_value(device_id, sensor_id, value):
    mycurl = pycurl.Curl()
    mycurl.setopt(mycurl.URL,
                  'http://api.yeelink.net/v1.0/device/' + device_id + '/sensor/' + sensor_id + '/datapoints')
    mycurl.setopt(mycurl.HTTPHEADER, ["U-ApiKey:" + apikey])
    mycurl.setopt(mycurl.POSTFIELDS, json.dumps({"value": value}))
    try:
        print 'http://api.yeelink.net/v1.0/device/' + device_id + '/sensor/' + sensor_id + '/datapoints'
        print "mycurl perform start : yeelink_api send_value"
        mycurl.perform()
        print ""
        print "mycurl perform end : yeelink_api send_value"
    except Exception, e:
        # print Exception, ":", e
        print "error : yeelink_api send_value"
    mycurl.close()
