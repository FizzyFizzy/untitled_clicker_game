import pygame


class ClickerWindow:
    def drawGame(self, screen: pygame.display, ui_boundary):
        self.GamePanel = pygame.Rect(0, 0, ui_boundary, screen.get_height())

    def __init__(self, screen: pygame.display, ui_boundary):
        self.drawGame(screen, ui_boundary)
