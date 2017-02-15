# coding=utf-8
import time
import sensor_api
import yeelink_config
import yeelink_api

import pygame
import sys
from pygame.locals import *
import dashboard
import color
import random
from time import time

import pycurl

_DEBUG_ = False

MYID = 1
yeelink_config.init(MYID)
device_id = yeelink_config.device_id()
apikey = yeelink_config.apikey()

time_old = time()

pygame.init()
pygame.display.set_caption("Demo")
clock = pygame.time.Clock()

try:
    import wx

    size = wx.GetDisplaySize()
except:
    print "Can't find wxpython."
    size = pygame.display.list_modes()[len(pygame.display.list_modes()) / 2]

gap = (int(size[0] / 14), int(size[1] / 9))
radius = min(gap[0], gap[1]) * 2
size = (2 * gap[0] + 6 * radius, gap[1] + 4 * radius)

# print size

screen = pygame.display.set_mode(size, FULLSCREEN | HWSURFACE)

color_bg = color.black

x_mydashboard = 3
y_mydashboard = 2
mydashboard = {}
values = {}
names = ['PM2.5', 'CO', 'SO2', 'O3', '甲醛'.decode('gbk', 'ignore').encode('utf-8'),
         '易燃气体'.decode('gbk', 'ignore').encode('utf-8')]
values_range = {}
values_range[names[0]] = (0, 500)
values_range[names[1]] = (0, 200)
values_range[names[2]] = (0, 50)
values_range[names[3]] = (0, 50)
values_range[names[4]] = (0, 1000)
values_range[names[5]] = (0, 1000)

for y in range(0, y_mydashboard):
    for x in range(0, x_mydashboard):
        position = (radius + x * (gap[0] + 2 * radius), radius + y * (gap[1] + 2 * radius))
        # mydashboard.append(dashboard.DASHBOARD(screen, position, radius, names[x + y * x_mydashboard], color_bg, 0, 1000))
        mydashboard[names[x + y * x_mydashboard]] = dashboard.DASHBOARD(screen, position, radius,
                                                                        names[x + y * x_mydashboard], color_bg,
                                                                        values_range[names[x + y * x_mydashboard]][0],
                                                                        values_range[names[x + y * x_mydashboard]][1])
        values[names[x + y * x_mydashboard]] = 0.0

values['甲醛'.decode('gbk', 'ignore').encode('utf-8')] = 0.06
values['易燃气体'.decode('gbk', 'ignore').encode('utf-8')] = 1.35

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit()

    value_CO = sensor_api.read_CO()
    if value_CO > 0:
        # print "CO :", value_CO
        values['CO'] = value_CO

    value_SO2 = sensor_api.read_SO2()
    if value_SO2 > 0:
        # print "SO2 :", value_SO2
        values['SO2'] = value_SO2

    value_O3 = sensor_api.read_O3()
    if value_O3 > 0:
        # print "O3 :", value_O3
        values['O3'] = value_O3
    value_O3 = 0

    time_now = time()
    if time_now - time_old > 15:
        # print "tick", time_now - time_old
        time_old = time_now

        value_pm25 = sensor_api.read_pm25()
        if value_pm25 > 0:
            # print "pm2.5 :", value_pm25
            values['PM2.5'] = value_pm25

        if not _DEBUG_:
            print "send value", values['CO'], values['SO2']
            yeelink_api.send_value(apikey, device_id, yeelink_config.sensor_pm25_id(), values['PM2.5'])
            yeelink_api.send_value(apikey, device_id, yeelink_config.sensor_CO_id(), values['CO'])
            yeelink_api.send_value(apikey, device_id, yeelink_config.sensor_SO2_id(), values['SO2'])
            # yeelink_api.send_value(apikey, device_id, yeelink_config.sensor_O3_id(), values['O3'])

            mycurl = pycurl.Curl()
            mycurl.setopt(mycurl.URL, 'http://www.zhangshengdong.com/weixin/warningtemplate.php')
            try:
                mycurl.perform()
            except Exception, e:
                print Exception, ":", e
            mycurl.close()

            # print ""

    screen.fill(color_bg)

    for y in range(0, y_mydashboard):
        for x in range(0, x_mydashboard):
            mydashboard[names[x + y * x_mydashboard]].draw(values[names[x + y * x_mydashboard]])

    pygame.display.flip()
    clock.tick(10)
