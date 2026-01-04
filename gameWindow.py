import dataclasses

import pygame
import clickerWindow
from ui import UI
from clickerWindow import ClickerWindow

class GameWindow:

    uiBoundary = 750
    def __init__(self, screen):
        self.ui = UI(screen, self.uiBoundary)
        self.gameWindow = ClickerWindow(screen, self.uiBoundary)
    def update(self, screen):
        pygame.draw.rect(screen, (30, 30, 30), self.ui.UIPanel)
        pygame.draw.rect(screen, (40, 40, 40), self.ui.UIBarrier)
        pygame.draw.rect(screen, (20, 20, 20), self.gameWindow.GamePanel)
