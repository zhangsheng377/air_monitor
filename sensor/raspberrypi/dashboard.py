import pygame
import color
import math

if ~pygame.font.get_init():
    pygame.font.init()


class DASHBOARD(pygame.sprite.Sprite):
    def __init__(self, surface, position, radius, index):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.radius = radius
        self.line_width = int(math.ceil(self.radius / 45))
        self.gap = int(math.ceil(self.line_width / 5.0))
        self.arc_width = int(math.ceil(self.line_width * 5))
        self.position = position
        self.index = index
        self.font = pygame.font.Font(None, 36)
        self.text_index = self.font.render(str(self.index), True, color.red)
        self.rect = (self.position[0] - self.radius, self.position[1] - self.radius, self.position[0] + self.radius,
                     self.position[1] + self.radius)


    def draw(self):
        #pygame.draw.circle(self.surface, color.grey, self.position, self.radius, self.line_width)
        self.surface.blit(self.text_index, self.position)
        pygame.draw.aaline(self.surface, color.red, (self.position[0] - self.radius, self.position[1]),
                           (self.position[0] + self.radius, self.position[1]), 2)
        pygame.draw.aaline(self.surface, color.red, (self.position[0], self.position[1] - self.radius),
                           (self.position[0], self.position[1] + self.radius), 2)
        #self.draw_blendcolor_arc(color.green, color.red, 0, 180)
        if self.index==1:
            pygame.draw.rect(self.surface,color.red,self.rect,4)
            print self.rect,self.radius*2

    def draw_blendcolor_arc(self, color_start, color_end, degree_start, degree_stop):
        degree_start = int(degree_start)
        degree_stop = int(degree_stop)
        color_i = color_start
        rect = (self.rect[0] + self.line_width + self.gap, self.rect[1] + self.line_width + self.gap,
                self.rect[2] - self.line_width - self.gap, self.rect[3] - self.line_width - self.gap)
        print rect
        for degree in range(degree_start, degree_stop + 1):
            color_i.r = color_i.r + (color_end.r - color_start.r) / (degree_stop - degree_start) * (
                degree - degree_start)
            color_i.g = color_i.g + (color_end.g - color_start.g) / (degree_stop - degree_start) * (
                degree - degree_start)
            color_i.b = color_i.b + (color_end.b - color_start.b) / (degree_stop - degree_start) * (
                degree - degree_start)
            pygame.draw.arc(self.surface, color.green, rect, math.radians(degree), math.radians(degree), 10)
        pygame.draw.rect(self.surface, color.blue, rect, 5)
        pygame.draw.circle(self.surface,color.red,self.position,self.radius-self.line_width-self.gap,1)
