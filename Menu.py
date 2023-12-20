import pygame
import Game

class Button:
    """Создание кнопок"""
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw_button(self, x, y, message, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(Game.display, (166, 100, 232), (x, y, self.width, self.height))

                if click[0] == 1 and action is not None:
                    action()
        else:
            pygame.draw.rect(Game.display, (255, 255, 255), (x, y, self.width, self.height))