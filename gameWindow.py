import dataclasses

import pygame
import clickerWindow
from ui import UI


class GameWindow:

    def __init__(self, screen):
        self.ui = UI(screen)
    def update(self, screen):
        pygame.draw.rect(screen, (30, 30, 30), self.ui.UIPanel)
