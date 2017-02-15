# coding=utf-8

import pygame
import color
import math

if ~pygame.font.get_init():
    pygame.font.init()


class DASHBOARD(pygame.sprite.Sprite):
    def __init__(self, surface, position, radius, name, color_bg, least, highest):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.radius = radius
        self.line_width = int(math.ceil(self.radius / 9.0))
        self.gap = int(max(math.ceil(self.line_width / 5.0), 2))
        self.arc_width = self.line_width
        self.position = position
        self.name = name.decode('utf-8', 'ignore').encode('gbk')
        #print self.name
        self.font_width = int(self.arc_width * 1.5)
        # self.font = pygame.font.SysFont('楷体', self.font_width)
        self.font = pygame.font.Font(None, self.font_width)
        self.rect = (self.position[0] - self.radius, self.position[1] - self.radius, self.radius * 2, self.radius * 2)
        self.color_bg = color_bg
        self.least = least
        self.highest = int(highest / 10.0 * 12)
        self.scale_gap = int(self.gap / 4.0 * 3)
        self.needle_length = self.radius - self.line_width - self.arc_width - self.font_width - (self.gap) * 5
        self.needle_width = int(max(self.arc_width / 2.0, 4))
        self.origin_radius = int(self.arc_width / 2.0)
        self.origin_gap = int(self.scale_gap / 2.0)

    def draw(self, value):
        self.draw_blendcolor_arc(self.radius, self.line_width, color.grey, color.grey, 0, 360, 20)
        self.draw_blendcolor_arc(self.radius - self.line_width - self.gap, self.arc_width, color.red, color.green, -60,
                                 232, 10)
        self.draw_scale(self.least, self.highest, self.line_width, self.color_bg, color.white)
        self.draw_needle(value, color.red)

        temp = 0
        old_font_width = self.font_width
        if (self.name == '甲醛'):
            # print self.name
            self.font_width = self.font_width / 4 * 3
            self.font = pygame.font.SysFont('楷体', self.font_width)
            temp = self.font_width / 10 * 3
        text_name = self.font.render(self.name.decode('utf-8', 'ignore'), True, color.white)
        distance_text_name = self.radius - self.line_width - self.gap - self.font_width - temp / 4 * 15
        self.surface.blit(text_name, (
            self.position[0] - len(self.name) * self.font_width / 5 + temp, self.position[1] + distance_text_name))
        temp = 0
        self.font_width = old_font_width
        self.font = pygame.font.Font(None, self.font_width)

        str_value = "%.2f" % value
        text_value = self.font.render(str_value, True, color.pink)
        distance_text_value = self.radius - self.line_width - self.arc_width - self.font_width * 2 - (self.gap) * 6
        # self.surface.blit(text_value, (self.position[0] - self.font_width, self.position[1] + distance_text_value))
        self.surface.blit(text_value, (
            self.position[0] - len(str_value) * self.font_width / 6, self.position[1] + distance_text_value))




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
            pygame.draw.line(self.surface, color_bg,
                             (self.position[0] + rate_cos * self.radius, self.position[1] - rate_sin * self.radius), (
                                 self.position[0] + rate_cos * (self.radius - width),
                                 self.position[1] - rate_sin * (self.radius - width)), self.scale_gap)
            number = i * step + least
            rate_cos = math.cos(math.radians(degree + degree_offset_number[i]))
            rate_sin = math.sin(math.radians(degree + degree_offset_number[i]))
            text_number = self.font.render(str(number), True, color_number)
            radius_number = self.radius - self.line_width - self.arc_width - (self.gap) * 2 - gap_number[i]
            self.surface.blit(text_number, (
                self.position[0] + rate_cos * radius_number, self.position[1] - rate_sin * radius_number))

    def draw_needle(self, value, color_needle):
        degree = 240 - (value - self.least) * 1.0 / (self.highest - self.least) * 360
        rate_cos = math.cos(math.radians(degree))
        rate_sin = math.sin(math.radians(degree))
        position_end = (
            int(self.position[0] + rate_cos * self.needle_length),
            int(self.position[1] - rate_sin * self.needle_length))
        pygame.draw.line(self.surface, color_needle, self.position, position_end, self.needle_width)
        pygame.draw.circle(self.surface, color_needle, position_end, int(self.needle_width / 24.0 * 14), 0)
        pygame.draw.circle(self.surface, color.white, self.position, self.origin_radius, 0)
        pygame.draw.circle(self.surface, self.color_bg, self.position, self.origin_radius - self.origin_gap, 1)
