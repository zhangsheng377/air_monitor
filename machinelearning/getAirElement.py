import pycurl
import json
import sqlite3
from io import BytesIO

buffer = BytesIO()

mycurl = pycurl.Curl()
mycurl.setopt(pycurl.URL, 'http://www.pm25.in/api/querys/all_cities.json')
mycurl.setopt(pycurl.WRITEDATA, buffer)
try:
    mycurl.perform()
except Exception as e:
    print(Exception, ":", e)
    print("")
mycurl.close()

print("mycurl.perform() over")

body = buffer.getvalue()
with open("data.dat", "w") as f:
    print(body, file=f)

print(body)
