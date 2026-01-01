import pygame


def main():
    pygame.init()
    icon = pygame.image.load("icon.png")

    #screen setup
    WIDTH, HEIGHT = 1000, 1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Untitled Clicker Game")
    pygame.display.set_icon(icon)

    #main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()