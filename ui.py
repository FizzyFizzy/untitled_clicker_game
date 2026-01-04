import pygame
import button

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 24)
SMALL_FONT = pygame.font.SysFont("Arial", 20)

UI_WIDTH = 220


class UI:

    def drawUI(self, screen: pygame.display):
        self.UIPanel = pygame.Rect(screen.get_width() - UI_WIDTH, 0, UI_WIDTH, screen.get_height())
        print(screen.get_width() - UI_WIDTH, 0, UI_WIDTH, screen.get_height())

    def __init__(self, screen):
        self.drawUI(screen)
