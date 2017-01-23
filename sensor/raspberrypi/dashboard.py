import pygame
import color

if ~pygame.font.get_init():
    pygame.font.init()


class DASHBOARD(pygame.sprite.Sprite):
    def __init__(self, surface, size, position, radius, index):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.size = size
        self.radius = radius
        self.line_width = self.radius / 45
        self.position = position
        self.index = index
        self.font = pygame.font.Font(None, 36)
        self.text_index = self.font.render(str(self.index), True, color.red)

    def draw(self):
        pygame.draw.circle(self.surface, color.grey, self.position, self.radius, self.line_width)
        self.surface.blit(self.text_index, self.position)
        pygame.draw.line(self.surface, color.red, (self.position[0] - self.radius, self.position[1]),
                         (self.position[0] + self.radius, self.position[1]), 2)
        pygame.draw.line(self.surface, color.red, (self.position[0], self.position[1] - self.radius),
                         (self.position[0], self.position[1] + self.radius), 2)

        # def draw_blendcolor_arc(self,color_start,color_end,rect,angle_start,angle_stop):
        #   pygame

    def change_size(self, size):
        self.radius = self.radius * min(size[0] / self.size[0], size[1] / self.size[1])
        self.line_width = self.radius / 45
        self.position = (self.position[0] * size[0] / self.size[0], self.position[1] * size[1] / self.size[1])
        self.size = size
