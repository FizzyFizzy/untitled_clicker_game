import pygame


class Button:
    DARK_GRAY = (30,30,30)
    LIGHT_GRAY = (200,200,200)
    WHITE = (255,255,255)

    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 50
    BUTTON_PADDING = 10
    BUTTON_ACTIVE = True

    def drawButton(self, UIwindowLeftBound, UIwindowTopBound):
        buttonTop = UIwindowTopBound + self.BUTTON_PADDING
        buttonLeft = UIwindowLeftBound + self.BUTTON_PADDING
        self.Button = pygame.Rect(buttonLeft, buttonTop, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

    def __init__(self, UIwindowLeftBound, UIwindowTopBound):
        self.drawButton(UIwindowLeftBound, UIwindowTopBound)