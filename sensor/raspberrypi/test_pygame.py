# coding=utf-8
import pygame
import sys
from pygame.locals import *
import dashboard
import color
import random
from time import time

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
mydashboard = []
for y in range(0, y_mydashboard):
    for x in range(0, x_mydashboard):
        position = (radius + x * (gap[0] + 2 * radius), radius + y * (gap[1] + 2 * radius))
        mydashboard.append(dashboard.DASHBOARD(screen, position, radius, x + y * x_mydashboard, color_bg, 0, 1000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit()

    time_now = time()
    if time_now - time_old > 15:
        print "tick", time_now - time_old
        time_old = time_now

    screen.fill(color_bg)

    for i in range(0, x_mydashboard * y_mydashboard):
        mydashboard[i].draw(random.uniform(0, 1000))

    pygame.display.flip()
    # pygame.time.delay(100)
    clock.tick(10)
