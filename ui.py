import pygame
import button

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 24)
SMALL_FONT = pygame.font.SysFont("Arial", 20)

BARRIER_WIDTH = 5


class UI:

    def drawUI(self, screen: pygame.display, ui_boundary):
        self.UIPanel = pygame.Rect(ui_boundary, 0, screen.get_width(), screen.get_height())
        self.UIBarrier = pygame.Rect(ui_boundary, 0, BARRIER_WIDTH, screen.get_height())
        self.Button1 = button.Button(ui_boundary, 0)

    def __init__(self, screen, ui_boundary):
        self.drawUI(screen, ui_boundary)
