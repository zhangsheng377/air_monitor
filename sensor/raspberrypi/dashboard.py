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
        self.gap = int(max(math.ceil(self.line_width / 5.0),2))
        self.arc_width = int(math.ceil(self.line_width * 5))
        self.position = position
        self.index = index
        self.font = pygame.font.Font(None, 36)
        self.text_index = self.font.render(str(self.index), True, color.red)
        # self.rect = (self.position[0] - self.radius, self.position[1] - self.radius, self.position[0] + self.radius,self.position[1] + self.radius)
        self.rect = (self.position[0] - self.radius, self.position[1] - self.radius, self.radius * 2, self.radius * 2)

    def draw(self):
        pygame.draw.circle(self.surface, color.grey, self.position, self.radius, self.line_width)
        self.surface.blit(self.text_index, self.position)
        #pygame.draw.aaline(self.surface, color.red, (self.position[0] - self.radius, self.position[1]),(self.position[0] + self.radius, self.position[1]), 2)
        #pygame.draw.aaline(self.surface, color.red, (self.position[0], self.position[1] - self.radius),(self.position[0], self.position[1] + self.radius), 2)
        self.draw_blendcolor_arc(color.red, color.green, -60, 240)
        # pygame.draw.rect(self.surface, color.red, self.rect, 4)
        # print self.rect, self.radius * 2

    def draw_blendcolor_arc(self, color_start, color_end, degree_start, degree_stop):
        # degree_start = int(degree_start)
        # degree_stop = int(degree_stop)
        # print color_start,color_end
        color_gap = (color_end.r - color_start.r, color_end.g - color_start.g, color_end.b - color_start.b)
        # color_start= (color_start.r, color_start.g, color_start.b)
        color_i = [color_start[0], color_start[1], color_start[2]]
        rect = (self.rect[0] + self.line_width + self.gap, self.rect[1] + self.line_width + self.gap,
                (self.radius - self.line_width - self.gap) * 2, (self.radius - self.line_width - self.gap) * 2)
        step = 10
        for degree in range(degree_start, degree_stop - step + 1):
            color_i[0] = int(
                color_start[0] + color_gap[0] * 1.0 / (degree_stop - degree_start) * (degree - degree_start))
            color_i[1] = int(
                color_start[1] + color_gap[1] * 1.0 / (degree_stop - degree_start) * (degree - degree_start))
            color_i[2] = int(
                color_start[2] + color_gap[2] * 1.0 / (degree_stop - degree_start) * (degree - degree_start))
            # print color_i,degree - degree_start,degree_stop - degree_start,color_gap,color_start
            pygame.draw.arc(self.surface, color_i, rect, math.radians(degree), math.radians(degree + step),
                            self.arc_width)
            # pygame.draw.rect(self.surface, color.blue, rect, 5)
            # pygame.draw.arc(self.surface, color.green, rect, math.radians(degree_start), math.radians(degree_stop), 10)
            # pygame.draw.circle(self.surface, color.red, self.position, self.radius - self.line_width - self.gap, 1)
