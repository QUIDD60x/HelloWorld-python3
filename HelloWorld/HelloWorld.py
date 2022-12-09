

import pygame

# Initializes Pygame.
pygame.init()

# Sets up the window.
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello, World!")

# Creates a font. I'm using Comic Sans because I deserved to be neutered.
font = pygame.font.SysFont("Comic Sans", 60)

# Creates a text surface and text rectangle.
text_surface = font.render("Hello, World!", True, (255, 255, 255))
text_rect = text_surface.get_rect()
text_rect.center = (200, 200)

# Main loop.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Draws the text to the screen.
    window.fill((0, 0, 0))
    window.blit(text_surface, text_rect)
    pygame.display.update()