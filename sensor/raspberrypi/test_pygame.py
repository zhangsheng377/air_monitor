# coding=utf-8
import pygame
import sys
from pygame.locals import *

pygame.init()

size=pygame.display.list_modes()[0]
size_window=pygame.display.list_modes()[0][0]/4,pygame.display.list_modes()[0][1]/4

screen = pygame.display.set_mode(size_window)
# 貌似必须要先窗口再全屏，之后才能正确切换成窗口
screen = pygame.display.set_mode(pygame.display.list_modes()[0], FULLSCREEN | HWSURFACE)
fullscreen = True

bg = (255, 255, 255)

pygame.display.set_caption("Demo")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(pygame.display.list_modes()[0], FULLSCREEN | HWSURFACE)
                    size=pygame.display.list_modes()[0]
                else:
                    screen = pygame.display.set_mode(size_window)
                    size=size_window

    screen.fill(bg)
    radius=min(size[0]/14,size[1]/6)
    line_width=radius/45
    pygame.draw.circle(screen,(120,120,120),(size[0]/2,size[1]/2),radius,line_width)
    pygame.display.flip()
    pygame.time.delay(10)
