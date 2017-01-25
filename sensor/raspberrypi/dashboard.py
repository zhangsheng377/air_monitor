import pygame
import color
import math

if ~pygame.font.get_init():
    pygame.font.init()


class DASHBOARD(pygame.sprite.Sprite):
    def __init__(self, surface, position, radius, index, color_bg):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.radius = radius
        self.line_width = int(math.ceil(self.radius / 9))
        self.gap = int(max(math.ceil(self.line_width / 5.0), 2))
        # self.arc_width = int(math.ceil(self.line_width * 5))
        self.arc_width = self.line_width
        self.position = position
        self.index = index
        self.font_width = int(self.arc_width * 1.5)
        self.font = pygame.font.Font(None, self.font_width)
        self.rect = (self.position[0] - self.radius, self.position[1] - self.radius, self.radius * 2, self.radius * 2)
        self.color_bg = color_bg

    def draw(self):
        # pygame.draw.circle(self.surface, color.grey, self.position, self.radius, self.line_width)
        self.draw_blendcolor_arc(self.radius, self.line_width, color.grey, color.grey, 0, 360, 20)
        # text_index = self.font.render(str(self.index), True, color.red)
        # self.surface.blit(self.text_index, self.position)
        # pygame.draw.aaline(self.surface, color.red, (self.position[0] - self.radius, self.position[1]),(self.position[0] + self.radius, self.position[1]), 2)
        # pygame.draw.aaline(self.surface, color.red, (self.position[0], self.position[1] - self.radius),(self.position[0], self.position[1] + self.radius), 2)
        self.draw_blendcolor_arc(self.radius - self.line_width - self.gap, self.arc_width, color.red, color.green, -60,
                                 232, 10)
        # pygame.draw.rect(self.surface, color.red, self.rect, 4)
        self.draw_scale(0, 360, self.line_width, self.color_bg, color.white)

    def draw_blendcolor_arc(self, radius, width, color_start, color_end, degree_start, degree_stop, step):
        color_gap = (color_end.r - color_start.r, color_end.g - color_start.g, color_end.b - color_start.b)
        color_i = [color_start[0], color_start[1], color_start[2]]
        rect = (self.position[0] - radius, self.position[1] - radius, radius * 2, radius * 2)
        for degree in range(degree_start, degree_stop + 1):
            color_i[0] = int(
                color_start[0] + color_gap[0] * 1.0 / (degree_stop - degree_start) * (degree - degree_start))
            color_i[1] = int(
                color_start[1] + color_gap[1] * 1.0 / (degree_stop - degree_start) * (degree - degree_start))
            color_i[2] = int(
                color_start[2] + color_gap[2] * 1.0 / (degree_stop - degree_start) * (degree - degree_start))
            pygame.draw.arc(self.surface, color_i, rect, math.radians(degree), math.radians(degree + step), width)

    def draw_scale(self, least, highest, width, color_bg, color_number):
        step = (highest - least) / 12
        gap_number = [self.font_width / 3 * 1, self.font_width / 3 * 1, 0, self.font_width / 12 * 1,
                      self.font_width / 20 * 1, self.font_width / 20, self.font_width / 8 * 5, self.font_width / 2 * 2,
                      self.font_width / 4 * 5, self.font_width / 3 * 4, self.font_width / 4 * 4]
        degree_offset_number = [-3, -2, -3, -3, 3, 6, 5, 8, 3, -2, -8]
        for i in range(0, 11):
            degree = 240 + i * (-30)
            rate_cos = math.cos(math.radians(degree))
            rate_sin = math.sin(math.radians(degree))
            pygame.draw.aaline(self.surface, color_bg,
                               (self.position[0] + rate_cos * self.radius, self.position[1] - rate_sin * self.radius), (
                                   self.position[0] + rate_cos * (self.radius - width),
                                   self.position[1] - rate_sin * (self.radius - width)), 0)
            number = i * step + least
            rate_cos = math.cos(math.radians(degree + degree_offset_number[i]))
            rate_sin = math.sin(math.radians(degree + degree_offset_number[i]))
            text_number = self.font.render(str(number), True, color_number)
            radius_number = self.radius - self.line_width - self.arc_width - (self.gap) * 2 - gap_number[i]
            self.surface.blit(text_number, (
            self.position[0] + rate_cos * radius_number, self.position[1] - rate_sin * radius_number))
