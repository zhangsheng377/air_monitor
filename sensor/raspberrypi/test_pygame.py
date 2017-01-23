# coding=utf-8
import pygame
import sys
from pygame.locals import *
import dashboard
import color
import wx

pygame.init()
pygame.display.set_caption("Demo")
'''
gap = (int(50 * wx.GetDisplaySize()[0] / max(wx.GetDisplaySize()[0], wx.GetDisplaySize()[1])),
       int(50 * wx.GetDisplaySize()[1] / max(wx.GetDisplaySize()[0], wx.GetDisplaySize()[1])))
radius = max(gap[0],gap[1])*2
size = (2 * gap[0] + 6 * radius, gap[1] + 4 * radius)
'''
size = wx.GetDisplaySize()
gap = (int(size[0] / 14), int(size[1] / 9))
radius = min(gap[0], gap[1]) * 2
size = (2 * gap[0] + 6 * radius, gap[1] + 4 * radius)

print  size

screen = pygame.display.set_mode(size, FULLSCREEN | HWSURFACE)

x_mydashboard = 3
y_mydashboard = 2
mydashboard = []
for y in range(0, y_mydashboard):
    for x in range(0, x_mydashboard):
        position = (radius + x * (gap[0] + 2 * radius), radius + y * (gap[1] + 2 * radius))
        print position, radius
        mydashboard.append(dashboard.DASHBOARD(screen, size, position, radius, x + y * x_mydashboard))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit()

    screen.fill(color.black)

    for i in range(0, x_mydashboard * y_mydashboard):
        mydashboard[i].draw()

    pygame.draw.rect(screen, color.red, (0, 0, size[0], size[1]), 10)

    pygame.display.flip()
    pygame.time.delay(10)
